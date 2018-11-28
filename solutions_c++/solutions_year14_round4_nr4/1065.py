#include<stdio.h>
#include<map>
#include<string.h>
#include<iostream>
#include<vector>
#include<set>
#define mod 1000000007

long long pot(long long a, long long b)
{
    long long res =1;
    for (int i=0;i<b;i++)
    {
	res*=a;
	res%=mod;
    }
    return res;
}


using namespace std;
int main()
{
    int zes;scanf("%d",&zes);
    for (int z = 0;z<zes;z++)
    {
	map<string,int> tab;
	char buf[20];
	int n,m;
	scanf("%d%d\n",&n,&m);
	map<int, vector<string> > prefixes;
	for (int i =0;i<n;i++)
	{
	    gets(buf);
	    string s=  buf;
	    for (int len=1;len<=s.size();len++)
	    {
		tab[s.substr(0,len)]++;
		prefixes[i].push_back(s.substr(0,len));
	    }
	}
	int res = min(n,m);
	long long res2=0;
	for (map<string,int>::iterator it  = tab.begin();it!=tab.end();it++)
	{
	    if(it->second > m) 
	    { 
		res+=m; 
	    }
	    else 
	    {
		res += it->second;
	    }
	}
	int ile = pot (m,n);
	for (int i =0;i<ile;i++)
	{

            int buf[10]={};int k=0;
	    int tmp = i;
	    do
	    {
		int x = tmp%m;
		buf[k++] = x;
	    }while(tmp/=m);
	    for (int i =0;i<n;i++)
	    {

	    }
	    map<int, set<string> > t;
	    bool byl[20]={};
	    for (int k =0;k<n;k++)
	    {
		byl[buf[k]]= true;
		for (int j=0;j<prefixes[k].size();j++)
		    t[buf[k]].insert(prefixes[k][j]);
	    }
	    int sum=0;
	    for (int k =0;k<m;k++)
		sum += t[k].size()+ byl[k];
	    if(sum == res)
		res2++;
	    res2%=mod;
	}

	printf("Case #%d: %d %lld\n",z+1, res,res2);

    }

}
