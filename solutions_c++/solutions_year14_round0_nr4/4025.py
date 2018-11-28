#include<iostream>
#include<stdio.h>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
//int arr[51][51];
double arr[1005];
double brr[1005];
int crr[1005];
int main()
{
	int i,j,t,k,n,a,b,r,ii,l,f,c,m,nao,ken,tst;
	//fstream cin;
	double p,ans,x,y;
	//cin.open("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2014\\Quali\\D\\Small Input.txt",ios::in);
	//freopen("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2014\\Quali\\D\\Small Output.txt","w",stdout);
	cin>>t;
	for(tst=1;tst<=t;tst++)
	{
		cout<<"Case #"<<tst<<": ";
        cin>>n;
        nao=ken=0;
        l=n;
     	for(i=0;i<n;i++)
		 {
 			cin>>arr[i];
 			crr[i]=0;
		 }
     	for(j=0;j<n;j++)cin>>brr[j];
     	sort(arr,arr+n);
     	sort(brr,brr+n);
     	for(i=0;i<n;i++)
     	{
	     	for(j=0;j<n;j++)
	     	{
	     		if(crr[j]==0&&arr[j]>brr[i])
	     		{
		     		crr[j]=1;
		     		nao++;
				break;
		     	}
	     	}
	     	
	     	
	     	
	     	
	     }
	     for(i=0;i<n;i++)crr[i]=0;
 		for(m=0,i=n-1;i>=0;i--)
 		{
 			for(j=0;j<n;j++)
 			{
			 	if(crr[j]==0&&brr[j]>arr[i])
			 	{
	 				crr[j]=1;
	 				break;
	 			}
			 }
			 if(j>=n)m++;
 		}
 		
 		
 		cout<<nao<<" "<<m<<endl;
	}
	return 0;
}