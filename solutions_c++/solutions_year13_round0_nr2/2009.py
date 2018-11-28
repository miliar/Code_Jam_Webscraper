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

int arr[105][105];


int main(){
    int test;
    scanf("%d",&test);
    
    for(int tt=1;tt<=test;tt++){      
        printf("Case #%d: ",tt);
        int n,m;
        scanf("%d %d",&n,&m);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                scanf("%d",&arr[i][j]);
        
        bool gt=false;
        for(int i=0;i<n&&!gt;i++)
            for(int j=0;j<m&&!gt;j++){
                bool gtr=false,gtc=false;
                for(int k=0;k<m;k++)
                    if(arr[i][k]>arr[i][j]) gtr=true;
                for(int k=0;k<n;k++)
                    if(arr[k][j]>arr[i][j]) gtc=true;
                gt=gtr&&gtc;                            
            }
        if(gt) printf("NO");
        else printf("YES");
        printf("\n");
    }

    return 0;
}
