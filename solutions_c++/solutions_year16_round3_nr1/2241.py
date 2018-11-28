#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long ll;

#define SZ(x) (int)(x.size())
#define F0(k,n) for(int k=0;k<n;k++)
#define F1(k,n) for(int k=1;k<=n;k++)

ll gcd(ll x, ll y) { return (y ? gcd(y, x%y) : x); }

int main() 
{

	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int tt, tn, n,i,tsum; 
	int m1,m2;
	bool chk;
	cin >> tn;
	
	F1(tt,tn) 
	{
		cin>>n;
		int *p=new int[n];
		tsum=0;
		F0(i,n)
		{	
			cin>>p[i];
			tsum+=p[i];
		}
		
		cout<<"Case #"<<tt<<": ";
		chk=false;		
		while(tsum!=0)
		{
			m1=0;
			F0(i,n)
			{
				if(p[i]>p[m1])
					m1=i;
			}
			if(m1>0)
				m2=m1-1;
			else
				m2=1;
			F0(i,n)
			{
				if(p[i]>=p[m2] && i!=m1)
					m2=i;
			}
			if(tsum>1 && ((p[m1]>1 || p[m2]>1) || tsum==2))
			{
				if(chk==false)
				{
				chk=true;					
					cout<<(char)(65+m1)<<(char)(65+m2);
				}
				else
					cout<<" "<<(char)(65+m1)<<(char)(65+m2);
				p[m1]--;
				p[m2]--;
				tsum-=2;
			}
			else
			{
				if(chk==false)
				{
					chk=true;
					cout<<(char)(65+m1);
				}
				else
					cout<<" "<<(char)(65+m1);
				p[m1]--;
				tsum--;
			}
		}	
		delete []p;
		cout<<endl;
	}
	return 0;
}
