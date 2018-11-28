#include<bits/stdc++.h>
using namespace std;
int mul[5][5]={
			 0,0,0,0,0,
	         0,1,2,3,4,	
	         0,2,-1,4,-3,
	         0,3,-4,-1,2,
	         0,4,3,-2,-1
			 };
 
int div1[5][5]={
			 0,0,0,0,0,
	         0,1,-2,-3,-4,
	         0,2,1,4,-3,
	         0,3,-4,1,2,
	         0,4,3,-2,1
			 };
 
int arr[10002];
 
int val(char ch)
{
	if(ch=='i')
	return 2;
	if(ch=='j')
	return 3;
	if(ch=='k')
	return 4;
}
 
int main()
{
	int t,l,x;
	cin>>t;
	string str,s;
	for(int k=1; k<=t; k++)
	{
		int i,j;
		cin>>l>>x;
		cin>>str;
		s=str;
		for(j=0; j<x-1; j++)
		str=str+s;
		
		arr[1]=val(str[0]);
		for(int j=2; j<=str.length(); j++)
		{
			if(arr[j-1]>0)
			arr[j]=mul[abs(arr[j-1])][val(str[j-1])];
			else
			arr[j]=-mul[abs(arr[j-1])][val(str[j-1])];
		}
		bool fl=0;
		int val1,val2,val3,len1,len2,len3;
		for(int j=1; j<=str.length(); j++)
		{
			for(int k=j+1; k<=str.length(); k++)
			{
				val1=arr[j];
				val2=arr[k];
				val3=arr[str.length()];
 
				if(val1!=2)
				continue;
 
				if(val2>0 && val3>0 || val1<0 && val2<0)
				len2=div1[abs(val3)][abs(val2)];
				else
				len2=-div1[abs(val3)][abs(val2)];
 
 				if(val1>0 && val2>0 || val1<0 && val2<0)
				len1=div1[abs(val2)][abs(val1)];
				else
				len1=-div1[abs(val2)][abs(val1)];
 
				if(len1==3 && len2==4)
				{
					fl=1;
					break;
				}
			}
			if(fl==1)
			{
				break;
			}
		}
		if(fl==1)
		cout<<"Case #"<<k<<": "<<"YES"<<endl;
		else
		cout<<"Case #"<<k<<": "<<"NO"<<endl;
	}
	return 0;
}
