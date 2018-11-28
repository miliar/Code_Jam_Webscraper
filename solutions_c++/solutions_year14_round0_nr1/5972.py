#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long LL;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

#define foru(i,a,b) for(int i=int(a);i<int(b);i++)
#define forui(i,a,b,c) for(int i=int(a);i<int(b);i+=c)
#define ford(i,a,b) for(int i=int(a);i>=b;i--)

#define pb push_back
#define mp make_pair
#define f first
#define s second

#define ms(v,x) memset(v,x,sizeof v)
#define fr freopen("A-small-attempt0.in","r",stdin)

int main()
{
    fr;
    freopen("A-small-attempt0.out","w",stdout);
    int n,fila,a;
    while(scanf("%d",&n)==1){
        foru(cases,1,n+1){
            scanf("%d",&fila);
            int v1[10];
            int v2[10];
            foru(i,1,5){
                foru(j,1,5){
                    scanf("%d",&a);
                    if(i==fila){
                        v1[j]=a;
                    }
                }
            }
            scanf("%d",&fila);
            foru(i,1,5){
                foru(j,1,5){
                    scanf("%d",&a);
                    if(i==fila){
                        v2[j]=a;
                    }
                }
            }
            int count=0,val;
            foru(i,1,5){
                foru(j,1,5){
                    if(v1[i]==v2[j]){
                        count++;
                        val = v1[i];
                    }
                }
            }
            printf("Case #%d: ",cases);
            if(count==1)printf("%d\n",val);
            else if(count>1)printf("Bad magician!\n");
            else printf("Volunteer cheated!\n");
        }
    }
    return 0;
}
