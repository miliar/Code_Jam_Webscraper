#include<algorithm>
#include<vector>
#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
int main(){
	freopen("C.in","r",stdin); 
	freopen("CodeJam.out","w",stdout);
	
	int n,i,j,k;
	double A[1000],B[1000];
	int flag;
	
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		printf("Case #%d: ",t);
		cin>>n;
		memset(A,0,sizeof(A));
		memset(B,0,sizeof(B));
		for(i=0;i<n;++i) cin>>A[i];
		for(i=0;i<n;++i) cin>>B[i];
		sort(A,A+n);
		sort(B,B+n);
		/*
		for(i=0;i<n;i++)cout<<A[i]<<" ";
		cout<<endl;
		for(i=0;i<n;i++)cout<<B[i]<<" ";
		cout<<endl;
		*/
		i=0;j=n-1;k=0;
		while(i<n){
			if(A[i]>B[k]) ++k;
			++i;
		}
		
		for(i=0;i<n;++i){
			j=0;
			while(j<n && A[i]>B[j]) ++j;
			if(j==n) break;
			B[j]=0.00;
		}
		flag = n-i;
		
		printf("%d %d\n",k,flag);
	}//while(1); 
	return 0;
}

