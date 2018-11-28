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
#include <list>
#include <cassert>



using namespace std;
#pragma comment(linker, "/STACK:50000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "D-small-attempt0(2)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}



string u[55];
string u2[55];

int main()
{
	init();

	int tst;
	scanf("%d\n",&tst);

	for (int cas = 1; cas<=tst; cas++)
	{
	
		int n;
	
		scanf("%d\n",&n);

		char st[55];
		for (int i=0;i<n;i++)
		{
			gets(st);
			u2[i] = st;
		}

		int res = 1<<20;

		
		
		
		for (int i=0;i<1<<(n*n);i++)
		{

			for (int i=0;i<n;i++)
			u[i] = u2[i];

			int cur = 0;
			int p = 0;
			for (int j=0;j<n*n;j++)
				if (((1<<j)&i)!=0)
				{
					cur++;
					u[j/n][j%n]='1';				
				}	

			vi perm(n,0);
			for (int i=0;i<n;i++)
				perm[i] = i;

			int ok = 1;
			do {
				int f = 0;
				vi u3(n,0);
				for (int i=0;i<n;i++) {
					if (u[i][perm[i]]=='0') f++; else
						u3[perm[i]] = 1;
				}

				for (int i=0;i<n;i++) {
					if (u[i][perm[i]]=='0')  {
						int bad = 1;
						for (int j=0;j<n;j++) {
							if (u3[j]==0 && u[i][j]=='1') 
							{
								f--;
								u3[j]=1;
							}
						}
						//if (bad) ok = 0;
					}
						
				}


				if (f!=0)
				{
					ok = 0;
					break;
				}			

			}	 while (next_permutation(all(perm)));

			if (ok) 
				res = min(res,cur);
		}


		

		
	
		printf("Case #%d: %d\n",cas,res);
	}

	


	return 0;
}
