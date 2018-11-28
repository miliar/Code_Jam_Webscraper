#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctype.h>
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
#include <sstream>
using namespace std;
#define ot(x) cout<<x<<endl
#define cen cout<<endl
#define EPS 1e-10
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
vector<vii> AdjList;
priority_queue< pair<int, ii> > Edgelist;
int n,m,i,t,j,k,l;
int a[26];

int main(){
    cin>>t;
    for(i=0;i<t;i++){
        cin>>n;
        memset(a,0,sizeof a);
        for(j=0;j<4;j++){
            for(k=0;k<4;k++){
                scanf("%d",&l);
                a[l]=j;
            }
        }
        cin>>m;
        int ans=0,cans=0;
        for(j=0;j<4;j++){
            for(k=0;k<4;k++){
                scanf("%d",&l);
                if(j==m-1){
                    if(a[l]==n-1){
                       cans++;
                       ans=l;
                    }
                }
            }
        }
        if(cans==0){
            printf("Case #%d: Volunteer cheated!\n",i+1);
        }else if(cans>1){
            printf("Case #%d: Bad magician!\n",i+1);
        }else{
            printf("Case #%d: %d\n",i+1,ans);
        }
    }
    return 0;
}

/*
5
1 0 -1 0 0
0 1 0 -1 -2
*/
