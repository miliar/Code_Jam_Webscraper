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

int pr[15];

int main(){
    int test;
    scanf("%d",&test);

    for(int tt=1;tt<=test;tt++){      
        printf("Case #%d:\n",tt);
        int r,n,m,k;
        scanf("%d %d %d %d",&r,&n,&m,&k);
        for(int rr=0;rr<r;rr++){        
        
        for(int i=0;i<k;i++) scanf("%d",&pr[i]);

        for(int a=2;a<=m;a++)
        for(int b=a;b<=m;b++)
        for(int c=b;c<=m;c++){
            int i;            
            for(i=0;i<k;i++){
                bool found=false;
                for(int j=0;j<(1<<n);j++){
                    int p=1;                    
                    if(j&1) p*=a;
                    if(j&2) p*=b;
                    if(j&4) p*=c;
                    if(p==pr[i]) {found=true; break;}            
                }
                if(!found) break;
            }
            if(i==k) {printf("%d%d%d\n",a,b,c); goto sal;}
        }
sal:
        ;
        }
    }

    return 0;
}
