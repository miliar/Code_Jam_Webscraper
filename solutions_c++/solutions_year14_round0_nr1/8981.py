#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <malloc.h>
#include <sstream>
#include <iostream>
#include <cstdlib>
#include <stdint.h>
#include <unistd.h>
#include <ctime>
#include <climits>
using namespace std;
#define EPS 		1e-8
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define F(i,a)      FOR(i,0,a)
#define PB          push_back
#define S           size()
#define MP          make_pair
#define ALL(v)      v.begin(),v.end()
#define LLA(v)      v.rbegin(),v.rend()
#define X           first
#define Y           second
#define NL 			printf("\n")
#define SP 			system("pause")
#define foreach(IT,C) for(typeof(C.begin())IT=C.begin();IT!=C.end();IT++)
const double PI = acos(-1.0);
int in(){int r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<string> vstr;
typedef long long   LL;

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int carts[4][4],t,c1,c2,carts2[4][4],cont,carta;
    cin>>t;
    F(cp,t){
        bool numero[20] = {0};
        cont=0;
        cin>>c1;
        F(i,4){
            F(j,4){
                cin>>carts[i][j];
            }
            if(i==c1-1){
                F(j,4){
                    numero[carts[i][j]]=1;
                }
            }
        }
        //F(i,16) cout<<numero[i]<<" "; NL;
        cin>>c2;
        F(i,4){
            F(j,4){
                cin>>carts2[i][j];
            }
            if(i==c2-1){
                F(j,4){
                    if(numero[carts2[i][j]]==1) {
                        carta=carts2[i][j];
                        //cout<<carta;NL;
                        cont++;
                    }
                }
            }
        }
        if(cont==1) cout<<"Case #"<<cp+1<<": "<<carta<<endl;
        else if(cont==0) cout<<"Case #"<<cp+1<<": Volunteer cheated!"<<endl;
        else cout<<"Case #"<<cp+1<<": Bad magician!"<<endl;
    }
    return 0;
}
