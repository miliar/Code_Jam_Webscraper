#include<iostream>
#include<cstdio>
#include<cstdlib>
#include <string.h>
#include<string>
#include<vector>
#include<set>
#include<list>
#include<algorithm>
using namespace std;
typedef long long ll;

char ff(char a, char b, bool si, bool *so);
char A[100005];
int main()
{
	freopen("in_C.txt", "r", stdin);
	freopen("out_C.txt", "w", stdout);
	ll T, L,X;
	scanf("%lld", &T);
	for (ll TC = 1; TC <= T; ++TC)
	{
		
		scanf("%lld %lld", &L, &X);
		scanf("%s", A);
		bool ii = false, jj = false, kk = false;
		char ic = '1';
		bool sigi = false,sigo=false;
		for (ll i = 0; i < L*X; ++i)
		{
			ll tt = i%L;
			char rt = ff(ic, A[tt], sigi, &sigo);
			if ((!ii) && (rt == 'i'))
			{
				ii = true;
				sigi = sigo;
				ic = '1';
			}
			else if ((ii)&&(!jj) && (rt == 'j'))
			{
				jj = true;
				sigi = sigo;
				ic = '1';
			}
			else if ((ii) && (jj) && (rt == 'k') && (i == (L*X - 1)))
			{
				if(!sigo)
				kk = true;
				
			}
			else
			{
				ic = rt;
				sigi = sigo;
			}

		}
		if (ii&jj&kk)
			printf("Case #%d: YES\n", TC);
		else
			printf("Case #%d: NO\n", TC);

	}
	return 0;
}


char ff(char a, char b, bool si, bool *so)
{
	char ret = '1';
	bool ss = false;
	if (a == 'i')
	{
		if (b == 'i')
		{
			ret = '1';
			ss = (!si);
		}
		else if (b == 'j')
		{
			ret = 'k';
			ss = si;
		}
		else if (b == 'k')
		{
			ret = 'j';
			ss = (!si);
		}
		else if (b == '1')
		{
			ret = 'i';
			ss = si;
		}
		else
		{
		}
	}
	else if (a == 'j')
	{
		if (b == 'i')
		{
			ret = 'k';
			ss = (!si);
		}
		else if (b == 'j')
		{
			ret = '1';
			ss = (!si);
		}
		else if (b == 'k')
		{
			ret = 'i';
			ss = si;
		}
		else if (b == '1')
		{
			ret = 'j';
			ss = si;
		}
		else
		{
		}
	}
	else if (a == 'k')
	{
		if (b == 'i')
		{
			ret = 'j';
			ss = si;
		}
		else if (b == 'j')
		{
			ret = 'i';
			ss = (!si);
		}
		else if (b == 'k')
		{
			ret = '1';
			ss = (!si);
		}
		else if (b == '1')
		{
			ret = 'k';
			ss = si;
		}
		else
		{
		}
	}
	else if (a == '1')
	{
		if (b == 'i')
		{
			ret = 'i';
			ss = si;
		}
		else if (b == 'j')
		{
			ret = 'j';
			ss = si;
		}
		else if (b == 'k')
		{
			ret = 'k';
			ss = si;
		}
		else if (b == '1')
		{
			ret = '1';
			ss = si;
		}
		else
		{
		}
	}

	*so = ss;
	return ret;
}
