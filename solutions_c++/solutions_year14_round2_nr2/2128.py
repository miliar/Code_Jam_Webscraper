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
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	//freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
	int testcase;

	
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{

		printf("Case #%d: ",case_id);
		int A,B,K,ans=0;
		cin>>A>>B>>K;
		for(int i=0;i<A;i++)
			for(int j=0;j<B;j++)
				if((i&j)<K) ans++;
		
		cout<<ans;
		printf("\n");
	}
	return 0;
}