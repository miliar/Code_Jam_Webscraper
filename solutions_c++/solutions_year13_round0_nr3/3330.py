#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <float.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

#define ABS(a) (a>=0?a:-(a))
#define MIN(a,b) (a<=b?a:b)
#define MAX(a,b) (a>=b?a:b)
#define rep(a,b) for(a=0;a<b;a++)
#define rep1(a,b) for(a=1;a<=b;a++)
#define rep2(a,b,c) for(a=b;a<c;a++)
#define drep(a,b) for(a=b-1;a>=0;a--)
#define drep1(a,b) for(a=b;a>=1;a--)
#define drep2(a,b,c) for(a=b;a>=c;a--)
#define foreach(vec,it) for(vector<int>::iterator it = vec.begin();it!=vec.end();it++)
#define foreach2(co,ty,it,name) for(co< ty >::iterator it = name.begin();it!=name.end();it++)

#define NMAX 1024
int A[NMAX];
void solve_problem()
{	
	double a,b,ans;
	int n, j, k;
	double i;
	char c;
	cin>>a;	
	cin>>b;	
	double s = sqrt(b);
	string st;
	ostringstream ss;
	ans=0;
	for(i=a;i<=b;i+=1.)
	{
		ss.str("");
		ss<<i;
		st = ss.str();
		int ii,jj;
//		cout<<st[st.length()-1] << "----- "<< st[0]<<endl;
		for(jj=st.length()-1,ii=0;ii<jj && st[ii]==st[jj];ii++,jj--);
		if(ii>=jj)
		{
			ss.str("");
			ss<<sqrt(i);
			st = ss.str();
			if(st.find('.')!=string::npos) continue;
			for(jj=st.length()-1,ii=0;ii<jj && st[ii]==st[jj];ii++,jj--);
			if(ii>=jj)
			{
				ans+=1.;
//				cout<<st<<endl;
			}
		}
	}
	cout<<ans<<endl;
}

int main(void)
{
	int ct, tc;
	scanf("%d",&tc);	
	for(ct=1;ct<=tc;ct++)			
	{
		//		cerr<<ct<<endl;
		printf("Case #%d: ", ct);	
		solve_problem();
	}
}
