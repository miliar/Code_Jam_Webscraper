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
 int getmins(vector<int> p);

 int main()
{
	freopen("B-Small-Attempt3.in","r",stdin);freopen("B-Small-Attempt3.out","w",stdout);
	int testcase;

	
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		vector<int> p;
		printf("Case #%d: ",case_id);
		int d;
		cin>>d;
		int t;
		for(int i=0;i<d;i++)
		{
			cin>>t;
			p.push_back(t);
		}
		sort(p.begin(),p.end());
		/*int a=p[p.size()-1];
		for(int i=1;i<=54;i++)
		{
			int curmax=p[p.size()-1];
			int t1=curmax/2;



			p[p.size()-1]=curmax-t1;
			p.push_back(t1);
			sort(p.begin(),p.end());
			int curmins=i+p[p.size()-1];
			if(curmins<a)
				a=curmins;
		}*/
		int a=getmins(p);
		cout<<a;
		printf("\n");
	}
	return 0;
}

 int getmins(vector<int> p)
 {
	 sort(p.begin(),p.end());
	 int max=p[p.size()-1];
	 if(max<=3)
		 return max;
	 int a=max;
	 for(int i=2;i<=max/2;i++)
	 {
		 vector<int> t;
		 for(int i=0;i<p.size()-1;i++)
			 t.push_back(p[i]);
		 t.push_back(i);
		 t.push_back(max-i);
		 int ci=getmins(t)+1;
		 a=a>ci?ci:a;
	 }
	 return a;
 }