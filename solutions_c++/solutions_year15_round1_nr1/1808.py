#include<iostream>
#include<cstdio>
using namespace std;

int main(){
	long int t,n,m1,m2,maxint,caseno=1;
	scanf("%ld",&t);
	while(t--){
		scanf("%ld",&n);
		long int arr[n];
		for(int i=0;i<n;i++)
			scanf("%ld",&arr[i]);
		m1 = m2 = 0;
		maxint = -1;
		for(int i=1;i<n;i++){
			if(arr[i]<=arr[i-1])
			{
				m1+=arr[i-1]-arr[i];
				maxint = max(maxint,arr[i-1]-arr[i]);
			}
		}
		for(int i=0;i<n-1;i++){
			m2+=min(arr[i],maxint);
		}
		cout<<"Case #"<<caseno++<<": "<<m1<<" "<<m2<<endl;
	}
}
