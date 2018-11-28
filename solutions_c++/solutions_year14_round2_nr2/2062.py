#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>

using namespace std;

int main()
{
//    freopen("D:\\GCJ\\R1B\\B-small-attempt0.in","r",stdin);
//    freopen("D:\\GCJ\\R1B\\B-small-attempt0.txt","w",stdout);
    int T,a,b,k;
    cin >> T;
    for (int cas = 0; cas < T; cas++){
        cin >> a >> b >> k;
        if (a>b) swap(a,b);
        int ans = 0;
        if (a<=k)
            ans = a*b;
        else {
            ans = k*b;
            for (int i=k;i<a;i++){
                for (int j=0;j<b;j++)
                    if ((i&j)<k)
                        ans++;
            }
        }
        cout << "Case #"<<cas+1<<": "<<ans<<endl;
    }
    return 0;
}
