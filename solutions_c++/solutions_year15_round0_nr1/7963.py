#include<iostream>
#include<conio.h>
#include<math.h>
#include<cstdio>
#include<stdio.h>
using namespace std;

int main()
{
 unsigned long long arr[50];
 int count=0;
	freopen("A-large.in","r",stdin);
    freopen("LargeA.in","w",stdout);
  unsigned long long int T;           
  cin>>T;
  for(unsigned long long int r=1;r<=T;r++)
  {
  	unsigned long long int  req=0;
  	unsigned long long int sum = 0;
  	int s;
  	cin>>s;
  	
  	string t;
  	cin>>t;                                                                                          
  	for(int  i=0;i<=s;i++)
  	{
  		int xx = t[i]-'0';
  		int re=0;
		while(sum+re<i)
  				re++;
  		req+=re;
  		sum+=xx;
  		sum+=re;
		 		
	  }
  	
    cout<<"Case"<<" #"<<r<<":"<<" "<<req<<"\n";
  }
                     
   getch();
   return(0);
}
