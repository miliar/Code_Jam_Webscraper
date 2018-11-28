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
        int n;
        cin >> n;
        if (n == 2){
        string a, b;
        cin >> a >> b;
        int ans = 0;
        int i=0;
        bool f=false;
        while ((a.length()) || (b.length())){
            int i=0, j = 0;
            if (((a.length()) && (!b.length())) ||((!a.length()) && (b.length()))){
                cout << "Fegla Won" << endl;
                f=true;
                break;
            }
            while (a[i] == a[0])
                i++;
            while (b[j] == b[0])
                j++;
            if (a[0] != b[0]){
                cout << "Fegla Won" << endl;
                f=true;
                break;
            }else{
                ans += abs(j-i);
            }
            a.erase(a.begin(),a.begin()+i);
            b.erase(b.begin(),b.begin()+j);
        }
        if (!f){
            cout << ans << endl;
        }
        }
        /*
        vector<string> a(n, "");
        for (int i=0;i<n;i++)
            cin >> a[i];
        int ans = 0;
        vector<int> c(n, 0);
        vector<int> d(n, 0);
        c.assign(n, 0);
        d.assign(n, 0);
        bool f = true;
        bool q = true;
        while (q){
            q=false;
            vector<int> d(n, 0);
            d.assign(n,0);
            for (int j=0;j<n;j++){
                if (a[j][c[j]] != a[0][c[0]]){
                    f = false;
                    break;
                }
            }
            for (int i=0;i<n;i++){
                int p = c[i];
                int j=p;
                while ((j<a[i].length())&&(a[i][j] == a[i][p])){
                    c[i]++;
                    d[i]++;
                    j++;
                    q = true;
                }
            }
            int mi = 100002;
            for (int j=0;j<n;j++){
                int tt = 0;
                for (int k=0;k<n;k++){
                    tt += abs(d[j] - d[k]);
                }
                mi = min(tt, mi);
            }
            ans += mi;
            if (!f)
                break;
        }
        if (!f){
            cout << "Fegla Won" << endl;
        }
        else{
            cout << ans << endl;
        }*/
    }

    return 0;
}
