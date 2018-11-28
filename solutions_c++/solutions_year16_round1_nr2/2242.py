#pragma comment(linker,"/STACK:268435456")
#include <iostream>
#include <iomanip>
#include <fstream>
#include <set>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <climits>
#include <cstring>
#include <string>
#include <sstream>
#include <bitset>
#include <iterator>
#include <list>
#include <ctime>
#include <functional>
#include <numeric>
#include <cassert>


#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for((cont)::iterator (it)=(v).begin();(it)!=(v).end();++(it))
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define VCPRINT(v) for(int iii = 0;iii < (v).size();iii++) cout<<(v)[iii]<<" ";cout<<endl;
#define SETPRINT(v,cont) for((cont)::iterator iiit = (v).begin();iiit != (v).end();iiit++) cout<<*iiit<<" ";cout<<endl;

bool ascending (int i,int j) { return (i<j); }
bool descending (int i,int j) { return (i>j); }

typedef long long ll;
typedef unsigned long long ull;
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PULI pair<unsigned long long,int>
#define PIL pair<int,long long>
#define PSI pair<string,int>
#define PSS pair<string,string>
#define PDD pair<double,double>
#define PIB pair<int,bool>
typedef long double ld;
#define PLI pair<ll,int>
#define PBI pair<bool,int>


using namespace std;

vector<vector<int> > V;

struct lex_compare {
    bool operator ()(const vector<int> & v1,const vector<int> & v2)
	{
		for(int i = 0;i < min(v1.size(),v2.size());i++)
		{
			if(v1[i]<v2[i]) return true;
			if(v1[i]>v2[i]) return false;
		}
		return v1.size()<v2.size();
	}
};


bool cmp(const vector<int> & v1,const vector<int> & v2)
{
	for(int i = 0;i < min(v1.size(),v2.size());i++)
	{
		if(v1[i]<v2[i]) return true;
		if(v1[i]>v2[i]) return false;
	}
	return v1.size()<v2.size();
}

int C[11][11];

int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");
	//ios::sync_with_stdio(0);
	int T;cin>>T;
	FOR(_,1,T+1)
	{
		V.clear();
		cout<<"Case #"<<_<<": ";
		int n;cin>>n;
		FR(i,2*n-1)
		{
			V.push_back(vector<int>());
			FR(j,n)
			{
				int a;cin>>a;V.back().push_back(a);
			}
		}
		sort(V.begin(),V.end(),cmp);

		FR(mask,1<<(2*n-1))
		{
			CLR(C,0);
			if(__popcnt(mask)==n)
			{
				vector<int> t;
				FR(j,2*n-1)
				{
					if((1<<j) & mask)
						t.push_back(V[j][0]);
				}
				bool flag = true;
				FR(i,t.size()-1) if(t[i+1]<=t[i]){ flag = false; break;}
				if(!flag) continue;

				int curidx = 0;
				FR(j,2*n-1)
				{
					if((1<<j) & mask)
					{
						FR(i,n) C[curidx][i] = V[j][i];
						curidx++;
					}
				}
				assert(curidx==n);

				flag = true;
				FR(r,n)
				{
					if(!flag) break;
					FR(j,n-1) if(C[r][j+1]<=C[r][j]){ flag=false; break;}
				}
				if(!flag) continue;
				FR(c,n)
				{
					if(!flag) break;
					FR(j,n-1) if(C[j+1][c]<=C[j][c]){ flag=false; break;}
				}
				if(!flag) continue;

				set<vector<int>,lex_compare> cols;
				set<vector<int>,lex_compare>::iterator it;
				FR(j,2*n-1)
				{
					if(((1<<j) & mask)==0){
						vector<int> curcol;
						FR(i,n) curcol.push_back(V[j][i]);
						cols.insert(curcol);
					}
				}
				
				int MISMATCH = -1;
				FR(c,n)
				{
					vector<int> curcol;
					FR(i,n) curcol.push_back(C[i][c]);

					if((it=cols.find(curcol))!=cols.end())
						cols.erase(it);
					else{
						if(MISMATCH == -1)
							MISMATCH = c;
						else MISMATCH = INT_MAX;
					}
				}
				if(MISMATCH != INT_MAX)
				{
					FR(j,n){
						cout<<C[j][MISMATCH];
						if(j==n-1) cout<<endl;
						else cout<<" ";
					}
					break;
				}

			}
			/*else if(__popcnt(mask)==n-1)
			{
				int tmask = ~mask;
				vector<int> t;
				FR(j,2*n-1)
				{
					if((1<<j) & tmask)
						t.push_back(V[j][0]);
				}
				bool flag = true;
				FR(i,t.size()-1) if(t[i+1]<=t[i]){ flag = false; break;}
				if(!flag) continue;

				int curidx = 0;
				FR(j,2*n-1)
				{
					if((1<<j) & tmask)
					{
						FR(i,n) C[i][curidx] = V[j][i];
						curidx++;
					}
				}

				flag = true;
				FR(r,n)
				{
					if(!flag) break;
					FR(j,n-1) if(C[r][j+1]<=C[r][j]){ flag=false; break;}
				}
				if(!flag) continue;
				FR(c,n)
				{
					if(!flag) break;
					FR(j,n-1) if(C[j+1][c]<=C[j][c]){ flag=false; break;}
				}
				if(!flag) continue;

				set<int> rows;
				set<int>::iterator it;
				FR(j,2*n-1)
				{
					if(!(bool)((1<<j) & tmask))
						rows.insert(V[j][0]);
				}
				
				int MISMATCH = -1;
				FR(r,n)
				{
					if((it=rows.find(C[r][0]))!=rows.end())
						rows.erase(it);
					else{
						if(MISMATCH == -1)
							MISMATCH = r;
						else MISMATCH = INT_MAX;
					}
				}
				if(MISMATCH != INT_MAX)
				{
					FR(j,n) cout<<C[MISMATCH][j]<<" ";cout<<endl;
					break;
				}
			}*/
		}


	}
}