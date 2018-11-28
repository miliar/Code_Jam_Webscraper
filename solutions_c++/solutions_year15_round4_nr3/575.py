#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <string.h>

using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "C-small-attempt0";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}


map <string, int > mp;
int val[100100],val2[100100];
int col = 0;
char st[100100];
vector <int> mas[212];
int main()
	
{
   init();


	int tst;
//	scanf("%d",&tst);
	scanf("%d\n",&tst);


	for (int cas = 1; cas<=tst;cas++)
	{
		int res = 0; 
		col = 0;
		mp.clear();
		memset(val,0,sizeof(val));
		memset(val2,0,sizeof(val2));
		int n;
		scanf("%d\n",&n);

		for (int i=0;i<n;i++)
			mas[i].clear();


		memset(val,0,sizeof(val));

		for (int i=0;i<n;i++) {
			gets(st);
			istringstream ss(st);
			string s;
			while (ss>>s)
			{
				if (mp[s]==0)
				{
					col++;
					mp[s] = col;
				}
				mas[i].push_back(mp[s]);
				if (i==0) val[mp[s]]|=1;
				if (i==1) val[mp[s]]|=2;
			}
		}

		n-=2;
		
		int mn=1<<29;
		for (int i=0;i<=col;i++)
			if (val[i]==3) res++;

		for (int i=0;i<1<<n;i++)
		{
			//memset(val,0,col*4+4);
			int cur = 0;
			memset(val2,0,col*4+4);
			for (int j=0;j<n;j++)
			{
				int add = 0;
				if ((1<<j)&i) add=1; else add=2;
				for (int k=0;k<sz(mas[j+2]);k++)
					val2[mas[j+2][k]]|=add;						
			}	

			

			for (int j=0;j<=col;j++)
				if ((val[j]|val2[j])==3) cur++;
			mn = min(mn,cur);

		}
		
		



		//if (!f) printf("Case #%d: IMPOSSIBLE\n",cas);	 else
		printf("Case #%d: %d\n",cas,mn);	

	}
	



	

	
   
	

   

	
  return 0;
}

