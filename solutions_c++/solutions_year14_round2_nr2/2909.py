#include <iostream>
#include <cstdio>
using namespace std;
int t;
long long a,b,x,sum,y;
int main()
{
//    freopen("B-small-attempt0.in","r",stdin);
//    freopen("out.out","w",stdout);
    cin >> t;
    for(int i=1;i<=t;i++){
        cin >> a >> b >> x;
        sum=0;
        for(long long j=0;j<a;j++){
            for(long long k=0;k<b;k++){
                y=j&k;
                if (y<x) sum++;
            }
        }
        cout << "Case #"<<i<<": " <<sum<<endl;
    }
    return 0;
}
