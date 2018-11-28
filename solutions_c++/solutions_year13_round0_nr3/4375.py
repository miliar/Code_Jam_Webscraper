#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int t, i=0;
	cin>>t;
	int ar[5] = {1, 4, 9, 121, 484};
	while(t>i++){
		
		int a, b, count = 0;
		cin>>a>>b;
		for(int k = 0; k < 5; ++k){
			if(ar[k]<= b && ar[k] >= a){
				++count;
			}
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}
