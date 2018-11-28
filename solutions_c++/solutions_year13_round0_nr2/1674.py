#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>

using namespace std;

#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define mkp make_pair
typedef long long ll;

int main(){
	int T;
	cin>>T;
	REP(x,T){
		int N,M;
		cin>>N>>M;
		int lawn[N][M];
		int dest[N][M];
		REP(i,N){
			REP(j,M){
				dest[i][j] = 100;
				cin>>lawn[i][j];
				}
			}
		//mow rows
		REP(i,N){
			int rowmax = -1;
			REP(j,M){
				if(lawn[i][j] > rowmax) rowmax = lawn[i][j];
				}
			REP(j,M){
				if(dest[i][j] > rowmax) dest[i][j] = rowmax;
				//cout<<dest[i][j]<<" ";
				}
			//cout<<endl;
			}
		//mow columns
		REP(i,M){
			int colmax = -1;
			REP(j,N){
				if(lawn[j][i] > colmax) colmax = lawn[j][i];
				}
			REP(j,N){
				if(dest[j][i] > colmax) dest[j][i] = colmax;
				//cout<<dest[j][i]<<" ";
				}
			//cout<<endl;
			}
		bool poss = true;
		REP(i,N){
			REP(j,M){
				if(lawn[i][j] != dest[i][j]){
					poss = false;
					break;
					}
				}
			if(!poss) break;
			}
		if(poss)
			cout<<"Case #"<<x+1<<": "<<"YES"<<endl;
		else
			cout<<"Case #"<<x+1<<": "<<"NO"<<endl;
		}
	return 0;
	}