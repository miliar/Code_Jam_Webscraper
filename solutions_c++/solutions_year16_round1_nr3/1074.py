#include<iostream>
#include<string>
#include<list>
#include<set>
#include<algorithm>

using namespace std;

set <pair<int, int> > A;
int maks;
void print( list<int> l){
	
    int tab[100];
    int k = 0;
    for(list<int>::iterator it=l.begin(); it!=l.end() ; ++it)
	{
		tab[k] = *it;
		k++;
	}
			
	do{
	//	cout <<  "sprawdzam ";
		bool satysfakcja[100];
		bool K = true;
		for(int i = 0; i < k; i++)
		{
			//cout << tab[i] << " ";
			satysfakcja[tab[i]] = 0;
		}
		//cout << endl << endl << endl;

		for(int i = 1; i < k-1; i++)
		{
			//cout << tab[i] << " " << tab[i - 1] << endl;
			if(A.find(make_pair(tab[i], tab[i - 1])) != A.end())
				satysfakcja[tab[i]] = 1;
				
			if(A.find(make_pair(tab[i - 1], tab[i])) != A.end())
				satysfakcja[tab[i - 1]] = 1;
				
			if(A.find(make_pair(tab[i], tab[i - 1])) == A.end()){
				if(A.find(make_pair(tab[i], tab[i + 1])) == A.end()){
					goto X;
				}
			}
		}
		//cout << tab[0] << " " << tab[k - 1] << endl;
		if(A.find(make_pair(tab[k-2], tab[k - 1])) != A.end())
				satysfakcja[tab[k-2]] = 1;
				
			if(A.find(make_pair(tab[k - 1], tab[k-2])) != A.end())
				satysfakcja[tab[k - 1]] = 1;
		if(A.find(make_pair(tab[0], tab[k - 1])) != A.end())
				satysfakcja[tab[0]] = 1;
				
			if(A.find(make_pair(tab[k - 1], tab[0])) != A.end())
				satysfakcja[tab[k - 1]] = 1;
	
		for(int i = 0; i < k; i++)
			if(satysfakcja[tab[i]] == false)
			{
				K = false;
				break;
			}
		if(K  == true)
		{
			maks = max(maks, k);
			return;
		}
		X:;
	}while(next_permutation(tab, tab+k));
    
}

void subset(int arr[], int size, int left, int index, list<int> &l){
    if(left==0){
        print(l);
        return;
    }
    for(int i=index; i<size;i++){
        l.push_back(arr[i]);
        subset(arr,size,left-1,i+1,l);
        l.pop_back();
    }

}     

int main(){
    int array[10]={1,2,3,4,5,6,7,8,9,10};
    list<int> lt;   
	int z;
	cin >> z;
	for(int p = 1; p <=z; p++)
	{
			int n;
			cin >> n;
			for(int i = 1; i <= n; i++)
			{
				int a;
				cin >> a;
				A.insert(make_pair(i, a));
			}
			maks = 0;
			
			for(int i = n; i >= 1; i--)
			{
				subset(array, n, i, 0, lt);
			}
			cout << "Case #" << p << ": " <<maks << endl;
			A.clear();
	}

    return 0;
}
