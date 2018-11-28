#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long ll;

int GetGN(ll p,ll q,int g)
{
	if(g>40) return 9999;	
	if(p==q) return 0;
	p=p*2;
	if(p<=q) 
		return 1+GetGN(p,q,g+1);
	else
	{
		int tmp=GetGN(p-q,q,g+1);
		if(tmp<5000)
			return 1;
		else
			return tmp;
	}
}


 int main()
{
	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	//freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	//freopen("A.in","r",stdin);freopen("A.out","w",stdout);
	int testcase;

	
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{

		printf("Case #%d: ",case_id);
		ll P=0,Q=0;
		string a;
		cin>>a;
		bool f=false;
		for(int i=0;i<a.length();i++)
		{
			if(a[i]=='/'){ f=true;continue;}
			if(!f)
			{
				P=P*10+a[i]-'0';
			}
			else
			{
				Q=Q*10+a[i]-'0';
			}
		}
		int ans=GetGN(P,Q,0);
		if(ans>5000)
			cout<<"impossible";
		else
			cout<<ans;
	

		printf("\n");
	}
	return 0;
}