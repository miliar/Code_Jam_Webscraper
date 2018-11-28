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
	freopen("D-large.in","r",stdin);freopen("D-large.out","w",stdout);
	//freopen("AAA.in","r",stdin);freopen("AAA.out","w",stdout);
	int testcase;

	
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{

		printf("Case #%d: ",case_id);
		int N;
		cin>>N;
		vector<double> nao;
		vector<double> ken;
		vector<double> ken2;
		for(int i=0;i<N;i++)
		{
			double tmp;
			cin>>tmp;
			nao.push_back(tmp);
		}
		for(int i=0;i<N;i++)
		{
			double tmp;
			cin>>tmp;
			ken.push_back(tmp);
		}
		sort(nao.begin(),nao.end());
		sort(ken.begin(),ken.end());
		for(int i=0;i<N;i++)
		{
			double tmp;
			tmp=ken[i];
			ken2.push_back(tmp);
		}
		int ans1=0,ans2=0;
		for(int i=0;i<N;i++)
		{
			bool found=false;
			for(int k=0;k<N;k++)
			{				
				if(ken[k]>nao[i])
				{
					found=true;
					ken[k]=-1;
					break;
				}
			}
			if(!found)
			{
				for(int j=0;j<N;j++)
				{
					if(ken[j]>0)
					{
						ken[j]=-1;
						break;
					}
				}
				ans2++;
			}
		}
		for(int i=0,j=0;i<N&j<N;)
		{
			if(nao[i]>ken2[j])
			{
				ans1++;
				i++;j++;
			}
			else
			{
				i++;
			}
		}

		cout<<ans1<<" "<<ans2;
		printf("\n");
	}
	return 0;
}