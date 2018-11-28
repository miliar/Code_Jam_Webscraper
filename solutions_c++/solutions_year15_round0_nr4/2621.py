#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <deque>
using namespace std;

#define ot(x) cout<<x<<endl
#define cen cout<<endl
#define EPS 1e-10
#define mp(x,y) make_pair(x,y)
#define DFS_GRAY 2
#define DFS_WHITE -1
#define DFS_BLACK 1
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
vector<vii> AdjList;
priority_queue< pair<int, ii> > Edgelist;
int n,t,j,k,i,m,l;
string s,z;
int x[10];

void A(){ printf("GABRIEL\n");}
void B(){ printf("RICHARD\n");}

int main(){
    int tc,itc=1;
    cin>>tc;
    while(tc--){
        scanf("%d%d%d",&t,&n,&m);
        if(n>m)swap(n,m);
        printf("Case #%d: ",itc++);
        if(t==1){
            A();
        }else if(t==2){
            if((n*m)%t==0)A();
            else B();
        }else if(t==3){
            if((n*m)%t==0 && n>1)A();
            else B();
        }else if(t==4){
            if((n*m)%t==0 && n>2)A();
            else B();
        }
    }
}
/*
3
1 1 1 4 5 6
1 2 3 4 5 6
2 1 1 1 5 6
3 5 6 4 2 1
*/
