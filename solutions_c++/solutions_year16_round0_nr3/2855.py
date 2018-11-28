/*************************************************************************
	> File Name: pC2.cpp
	> Author: fuyu0425/a0919610611
	> School: National Chiao Tung University
	> Team: NCTU_Ragnorok
	> Mail: a0919610611@gmail.com
	> Created Time: 西元2016年04月09日 (週六) 18時05分48秒
 ************************************************************************/
#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
bool isprime[20000000]={};
vector<int> prime;
LL pow(LL a,LL b)
{
	LL ans=1;
	LL base=a;
	while(b)
	{
		if(b&1) ans*=base;
		base*=base;
		b>>=1;
	}
	return ans;
}
int n;
LL cal(vector<LL> &a ,int base)
{
	LL ans=0;
	for(int i=n-1;i>=0;i--)
	{	
		ans*=base;
		ans+=a[i];
	}
	//cout<<"ans="<<ans<<endl;
	return ans;
	
}
LL fac(LL x)
{
	for(int i=0;i<prime.size() && x>prime[i];i++)
	{
		if(x%prime[i]==0) return prime[i];
	}
	return 0;
}
int main()
{
	    for (int i=2; i<20000000; i++)
 
		{
			if (!isprime[i]) prime.push_back(i);
		        for (int j=0; i*prime[j]<20000000; j++)
				{		
//					cout<<i*prime[j]<<endl;
					isprime[i*prime[j]] = true;
				  if (i % prime[j] == 0) break;
				}							    
		}
		//cout<<"hi"<<endl;
		int T;
		cin>>T;
		cout<<"Case #1:"<<endl;
		int j;
		cin>>n>>j;
		//cout<<"ya";
		vector<LL>a(33);
		a[0]=1;a[n-1]=1;
		int k;
		vector<vector<LL> > str;
		vector<vector<LL> > ans;
		int i;
		//cout<<"mypow"<<pow(2,n-2)<<endl;
		for(i=0;i<pow(2,n-2);i++)
		{	
			//cout<<i<<endl;
			int index=1;
			int now=i;
			for(k=1;k<=n-2;k++)
			{
				a[k]=now%2;
				now/=2;
			}
			vector<LL>tmp;
			for(k=2;k<=10;k++)
			{
				LL num=cal(a,k);
				LL t=fac(num);
				//cout<<"t="<<t<<endl;
				if(t!=0) tmp.push_back(t);
				else break;

			}
			//cout<<tmp.size();
			//cout<<ans.size();
			if(tmp.size()==9){str.push_back(a);ans.push_back(tmp);}
			if(ans.size()==j)break;
		}

		for(i=0;i<j;i++)
		{
			for(k=n-1;k>=0;k--) cout<<str[i][k];
			cout<<" ";
			for(k=0;k<9;k++)
			{
				if(k)cout<<" ";
				cout<<ans[i][k];
			}
			cout<<endl;
		}

     return 0;
}
