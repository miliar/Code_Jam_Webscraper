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
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase;

	
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{

		printf("Case #%d: ",case_id);
		int s;
		cin>>s;
		string sl;
		cin>>sl;
		int c=0,a=0;
		for(int i=0;i<=s;i++)
		{
			int t=sl[i]-'0';
			if(c<i)
			{
				a=a>(i-c)?a:(i-c);
			}
			c+=t;
		}
		cout<<a;
		printf("\n");
	}
	return 0;
}
