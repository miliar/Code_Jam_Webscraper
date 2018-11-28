#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

int t,n;

int getMax(int arr[], int n)
{
    int mx = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > mx)
            mx = arr[i];
    return mx;
}
 
void countSort(int arr[], int n, int exp)
{
    int output[n]; 
    int i, count[10] = {0};
 
    
    for (i = 0; i < n; i++)
        count[ (arr[i]/exp)%10 ]++;
 
    for (i = 1; i < 10; i++)
        count[i] += count[i - 1];
 
    for (i = n - 1; i >= 0; i--)
    {
        output[count[ (arr[i]/exp)%10 ] - 1] = arr[i];
        count[ (arr[i]/exp)%10 ]--;
    }
 
    for (i = 0; i < n; i++)
        arr[i] = output[i];
}
 

void radixsort(int arr[], int n)
{
    int m = getMax(arr, n);
    for (int exp = 1; m/exp > 0; exp *= 10)
        countSort(arr, n, exp);
}
void reverseArray(int arr[], int start, int end)
{
    int temp;
    while (start < end)
    {
        temp = arr[start];   
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }   
} 
int sum_p(int arr[],int size){
	int sum = 0;
	for (int i = 0; i < size; ++i)
	{
		sum += arr[i]; 
	}
	return sum;
}
int main(){
	cin>>t;
	int k = t;
	while(t){
		cin>>n;
		int party[n];
		char alpha[n];
		for (int i = 0; i < n; ++i)
		{
			cin>>party[i];
		}
		int i = 0; 
		char a = 'A'; 
		int add = 0;
		cout<<"Case #"<<k-t+1<<": ";
		while (i<n){
			alpha[i] = (char)(a + add);
			++i;
			++add;
		}
		if(n==2){
			while(party[0]!=0){
				cout<<"AB ";
				party[0]--;
			}
		}
		else{
			while(sum_p(party,n)!=0){
				int index[n];
				int temp[n];
				int party_sort[n] = {0};
				for (int i = 0; i < n; ++i)
				{
					party_sort[i] = party[i];
					temp[i] = party[i];
				}
				radixsort(party_sort,n);
				reverseArray(party_sort,0,n-1);
				// for (int i = 0; i < n; ++i)
				// {
				// 	/* code */
				// 	cout<<party_sort[i]<<" ";
				// }
				// cout<<endl;
				int k = 0;
				for(int i = 0;i<n;i++){
					for(int j = 0;j<n;j++){
						if(party_sort[i] == temp[j]){
							index[k] = j;
							temp[j] = -5;
							k++;
							break;
						}
					}
				}

				if((party_sort[0]>party_sort[1]) && (party_sort[0]!=1)){
					party[index[0]] = party[index[0]] - 2;
					cout<<alpha[index[0]]<<alpha[index[0]]<<" ";
				}
				else if(party_sort[0]!=1){
					party[index[0]]--;
					party[index[1]]--;
					cout<<alpha[index[0]]<<alpha[index[1]]<<" ";
				}
				else if (party_sort[0] == 1)
				{
					if(((sum_p(party_sort,n)%2) == 1) && (n==3)){
						party[index[0]]--;
						cout<<alpha[index[0]]<<" ";
					}
					else{
						party[index[0]]--;
						party[index[1]]--;
						cout<<alpha[index[0]]<<alpha[index[1]]<<" ";
					}
				}
			}
			
		}
		cout<<endl;
		t--;
	}
	
}