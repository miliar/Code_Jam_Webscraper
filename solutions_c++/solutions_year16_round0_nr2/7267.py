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
        
		int last = S.sz;
		while(S[last-1] == '+'){
			last--;
			}
		//cout<<last<<"\t";
		char t = S[0];
		int swaps = 1;
		if(last == 0 && S[last] == '+')
			swaps = 0;
		//cout<<swaps<<"\t";
		REP(i,last){
			if(S[i] != t){
				swaps++;
				t = S[i];
				}
		}
		
		cout<<"Case #"<<x<<": ";
		cout<<swaps<<endl;
		}
	return 0;
	}
	
