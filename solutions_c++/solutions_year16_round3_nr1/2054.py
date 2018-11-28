#include<bits/stdc++.h>
using namespace std;
int n;
int allzero(int a[])
{
	for(int j=0;j<n;j++)
		if(a[j]!=0) return 0;
	return 1;
}
int violating(int a[], int sum)
{
	for(int j=0;j<n;j++)
		if(a[j]>sum/2) return 1;
	return 0;
}
int main()
{
	int t,i,sum,max1,posmax,prev1,pos1,prev2,pos2,t0=1;
	string op;
	cin>>t;
	while(t--)
	{
		op="";
		cin>>n;
		int a[n];
		for(i=0;i<n;i++)
			cin>>a[i];
		cout<<"Case #"<<t0++<<": ";
		while(!allzero(a))
		{
		op="";		
		sum=0;
		for(i=0;i<n;i++)
			sum+=a[i];		
		prev1=INT_MIN;
		pos1=-1;
		max1=INT_MIN;
		posmax=-1;
		for(i=0;i<n;i++)
		{
			if(2*a[i]>=sum && a[i]>prev1)
			{	prev1=a[i];
				pos1=i;
			}
			if(a[i]>max1)
				max1=a[i],posmax=i;
		}
		if(pos1==-1) pos1=posmax;
		if(pos1!=-1 && a[pos1])
		op=op+(char)(pos1+65);
		a[pos1]--;
		sum--;
		prev2=INT_MIN;
		pos2=-1;
		for(i=0;i<n;i++)
		{
			if(2*a[i]>=sum && a[i]>prev2)
			{	prev2=a[i];
				pos2=i;
		}}
		if(pos2!=-1 && a[pos2])
		{op=op+(char)(pos2+65);
		a[pos2]--;}
		if(violating(a,sum-1))
			op=(char)(pos1+65), a[pos2]++;
		cout<<op<< " ";
		}	
	cout<<endl;
	}
	
}
