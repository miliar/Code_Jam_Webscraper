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

int main(){
    int test;
    scanf("%d",&test);
    ll r,t;        
    for(int tt=1;tt<=test;tt++){
        cin>>r>>t;
        printf("Case #%d: ",tt);
        ll l=0,u=t,res=0;
        while(l<=u){
            double dm=l; dm+=u; dm/=2; dm++;

            if(2*dm*dm + 2*dm*r - dm > double(t)){
                u=ll(dm);            
            }

            double m = (l+u)/2;            

            if( 2*m*m + 2*m*r - m <= t ){
                res = m;
                l = m + 1;
            }else{
                u = m - 1;      
            }                                
        }
        cout<<res;
        printf("\n");
    }

    return 0;
}
