#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<vector>
#include<bitset>
#include<map>
#include<set>
#include<climits>
#include<algorithm>
#include<utility>
#include<cstdlib>
#include<cctype>
#include<queue>
#include<sstream>
#include <stack>
#include <list>
#include <numeric>
#define INT_MAX 2147483647
#define INT_MIN -2147483647 //2^31-1
#define pi acos(-1.0)
#define N 1000000
#define LL unsigned long long
#define read(x) scanf("%d",&x)
#define write(x) printf("%d\n",x)
#define assign(x,n) x=(int*)calloc(n,4)
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define SWAP(a,b) a= a^b, b=a^b, a=a^b
typedef  long long int ull;
using namespace std;

int main()
{
//freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
int t;cin>>t;

for(int k=1;k<=t;k++){
        
        double c,f,x,ans=0.0,a,v=INT_MAX,n=1;
        cin>>c>>f>>x;
        
        v= x/2; // 0 farms
      
        while(1){
                   
        ans += c/(2+ (n-1)*f);    
        
        a= x/(2+ n*f);         
        //cout<<v<<endl<<ans+a<<endl; 
               
        if(v<ans+a){printf("Case #%d: %.7lf\n",k,v); break;}
        else v= ans+a;
        
        n++;
        }
        
        }
//system("pause");
return 0;
}
