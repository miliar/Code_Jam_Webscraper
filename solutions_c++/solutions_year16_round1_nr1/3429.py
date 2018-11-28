#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>

using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define ZERO(x) memset(x,0,sizeof(x))
#define FOR(v,p,k) for(int v=p;v<k;++v)
#define FORE(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define FORC(i,c) for(__typeof(c.begin()) i=(c.begin());i!=(c).end();++i)
#define ALL(c) c.begin(),c.end()
//cout <<  __func__ << " : " << __LINE__ << endl;


int main(void)                                                                
{                                                                             
	string str;                                                           
	list <char> ans;
	int tc, cnt;                                                          
	cin >> tc;                                                            
	REP(i, tc) {                                                          
		str.clear();                                                  
		ans.clear();
		cin >> str;                                                   
		FORC(it, str) {                                               
			if (ans.size() == 0) {
				ans.push_back(*it);
				continue;
			}
			if(*it >= ans.front())
				ans.push_front(*it);
			else
				ans.push_back(*it);
		}                                                             
		cout << "Case #" << i+1 << ": ";               
		FORC(it, ans) {
			cout << *it;
		}
		cout << endl;
	}
	return 0;                                                             
}                                                                             

