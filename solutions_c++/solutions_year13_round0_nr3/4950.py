//============================================================================
// Name        : FairSquare.cpp
// Author      : Mostafa Shokrof
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdint.h>
#include <math.h>
#include <map>
#include <stdio.h>
using namespace std;

unsigned long arr[21]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404};

int main() {

	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		unsigned long begin,end;
		cin>>begin>>end;

		int indexbegin,indexend;
		if(begin>404090404)
		{
			indexbegin=21;
		}
		else{
			for(int p=0;p<21;p++)
				if(begin<=arr[p])
				{
					indexbegin=p;
					break;
				}
		}
		if(end>=404090404)
		{
			indexend=21;

		}
		else{
			for(int p=0;p<21;p++)
				if(end<arr[p])
				{
					indexend=p;
					break;
				}
		}

//		if(begin==40409040&&end==40409040)
//		{
//			indexend++;
//		}


		printf("Case #%d: %d\n",i,indexend-indexbegin);
	}
	// double n;
	//	 unsigned int ten[15];
	//	ten[0]=1;
	//	map< double ,int> palindromes;
	//	for(int i=1;i<15;i++)
	//	{
	//		ten[i]=ten[i-1]*10;
	//		//cout<<ten[i]<<endl;
	//	}
	//	double prev=1;
	//	for(int i=0;i<14;i++){
	//		for( unsigned int j=ten[i];j<ten[i+1];j++)
	//		{
	//			//check palindrom
	//			bool palin=true;
	//			for(int p=0;p<=(i/2);p++)
	//			{
	//				int f=j/ten[p]%10;
	//				int l=j/ten[i-p]%10;
	//				if(j/ten[p]%10!=j/ten[i-p]%10)
	//				{
	//					palin=false;
	//					break;
	//				}
	//			}
	//			if(palin)
	//			{
	//				double t=(double)j;
	//				palindromes.insert(pair< double,int>(t,0));
	//				 double sqr=sqrt(t);
	//				if(palindromes.find(sqr)!=palindromes.end())
	//				{
	//					cout<<j<<endl;
	//				}
	//			}
	//		}
	//	}



}
