#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<vector>
#include<map>
#include<list>
#include<string.h>
using namespace std;
int main()
{
	int t,kp,a,counti,val;
	cin>>kp;
	for(int t=1;t<=kp;t++){
		counti=0;
		
		cin>>a;
		int arr[5][5];
		for(int i=1;i<5;i++)
			for(int j=1;j<5;j++)
				cin>>arr[i][j];
		
		
		int crr[4];
		int k=-1;
		for(int j=1;j<5;j++)
			crr[++k]=arr[a][j];
		cin>>a;
		for(int i=1;i<5;i++)
			for(int j=1;j<5;j++)
				cin>>arr[i][j];
		
		
		int drr[4];
		k=-1;
		for(int j=1;j<5;j++)
			drr[++k]=arr[a][j];
		
		
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(crr[i]==drr[j]){val=crr[i];counti++;}
	
	
		if(counti==1)
			cout<<"Case #"<<t<<": "<<val<<endl;
		else if(counti>1)
			cout<<"Case #"<<t<<": "<<"Bad magician!"<<endl;
		else if(counti<1)
			cout<<"Case #"<<t<<": "<<"Volunteer cheated!"<<endl;
		
				
	}
	
	
	
	return 0;
}

