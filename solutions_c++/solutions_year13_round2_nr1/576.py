#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

ofstream fout("out.txt");

long long int min(long long int a,long long int b){
	return (a<b)?a:b;
}
int T;
long long int A,n,sol,curr;
long long int arr[101];
int main(){
	cin>>T;
	for(int g=1;g<=T;g++){
		cin>>A>>n;
		for(int i=0;i<n;i++){
			cin>>arr[i];
		}
		sol=n,curr=0;
		sort(arr,arr+n);
		if(A!=1)
		for(int i=0;i<n;i++){
			while(A<=arr[i]){
				A+=A-1;
				curr++;
			}
			sol=min(sol,curr+n-i-1);
			A+=arr[i];
		}
		fout<<"Case #"<<g<<": "<<sol<<endl;
	}
}