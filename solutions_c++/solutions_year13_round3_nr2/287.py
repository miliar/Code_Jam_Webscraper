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
typedef pair<char,int> pci;
typedef long long ll;
int x,y;

int main(){
    int test;
    scanf("%d",&test);
    
    for(int tt=1;tt<=test;tt++){      
        printf("Case #%d: ",tt);
        scanf("%d %d",&x,&y);
        if(x>0){
            for(int i=0;i<x;i++)
                printf("WE");
        }else{
            x*=-1;
            for(int i=0;i<x;i++)
                printf("EW");
        }

        if(y>0){
            for(int i=0;i<y;i++)
                printf("SN");
        }else{
            y*=-1;
            for(int i=0;i<y;i++)
                printf("NS");
        }

        printf("\n");
    }

    return 0;
}
