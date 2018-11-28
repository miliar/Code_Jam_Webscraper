#include<iostream>

using namespace std;
int mx(int* cake,int d)
{
	int maxi=-1;
	for(int i=0;i<d;i++)
	{if(maxi<cake[i]) maxi=cake[i];}
	return maxi;
}
int check(int *cake,int d)
{
	int cake1[d+1], cake2[d+2];
	int maxi=mx(cake,d);
	if(maxi==1) return 1;
	if(maxi==0) return 0;
	for(int i=0;i<d;i++)
	{
		if(cake[i]==0)cake1[i]=0;
		else
		cake1[i]=cake[i]-1;
		cake2[i]=cake[i];
	}
	cake2[d]=0;
	for(int i=0;i<d;i++)
	{
		if(maxi==cake2[i])
		{
			if(maxi==2) {cake2[i]=1;cake2[d]=1;break;}
			else if(maxi==3) {cake2[i]=1;cake2[d]=2;break;}
			else if(maxi==4) {cake2[i]=2;cake2[d]=2;break;}
			else if(maxi==5) {cake2[i]=2;cake2[d]=3;break;}
			else if(maxi==6) {cake2[i]=3;cake2[d]=3;break;}
			else if(maxi==7) {cake2[i]=3;cake2[d]=4;break;}
			else if(maxi==8) {cake2[i]=4;cake2[d]=4;break;}
			else if(maxi==9) {cake2[i]=3;cake2[d]=6;break;}
		}
	}
	int r=1+min(check(cake1,d),check(cake2,d+1));
	return r;
}

		

int main()
{
	int t,q=1,res;
	cin>>t;
	while(q<=t)
	{
		int cp,k=0,sum=0;
		cin>>cp;
		int cake[cp];
		for(int i=0;i<cp;i++)
		{	
			cin>>cake[i];
			k=max(k,cake[i]);
		}
		cout<<"Case #"<<q<<": "<<check(cake,cp)<<endl;
		q++;
	}
	return 0;
}
