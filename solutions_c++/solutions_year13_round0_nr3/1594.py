#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<math.h>
#include<sstream>

using namespace std;

int d1[50];
int d2[100];

string ech(long mask)
{
	int i=0,j,m=(int)(log2(mask))+1;
	for(i=m;i<2*m;i++)
	{
		d1[i]=d1[2*m-1-i]=mask%2;
		mask/=2;
	}
	//for(i=0;i<2*m;i++) cout<<d1[i];
	//cout<<endl;
	for(i=0;i<100;i++) d2[i]=0;
	for(i=0;i<2*m;i++)
	{
		if(d1[i]==0) continue;
		for(j=0;j<2*m;j++)
			d2[i+j]+=d1[j];
		if(d2[i]>9) return "0";
	}
	//for(i=0;i<=4*m-2;i++) cout<<d2[i];
	//cout<<endl;
	stringstream o;
	for(i=4*m-2;i>=0;i--)
	{
		o<<d2[i];
		if(d2[4*m-2-i]!=d2[i]) return "0";
	}
	return o.str();

}
string och(long mask)
{
	int i=0,j,m=(int)(log2(mask))+1;
	for(i=m-1;i<2*m-1;i++)
	{
		d1[i]=d1[2*m-2-i]=mask%2;
		mask/=2;
	}
	//for(i=0;i<2*m;i++) cout<<d1[i];
	//cout<<endl;
	for(i=0;i<100;i++) d2[i]=0;
	for(i=0;i<2*m-1;i++)
	{
		if(d1[i]==0) continue;
		for(j=0;j<2*m-1;j++)
			d2[i+j]+=d1[j];
		if(d2[i]>9) return "0";
	}
	//for(i=0;i<=4*m-2;i++) cout<<d2[i];
	//cout<<endl;
	stringstream o;
	for(i=4*m-4;i>=0;i--)
	{
		o<<d2[i];
		if(d2[4*m-4-i]!=d2[i]) return "0";
	}
	return o.str();
}
string tch(long mask)
{
	int i=0,j,m=(int)(log2(mask))+1;
	for(i=m-1;i<2*m-1;i++)
	{
		d1[i]=d1[2*m-2-i]=mask%2;
		mask/=2;
	}
	d1[m-1]=2;
	for(i=0;i<100;i++) d2[i]=0;
	for(i=0;i<2*m-1;i++)
	{
		if(d1[i]==0) continue;
		else if(d1[i]==2)
		{
			for(j=0;j<2*m-1;j++)
				d2[i+j]+=2*d1[j];
			if(d2[i]>9) return "0";
			continue;
		}
		for(j=0;j<2*m-1;j++)
			d2[i+j]+=d1[j];
		if(d2[i]>9) return "0";
	}
	//for(i=0;i<=4*m-4;i++) cout<<d2[i];
	//cout<<endl;
	stringstream o;
	for(i=4*m-4;i>=0;i--)
	{
		o<<d2[i];
		if(d2[4*m-4-i]!=d2[i]) return "0";
	}
	return o.str();
}
int main()
{
	vector<string> P;
	P.push_back("1");
	P.push_back("4");
	P.push_back("9");
	P.push_back("121");
	long M=pow(2,14)-1;
	string r;
	int i,j;
	for(long k=2;k<=M;k++)
	{
		r=och(k);
		if(r!="0")
		{
			P.push_back(r);
			r=ech(k);
			if(r!="0")
			{
				P.push_back(r);
				if(k%2==0)
				{
					r=tch(k);
					if(r!="0") P.push_back(r);
				}
			}
		}
		//if och=0, ech=0
		//if och=0, tch=0
		//if ech=0, tch=0
	}
	string x;
	for(i=0;2*(i+2)-1<=100;i++)
	{
		stringstream o;
		o<<4;
		for(j=0;j<i;j++) o<<0;
		o<<8;
		for(j=0;j<i;j++) o<<0;
		o<<4;
		x=o.str();
		P.push_back(x);
		o.str(std::string());
		if(i%2==1)
		{
			o<<4;
			for(j=0;j<(i-1)/2;j++) o<<0;
			o<<4;
			for(j=0;j<(i-1)/2;j++) o<<0;
			o<<9;
			for(j=0;j<(i-1)/2;j++) o<<0;
			o<<4;
			for(j=0;j<(i-1)/2;j++) o<<0;
			o<<4;
			x=o.str();
			P.push_back(x);
		}
	}
	for(i=0;i<P.size();i++)
	{
		stringstream o;
		for(j=0;j<(100-P[i].length());j++) o<<0;
		x=o.str();
		P[i]=x+P[i];
	}
	sort(P.begin(),P.end());
	int T,a,b;
	string A,B;
	//for(i=0;i<P.size();i++) cout<<P[i]<<endl;
	scanf("%d",&T);
	for(int c=1;c<=T;c++)
	{
		cin>>A;
		cin>>B;
		stringstream o;
		for(j=0;j<(100-A.length());j++) o<<0;
		x=o.str();
		A=x+A;
		o.str(std::string());
		for(j=0;j<(100-B.length());j++) o<<0;
		x=o.str();
		B=x+B;
		a=(lower_bound(P.begin(),P.end(),A)-P.begin());
		b=(upper_bound(P.begin(),P.end(),B)-P.begin());
		printf("Case #%d: %d\n",c,b-a);
	}
	return 0;
}
