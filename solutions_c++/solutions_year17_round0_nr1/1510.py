#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<set>
#include<map>
#include<vector>
#include<utility>
#include<queue>
#include<stack>
#include<string>


#define ri(X) scanf("%d",&X)
#define rii(X,Y) scanf("%d %d",&X,&Y)
#define rf(X) scanf("%lf",&X)
#define rff(X,Y) scanf("%lf %lf",&X,&Y)
#define mp(X,Y) make_pair(X,Y)
#define pii pair<int,int>
#define FOR(i,j) for(int i=0;i<j;i++)
#define FORC(i,j,c) for(int i=0;i<j;i+=c)

using namespace std;
int T;
string s;
int K;
const int mn = 1e3+10;
int use[mn];
int main(){
    cin >> T;
    
    FOR(i, T){
        cout << "Case #" << i+1 <<": ";
        cin >> s >> K;   
        int tmp = 0;
        int flips = 0;
        int ready = 0;
        memset(use, 0, sizeof use);
        FOR(i,s.size()){
          tmp += use[i];
          int face = s[i]=='+';
          face += tmp; face%=2;
          if(!face && i<s.size()-K+1) {
            use[i+K] = -1;
            tmp++; flips++;
            s[i]= '+';
          } else if(!face){
            cout <<"IMPOSSIBLE" << endl;
            ready = 1;
            break;
          }
        }
        if(!ready) cout << flips << endl;
    }

	return 0;
}
