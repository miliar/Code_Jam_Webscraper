#include <string> 
#include <vector> 
#include <map> 
#include <utility> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <queue> 
#include <stack> 
#include <set> 
#include <sstream> 
#include <algorithm> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
using namespace std; 
  
#define INF 0x3f3f3f3f
#define ALL(v) v.begin(),v.end() 
typedef pair<int,int> pii; 
typedef long long ll;

struct attack{
    int day;
    pii interval;
    int strength;
}AT[1005*1005];

bool sortsat(const attack &a, const attack &b){
    if(a.day==b.day) return a.strength < b.strength;
    return a.day<b.day;
}

#define OFF(x) x+1001
int height[2005][2005];

int main(){
    int test;
    scanf("%d",&test);

    for(int tt=1;tt<=test;tt++){      
        printf("Case #%d: ",tt);
        int nt;
        scanf("%d",&nt);
        int sat=0;
        for(int i=0;i<nt;i++){
            int di,ni,wi,ei,si,ddi,dpi,dsi;
            scanf("%d %d %d %d %d %d %d %d",&di,&ni,&wi,&ei,&si,&ddi,&dpi,&dsi);
            for(int j=0;j<ni;j++){
                AT[sat].day = di + ddi * j;
                AT[sat].interval.first = wi + dpi * j;
                AT[sat].interval.second = ei + dpi * j;
                AT[sat].strength = si + dsi * j;
                sat++;                          
            }
        }
        sort(AT,AT+sat,sortsat);
        int res=0;
        memset(height,0,sizeof(height));
        for(int i=0;i<sat;i++){
            
            bool succ=false;
            for(int j=AT[i].interval.first;j<AT[i].interval.second;j++)
                if(height[OFF(j)][OFF(j+1)]<AT[i].strength){
                    succ=true;
                    height[OFF(j)][OFF(j+1)]=AT[i].strength;
                }
            if(succ)
                res++;
//            printf("%d %d %d %d %d\n",AT[i].day,AT[i].interval.first,AT[i].interval.second,AT[i].strength,succ);
        }
        printf("%d",res);
        printf("\n");
    }

    return 0;
}
