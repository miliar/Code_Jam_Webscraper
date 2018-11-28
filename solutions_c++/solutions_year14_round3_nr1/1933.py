#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

long long gcd(long long u,long long v)
{
    int t;

    while(u > 0){

        if(u < v){

            t = u;

            u = v;

            v = t;
        }
        u = u - v;
    }
    return v;
}
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("A.txt","w",stdout);

    int tc,cas = 0;

    long long a,b;

    scanf("%d",&tc);

    while(tc--){

        scanf("%lld/%lld",&a,&b);

        printf("Case #%d: ",++cas);

        long long int g = gcd(a,b);

        a = a/g;
        b = b/g;

        if(pow(2,log2(b)) == b){

            cout << floor((log2(b/pow(2,floor(log2(a)))))) << endl;
        }
        else {

            cout << "impossible\n";
        }
    }
    return 0;
}
