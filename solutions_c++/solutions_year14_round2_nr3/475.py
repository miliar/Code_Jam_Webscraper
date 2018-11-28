									/*ba yade oo */
//Mehrdad AP

//#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <cstring>
#include <sstream>
#include <queue>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <time.h>

using namespace std;

#define absol(x) ((x)>(0) ? (x):(-1)*(x))
#define pow2(x) ((x)*(x))
#define EPS 1e-9
#define MAX 30000
#define MOD 1000000007
#define Left(x) (2*x)
#define Right(x) ((2*(x)+1)
#define mP make_pair
#define pB push_back

//#define inRange(x,y) (x>=0 && x<N && y>=0 && y<M)

typedef long long int LL;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<int,pii> piii;

const double PI = 2.0*acos(0.0);
const int INF = 1000*1000*1000;
const int maxn=10;

#define assert(x) { cerr  << #x << ": "<< (x) << endl;}
#define SP system("pause")



bool g[maxn][maxn];

string s[maxn];
int main()
{

	int tc,TC=0;
	int N,M;
	int x,y;
	cin >> tc;
	
	while (tc--){
		cin >> N >> M;
		vector<int> perm;
		for (int i=0;i<N;i++){
			cin >> s[i];
			perm.push_back(i);
		}


		memset(g,false,sizeof g);
		for (int i=0;i<M;i++){
			cin >> x >> y;
			x--,y--;
			g[x][y]=g[y][x]=true;
		}
		
		string ans="";
		do{

			stack<int>stk;
			set<int> st;
			stk.push(perm[0]);
			st.insert(perm[0]);
			for (int i=1;i<N;i++){

				if (g[stk.top()][perm[i]]){
					stk.push(perm[i]);
					st.insert(perm[i]);
				}
				else{

					while (!stk.empty() && g[stk.top()][perm[i]]==false)
						stk.pop();
					
					if (!stk.empty()){
						stk.push(perm[i]);
						st.insert(perm[i]);
					}

				}
				if (stk.empty()) break;
			}

			if ((int)st.size()==N){
				string tmp="";
				for (int i=0;i<N;i++)
					tmp+=s[perm[i]];


				if (ans.empty() || tmp<ans)
					ans=tmp;

			}
			
		}while(next_permutation(perm.begin(),perm.end()));


		printf("Case #%d: ",++TC);
		cout << ans << endl;

	}
	
	return 0;

}