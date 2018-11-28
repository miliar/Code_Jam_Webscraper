#include <iostream>
#include <stdlib.h>
using namespace std;

int compare (const void * a, const void * b)
{
  if ( *(double*)a <  *(double*)b ) return -1;
  if ( *(double*)a == *(double*)b ) return 0;
  if ( *(double*)a >  *(double*)b ) return 1;
}

int main() {
	// your code goes here
	int t,tc=1;
	cin>>t;
	while(t--){
		int i,j,jr;
		int DW=0,W=0;
		int n;
		cin>>n;
		double* bn = new double[n];
		double* bk = new double[n];
		
		for(i=0;i<n;i++)cin>>bn[i];
		for(i=0;i<n;i++)cin>>bk[i];
		
		qsort(bn,n,sizeof(double),compare);
		qsort(bk,n,sizeof(double),compare);
		
		for(i=j=0,jr=n-1;i<n;i++){
			//DW
			if (bn[i]>bk[j]){
				DW++; j++;
			}
			//W
			if (bn[n-1-i]>bk[jr]){
				W++;
			} else jr--;
		}
		
		cout<<"Case #"<<tc<<": "<<DW<<" "<<W<<endl;
		tc++;
	}
	return 0;
}