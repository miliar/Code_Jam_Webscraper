#include <bits/stdc++.h>
using namespace std;

double arr[1010];
double brr[1010];

int main()
{
	int test;
	long long int n,i,j,k;
	cin >> test;
	for(k=1;k<=test;k++){
		
		cin >> n;
		memset(arr,0,sizeof(arr));
		memset(brr,0,sizeof(brr));

		for(i=0;i<n;i++)
			cin >> arr[i];

		for(i=0;i<n;i++)
			cin >> brr[i];

		sort(arr,arr+n);
		sort(brr,brr+n);
		long long int count = 0;
		i = 0;
		j = 0;
		while(1){
			if(arr[i]>brr[j]){
				count++;
				i++;
				j++;
			}
			else
				i++;
			if((i==n)||(j==n))
				break;
		}
		cout<<"Case #"<<k<<": "<<count;
		count = 0;
		i = 0;
		j = 0;
		while(1){
			if(arr[i]<brr[j]){
				count++;
				i++;
				j++;
			}
			else
				j++;
			if((i==n)||(j==n))
				break;
		}
		int res;
		res = n-count;
		cout <<" " <<res << endl;
	}
	return 0;
}
	
						
			
		
