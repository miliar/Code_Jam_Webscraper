#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int arr[10];

int main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		string S;
		cin>>S;
		memset(arr,0,10*sizeof(int));
		for(int j=0;j<S.length();j++){
			if(S[j]=='Z')
				arr[0]++;
			if(S[j]=='X')
				arr[6]++;
			if(S[j]=='G')
				arr[8]++;
			if(S[j]=='U')
				arr[4]++;
			if(S[j]=='W')
				arr[2]++;
		}
		int noF=0,noT=0,noO=0,noV=0,noN=0;
		for(int j=0;j<S.length();j++){
			if(S[j]=='F')
				noF++;
			if(S[j]=='O')
				noO++;
			if(S[j]=='T')
				noT++;
			if(S[j]=='V')
				noV++;
			if(S[j]=='N')
				noN++;
		}
		arr[5]=noF-arr[4];
		arr[3]=noT-arr[2]-arr[8];
		arr[1]=noO-arr[0]-arr[4]-arr[2];
		arr[7]=noV-arr[5];
		if((noN-arr[7]-arr[1])%2==0)
			arr[9]=(noN-arr[7]-arr[1])/2;
		else
			cout<<"Some Problem";
		printf("Case #%d: ",i+1);
		for(int j=0;j<10;j++){
			for(int k=0;k<arr[j];k++)
				printf("%d",j);
		}
		printf("\n");
	}
	return 0;
}