#include <iostream>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    int e,r,n;
   // double pi=3.1415926535897932;
    vector <int> v;
    for (int o_O=0;o_O<t;o_O++){
          cout << "Case #" << o_O+1 << ": ";
          cin >> e >> r >> n;
          v.assign(n, 0);
          for (int i=0;i<n;i++){
            cin >> v[i];
          }
          long long ans=0;
          vector <long long> q(e+1,0);
          vector <long long> w(e+1,0);
          for (int i=0;i<n;i++){
            w.assign(e,0);
            for (int j=0;j<=e;j++){
                for (int k=0;k <= j;k++){
                    if (j-k+r <= e)
                        w[j-k+r]=max(w[j-k+r],q[j]+v[i]*k);
                    else
                        w[e]=max(w[e],q[j]+v[i]*k);
                }
            }
            for (int j=0;j<=e;j++)
                q[j]=w[j];
          }
          for (int i=0;i<=e;i++)
            if (q[i] > ans)
                ans=q[i];
          cout << ans << endl;
    }
    return 0;
}
