#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <string>

using namespace std;


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int o=0;o<t;o++){
        cout << "Case #" << o+1 << ": ";
        int n, x;
        cin >> n;
        vector <int> a(n,0);
        vector <int> b(n,0);
        for (int i=0;i<n;i++){
            cin >> a[i];
            b[i] = i;
        }
        int p=1;
        for (int i=1;i<=n;i++)
            p *= i;
        int ans = 1000000000;
        for (int i=0;i<p;i++){
            int tmp = 0;
            int k = 0;
            while ((k < n-1)&&(a[b[k]] < a[b[k+1]])){
                k++;
            }
            while ((k < n-1)&&(a[b[k]] > a[b[k+1]])){
                k++;
            }
            if (k == n-1){
                vector <int> c(n,0);
                vector <int> d(n,0);
                for (int j=0;j<n;j++){
                    c[j] = a[j];
                    d[j] = a[b[j]];
                }
                for (int j=0;j<n;j++){
                    for (int k=0;k<n;k++){
                        if (d[j] == c[k]){
                            for (int l = k; l > j;l--){
                                tmp++;
                                swap(c[l], c[l-1]);
                            }
                        }
                    }
                }
                if (tmp < ans)
                    ans = tmp;
            }
            next_permutation(b.begin(),b.end());
        }
        cout << ans << endl;
    }
    return 0;
}
