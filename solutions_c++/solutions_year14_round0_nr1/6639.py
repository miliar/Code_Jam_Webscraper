#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;

#define sz(X) ((int)(X.size()))
#define all(x) x.begin(),x.end()
#define clr(x,c) memset(x,c,sizeof(x))
#define up(i,s,e) for(int i=s;i<e;i++)
#define down(i,s,e) for(int i=s;i>e;i--)
#define INF 0x7FFFFFFF

int main(){
    
    #ifndef ONLINE_JUDGE
    	freopen("/Users/maoweiye/Desktop/c++/program/program/input.txt", "r", stdin);
    #endif
    int t;
    scanf("%d",&t);
    int candidate[4];
    vector<int> res;
    
    up(i,1,t+1){
        res.clear();
        int first,second;
        scanf("%d",&first);
        up(j,1,5){
            int a1,a2,a3,a4;
            scanf("%d %d %d %d",&a1,&a2,&a3,&a4);
            if(first==j){
                candidate[0]=a1;
                candidate[1]=a2;
                candidate[2]=a3;
                candidate[3]=a4;
            }
        }
        scanf("%d",&second);
        up(j,1,5){
            int a1,a2,a3,a4;
            scanf("%d %d %d %d",&a1,&a2,&a3,&a4);
            if(second==j){
                up(k,0,4){
                    if(candidate[k]==a1||candidate[k]==a2||candidate[k]==a3||candidate[k]==a4){
                        res.push_back(candidate[k]);
                    }
                }
            }
        }
        
        printf("Case #%d: ",i);
        if(res.size()){
            if(res.size()==1){
                printf("%d\n",res[0]);
            }else{
                printf("Bad magician!\n");
            }
        }else{
            printf("Volunteer cheated!\n");
        }
    }
    
    return 0;
}












