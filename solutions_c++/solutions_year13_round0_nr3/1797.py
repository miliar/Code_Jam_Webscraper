#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<fstream>
#include<sstream>
using namespace std;
int no[10000001],ren=0;
bool palin(long long x)
{
	string s;
	stringstream ss;
    ss << x;
    s=ss.str();
    int l=s.length(),m;
    m=(l/2)+(l%2);
	for(int i=0;i<m;i++)
		if(s[i]!=s[l-1-i])
			return false;
	return true;
}
void prep()
{
	long long x;
	no[0]=0;
	for(int i=1;i<10000001;i++)
	{
		no[i]=ren;
		if(palin((long long)(i)))
		{
			x=pow((long long)(i),2);
			if(palin(x))
			{
				no[i]+=1;
				ren=no[i];
			}
		}
	}
}
int main()
{
	prep();
	int t;
	long long a,b,c,d;
	ifstream rf("input.txt");
	ofstream wf("result.txt");
	rf>>t;
//	scanf("%d",&t);
	for(int z=1;z<=t;z++)
	{
		rf>>a>>b;
//		scanf("%lld%lld",&a,&b);
		c=ceil(sqrt(double(a)));
		d=floor(sqrt(double(b)));
		wf<<"Case #"<<z<<": "<<no[d]-no[c-1]<<"\n";
//		printf("Case #%d: %d\n",z,no[d]-no[c-1]);
	}
	return 0;
}
