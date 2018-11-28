#include <algorithm>
#include <numeric>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <stack>
using namespace std;

int main()
{
	freopen("in.in","rt",stdin);
	freopen("out.out","wt",stdout);
	int T;
	cin>>T;
	for (int i=0;i<T;i++)
	{
		long long n,P,A,B,p2=1;
		cin>>n>>P;
		long long N=1ll<<n, m=N-1;
		for (int i=0;i<=n;i++)
		{
			long long ii=N-p2;
			if (m<P)
			{
				B=ii;
				break;
			}
			m/=2;
			p2*=2;
		}
		p2=1;
		m=0;
		long long pl=1ll<<(n-1);
		for (int i=0;i<=n;i++)
		{
			long long iin=min(N-1,(p2-1)*2);
			if (m<P)
				A=iin;
			m=m|pl;
			pl/=2;
			p2*=2;
		}
		printf("Case #%d: ",i+1);
		cout<<A<<" "<<B<<endl;
	}
	return 0;
}
