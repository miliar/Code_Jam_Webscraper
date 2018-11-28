/*
Problem :A magic trick
contest : Google code jam
author :saurabh jain
date :12/4/2014
*/

#include<iostream>
#include<stdio.h>
#include<string.h>
#include<iterator>
#include<stdlib.h>
#include<map>
#include<vector>
#include<algorithm>
#define MOD 1000000007
#define max(x,y)((x>y)?x:y)
#define min(x,y)((x<y)>x:y)
#define FEP(i,a,b) for(int i=a;i<b;i++)
#define PI 3.14
using namespace std;
unsigned long long mod_pow(unsigned long long num, unsigned long long pow, unsigned long long mod)
{
    unsigned long long test;
    unsigned long long n = num;
    for(test = 1; pow; pow >>= 1)
    {
        if (pow & 1)
            test = ((test % mod) * (n % mod)) % mod;
        n = ((n % mod) * (n % mod)) % mod;
    }
    return test; /* note this is potentially lossy */
}
int main(int argc, char* argv[])
{	int t;
	scanf("%d",&t);
	int mat1[5][5],mat2[5][5];
	int ans1,ans2;
	for(int k=1;k<=t;k++)
	{
		scanf("%d",&ans1);
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
				scanf("%d",&mat1[i][j]);
		}
		scanf("%d",&ans2);
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
				scanf("%d",&mat2[i][j]);
		}
		//cout<<"check1"<<endl;
		map<int,int> mp;
		for(int i=1;i<=4;i++)
		{
			mp[mat1[ans1][i]]++;
		}		
		int match=0;
		int ans=-1;
		for(int i=1;i<=4;i++)
		{
			if(mp[mat2[ans2][i]])
			{	
				match++;
				ans=mat2[ans2][i];
			}	
		}
		
		mp.clear();
		//cout<<ans<<" "<<match<<endl;
		if(match==0)
		{	//cout<<"1"<<endl;
			printf("Case #%d: Volunteer cheated!\n",k);
		}
		else if(match==1)
		{	//cout<<"2"<<endl;	
			printf("Case #%d: %d\n",k,ans);
		}
		else
		{	//cout<<"3"<<endl;
			printf("Case #%d: Bad magician!\n",k);
		
		}
		//cout<<"end"<<endl;
	}	
}
