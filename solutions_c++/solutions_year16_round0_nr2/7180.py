#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <stdio.h> 

using namespace std;


int CalculateMove(int a[], int iSize)
{	int iNomiss = 0, iCount = 0, iOne;
	int aTestSize = iSize;

	//for(int i=0;i<iSize;i++)
	//	cout<<a[i];
	//cout<<endl;
	while(aTestSize){
		iOne = iNomiss = 0;
		for(int i = aTestSize-1; i>=0;i--){
			//cout<<a[i];
			if(a[i] == 1 && iNomiss == 0){ --aTestSize;continue;}
			iNomiss = 1;
			a[i] ^= 1;
			iOne = 1;	
		}
		//cout<<endl;
		aTestSize -= iOne;
		iCount += iOne;
	}
	return iCount;
}


int main()
{
	int t, a[200], res;
	char c[200];
	//freopen("input2.txt", "r", stdin);
	//freopen("out2.txt", "w", stdout);
	cin >>t;
	for(int i = 1;i<=t;i++)
	{
		cin>>c;
		
		for(int j=0;j<strlen(c);j++){
			if(c[j] == '-')	
			a[j] = 0;
		 	else a[j] = 1;
		}
		res = CalculateMove(a, strlen(c));	
		cout<<"Case #"<<i<<": "<<res<<endl;
	}	
	return 0;	
}
