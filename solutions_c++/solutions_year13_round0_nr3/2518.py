#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <cstdio>
#define FOR(k,x,n) for(long long k=x;k<n;k++)
#define SORT(x) sort(x.begin(),x.end())
using namespace std;
bool ispal(long long x);
int main()
{
    ios_base::sync_with_stdio(false);
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    long long Test,cases=1;
    cin>>Test;
    long long sqpal[]={
1,
4,
9,
121,
484,
10201,
12321,
14641,40804,
44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,
400080004,404090404,10000200001LL,10221412201LL,12102420121LL,12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,
1022325232201LL,
1024348434201LL,
1210024200121LL,
1212225222121LL,
1214428244121LL,
1232346432321LL,
1234567654321LL,
4000008000004LL,
4004009004004LL
};
 
    for(long long i=0;i<Test;i++){
                                            long long a,b,c=0;
                                            cin>>a>>b;
                                            for(long long k=0;k<39;k++){
                                                                            if( sqpal[k] >=a && sqpal[k] <=b  ){
                                                                                c++;
                                                                                }
                                                                            }
                                                                                                                                        cout<<"Case #"<<cases<<": "<<c<<endl;
                                                                                                                                        cases++;
                                                                                                                                        }
                                                                                                                                        return 0;
}
 
bool ispal(long long x){
                long long aux=x;
                                                                                                        long long res=0;
                                                                                                        while(aux>0){
                                                                                                        res+=aux%10;
                                                                                                        aux/=10;
                                                                                                        if(aux>0)
                                                                                                        res*=10;
                                                                                                        }
                if(res==x)return true;
                return false;
                }
