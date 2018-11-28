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


 int main()
{
	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	int testcase;

	
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{

		printf("Case #%d: ",case_id);
		double C,F,X;
		int N;
		cin>>C>>F>>X;
		double tmp=X*F-C*F-2*C;
		tmp=tmp/(C*F);
		if(tmp<0) tmp=0;
		N=(int)ceil(tmp);
		if(N<0) N=0;
		double ans=0;
		for(int i=0;i<N;i++)
			ans+=(C*1.0)/(i*F+2);
		ans+=(X*1.0)/(N*F+2);
		printf("%.7f",ans);
		printf("\n");
	}
	return 0;
}