#include<bits/stdc++.h>
using namespace std;
long long a[11];
void get()
{
	long long i,j,pow;
	for(j=3;j<=10;j++)
	{
		a[j]=0;
		i=a[2];
		pow=1;
		while(i>0)
		{
			a[j]+=((i&1)*pow);
			i>>=1;
			pow*=j;
		}
	}
}
		
int main()
{
	int i,count=0;
	a[2]=32769;
	cout<<"Case #1:\n";
	while(count<50)
	{
		get();
		//for(i=2;i<=10;i++) cout<<a[i]<<' ';cout<<endl;
		for(i=2;i<=10;i++)
		{
			if((a[i])%2==0) continue;
			if((a[i])%3==0) continue;
			if((a[i])%5==0) continue;
			if((a[i])%7==0) continue;
			if((a[i])%11==0) continue;
			if((a[i])%13==0) continue;
			if((a[i])%17==0) continue;
			if((a[i])%19==0) continue;
			break;
		}
		if(i==11) 
		{
			cout<<a[10]<<' ';
			for(i=2;i<=10;i++)
			{
				if((a[i])%2==0) {cout<<"2 ";continue;}
				if((a[i])%3==0) {cout<<"3 ";continue;}
				if((a[i])%5==0) {cout<<"5 ";continue;}
				if((a[i])%7==0) {cout<<"7 ";continue;}
				if((a[i])%11==0) {cout<<"11 ";continue;}
				if((a[i])%13==0) {cout<<"13 ";continue;}
				if((a[i])%17==0) {cout<<"15 ";continue;}
				if((a[i])%19==0) {cout<<"17 ";continue;}
				break;
			}
			cout<<endl;
			count++;
		}
		a[2]+=2;
	}
}
