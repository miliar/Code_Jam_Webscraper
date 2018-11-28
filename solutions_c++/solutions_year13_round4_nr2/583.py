#include <iostream>
#include <string>
#include <string.h>
#include <math.h>
#include <time.h>
#include <stdio.h>
#include <utility>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <list>

#define FORST(X,S,T) for(int X=S; X<=T; X++)  
#define RFORST(X,S,T) for(int X=S; X>=T; X--)  
#define FOR(X,XB) for(int X=0; X<XB; X++)
#define RFOR(X,XB) for(int X=(XB)-1; X>=0; X--)
#define FORSTL(X,C) for(X=C.begin();X!=C.end();X++)
#define SQR(X) ((X)*(X))
#define MID(X,Y) (((X)+(Y))/2)
#define FILL(X,V) memset(X,V,sizeof(X))
#define FILE_R(X) freopen(X, "r", stdin)  
#define FILE_W(X) freopen(X, "w", stdout)  
#define ERREQ(X,Y) (fabs((X)-(Y))<EPS)
#define MIN(X,Y) ((X)<(Y)?(X):(Y))
#define MAX(X,Y) ((X)>(Y)?(X):(Y))
#define INITLISTS {L=0; FILL(adj,-1);}
#define DBGL cout << "here" << endl;
#define SZ(X) sizeof(X)
const double PI = acos(-1.0);
const double EPS = 1E-9;
const int INF = (int)1E9;
typedef long long LINT;
using namespace std;

#define MAXN 100
LINT N, P;

int main(){
	int cs;

	FILE_W("output");

	cin>>cs;

	for(int csn=1;csn<=cs;csn++){
		printf("Case #%d: ", csn);
		cin >> N >> P;
		P--;
		int L = 0;
		int b[MAXN];
		FILL(b, 0);
		while(P){
			b[L++] = P%2;
			P/=2;
		}

		LINT any = 1;
		RFOR(i, N){
			LINT j = N-i;
			if(b[i]==0){
				any--;
				break;
			}else{
				any += ((1LL)<<j);
			}
		}
		any = MIN(any, ((1LL)<<N)-1);
		LINT all = 0;
		LINT j = 0;
		RFOR(i, N){
			if(b[i]==0){
				all += ((1LL)<<j);
				j++;
			}else{
				LINT cnt = 0;
				RFOR(t, i){
					if(b[t]==0){
						cnt++;
					}
				}
				if(cnt>=1){
					all += ((1LL)<<j);
				}
				break;
			}
		}
		
		cout << any << " " << ((1LL)<<N)-all-1 << endl;



	}
	return 0;
}