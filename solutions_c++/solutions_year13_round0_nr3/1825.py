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

bool ispal(ll x){
    string r;
    while(x){
        r+=((x%10)+'0');
        x/=10;
    }
    for(int i=0;i<r.size()/2;i++)
        if(r[i]!=r[r.size()-1-i])
            return false;

    return true;
}

int main(){
    int test;
    scanf("%d",&test);
    long long a=1,b=100000000000001LL;
    vector<long long> pre;
    int sqa=sqrt(double(a)),sqb=sqrt(double(b));
    for(ll i=sqa;i<=sqb;i++)
            if(i*i>=a&&i*i<=b&&ispal(i)&&ispal(i*i))
                pre.push_back(i*i);
            

    for(int tt=1;tt<=test;tt++){      
        printf("Case #%d: ",tt);
        
        scanf("%lld %lld",&a,&b);
        

        int res=0;

        for(int i=0;i<pre.size();i++)
            if(pre[i]>=a&&pre[i]<=b)
                res++;        

        printf("%d",res);
        printf("\n");
    }

    return 0;
}
