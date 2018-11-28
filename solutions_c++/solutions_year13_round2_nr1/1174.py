#include <iostream>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    int a, n;
    for (int o_O=0;o_O<t;o_O++){
        cout << "Case #" << o_O+1 << ": ";
        cin >> a >> n;
        vector <int> b(n,0);
        for (int i=0;i<n;i++)
            cin >> b[i];
        sort(b.begin(),b.end());
        int ans = n;
        int e=a;
        if (a != 1){
            for (int i=0;i<n;i++){
                a=e;
                int j=0;
                int m = 0;
                while (j < n-i){
                    while (a > b[j]){
                        a+=b[j];
                        j++;
                    }
                    if (j < n-i){
                        m++;
                        a+=a-1;
                    }
                }
                if (m + i < ans)
                    ans = m+i;
            }
        }
        cout << ans << endl;
    }
    return 0;
}
