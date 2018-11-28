#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
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
#define EPS 1e-12

int main(){
	int T;
	cin>>T;
	for(int x=1;x<=T;x++){
		string S;
		cin>>S;
		// 8, 0, 2, 4, 6, 3, 1, 5, 7, 9
		vector<int> vc(26,0);
		
		REP(i,S.sz)
			vc[S[i]-'A']++;
		
		vector<int> ans(10,0);
		
		//while(1){
				//8
				if(vc['G'-'A'] >0){
					ans[8] = vc['G'-'A'];
					vc['E'-'A'] -= ans[8];
					vc['I'-'A'] -= ans[8];
					vc['G'-'A'] -= ans[8];
					vc['H'-'A'] -= ans[8];
					vc['T'-'A'] -= ans[8];
				}
				//0
				if(vc['Z'-'A']>0){
					ans[0] = vc['Z'-'A'];
					vc['Z'-'A'] -= ans[0];
					vc['E'-'A'] -= ans[0];
					vc['R'-'A'] -= ans[0];
					vc['O'-'A'] -= ans[0];
				}
				//2
				if(vc['W'-'A']>0){
					ans[2] = vc['W'-'A'];
					vc['T'-'A'] -= ans[2];
					vc['W'-'A'] -= ans[2];
					vc['O'-'A'] -= ans[2];
				}
				//4
				if(vc['U'-'A']>0){
					ans[4] = vc['U'-'A'];
					vc['F'-'A'] -= ans[4];
					vc['O'-'A'] -= ans[4];
					vc['R'-'A'] -= ans[4];
					vc['U'-'A'] -= ans[4];
				}
				//6
				 if(vc['X'-'A']>0){
					ans[6] = vc['X'-'A'];
					vc['S'-'A'] -= ans[6];
					vc['I'-'A'] -= ans[6];
					vc['X'-'A'] -= ans[6];
				}
				//3
				 if(vc['H'-'A']>0){
					ans[3] = vc['H'-'A'];
					vc['T'-'A'] -= ans[3];
					vc['H'-'A'] -= ans[3];
					vc['R'-'A'] -= ans[3];
					vc['E'-'A'] -= ans[3];
					vc['E'-'A'] -= ans[3];
				}
				//1
				 if(vc['O'-'A']>0){
					ans[1] = vc['O'-'A'];
					vc['O'-'A'] -= ans[1];
					vc['N'-'A'] -= ans[1];
					vc['E'-'A'] -= ans[1];
				}
				//5
				 if(vc['F'-'A']>0){
					ans[5] = vc['F'-'A'];
					vc['F'-'A'] -= ans[5];
					vc['I'-'A'] -= ans[5];
					vc['V'-'A'] -= ans[5];
					vc['E'-'A'] -= ans[5];
				}
				//7
				 if(vc['V'-'A']>0){
					ans[7] = vc['V'-'A'];
					vc['S'-'A'] -= ans[7];
					vc['E'-'A'] -= ans[7];
					vc['V'-'A'] -= ans[7];
					vc['E'-'A'] -= ans[7];
					vc['N'-'A'] -= ans[7];
				}
				//9
				 if(vc['I'-'A']>0){
					ans[9] = vc['I'-'A'];
					vc['N'-'A'] -= ans[9];
					vc['I'-'A'] -= ans[9];
					vc['N'-'A'] -= ans[9];
					vc['E'-'A'] -= ans[9];
				}
			//}
		//}
		
		cout<<"Case #"<<x<<": ";
		REP(i,10){
			REP(j,ans[i])
				cout<<i;
		}
		cout<<endl;
		}
	return 0;
	}
	
