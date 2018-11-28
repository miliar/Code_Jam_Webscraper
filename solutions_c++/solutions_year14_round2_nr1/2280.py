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

vector<string> swords;




int w[100][204];

 int main()
{
	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	//freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	//freopen("A.in","r",stdin);freopen("A.out","w",stdout);
	int testcase;

	
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		memset(w,0,sizeof(int)*20400);
		printf("Case #%d: ",case_id);
		int N;
		cin>>N;
		for(int i=0;i<N;i++)
		{
			string tmp;
			cin>>tmp;
			int s=tmp[0],pos=0,c=1;
			for(int j=1;j<tmp.length();j++)
				if(tmp[j]==s) 
					c++;
				else
				{
					w[i][pos++]=s;
					w[i][pos++]=c;
					s=tmp[j];
					c=1;
				}
			w[i][pos++]=s;
			w[i][pos++]=c;
		}
		int pos=0;
		int ans=0;
		while(w[0][pos]!=0)
		{			
			int t=0;
			for(int i=0;i<N;i++)
				if(w[0][pos]!=w[i][pos])
				{
					ans=-1;
					break;
				}
				else
				{
					t+=w[i][pos+1];
				}
			if(ans==-1) break;
			int m=t/N;
			for(int i=0;i<N;i++)
				ans=ans+abs(w[i][pos+1]-m);
			pos+=2;
		}
		for(int i=0;i<N;i++)
			if(w[i][pos]!=0) ans=-1;
		if(ans==-1) 
			cout<<"Fegla Won";
		else
			cout<<ans;
		

		
		
		printf("\n");
	}
	return 0;
}