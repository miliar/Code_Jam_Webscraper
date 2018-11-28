// 123.cpp : 定义控制台应用程序的入口点。
//



#include "stdafx.h"
#include <iostream>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include <iomanip>
#include <fstream>
#include<bitset>
 using namespace std;
 int a[20];
 inline bool ishuiwen(long long n)
 {
	 long long t=n;
	 int k=1;
	 while(t>=10)
	 {
		 a[k]=t%10;
		 t/=10;
		 k++;
	 }
	 if(t>0)a[k]=t;
	 for(int i=1;i<=k>>1;i++)
		 if(a[i]!=a[k-i+1])return 0;
	 return 1;
 }
 int main()
 {
	 ifstream inFile;  
	 ofstream outFile;  
	 inFile.open("C-small-attempt3.in");  
	 outFile.open("outData.out");
	 char * b=new char[10000001];
	 memset(b,0,10000001);
	 long long square=0;
	 for(int i=1;i<=10000000;i++)
	 {
         square+=2*(i-1)+1;
		 if(ishuiwen(i)&&ishuiwen(square))b[i]=1;
	 }
	 int t1=b[1];
	 t1=b[2];
	 t1=b[3];
	 t1=b[4];
	//for(int i=1;i<=10000000;i++)
	 //{
	//	 if(b[i]==1)outFile<<i<<endl;
	// }
	 int T;
	 inFile>>T;
	 long long a1,a2;
	 int b1,b2;
	 int count;
	 for(int icases=1;icases<=T;icases++)
	 {
		 inFile>>a1>>a2;
		 b1=pow(a1,0.5);
		 //if(b1*b1<a1)b1++;
		 //b1=max(1,b1-10);
		 b2=pow(a2,0.5);
		 b2++;
		 //b2=min(10000000,b2+100);
		 count=0;
		 for(int i=b1;i<=b2;i++)
		 {
			 count+=b[i];
		 }
		 if(b1*b1<a1)count-=b[b1];
		 if(b2*b2>a2)count-=b[b2];
		 if((b2-1)*(b2-1)>a2)count-=b[b2-1];
		 outFile<<"Case #"<<icases<<": "<<count<<endl;
	 }
	  inFile.close();  
	  outFile.close();
 }