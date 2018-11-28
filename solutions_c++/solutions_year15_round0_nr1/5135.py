#include<iostream>
#include<queue>
#include<algorithm>
#include<vector>
#include <map>
#include <set>
using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define sz size()
#define pb push_back
#define mp make_pair
#define fr(i, n) for(i=0;i<n;i++)
#define fr2(i, a, n) for(i=a;i<n;i++)

int main() {
    int tt;
    cin >> tt;
    for (int t = 1; t <= tt; t++) {
        int n;
        cin >> n;
        n++;
        int a[n];

        string s;
        cin >> s;
        for (int i = 0; i < n; i++)
            a[i] = s[i] - '0';
        int tot = a[0];
        int need = 0;
        for (int i = 1; i < n; i++) {
            //    cout << tot << " ";
                if (i <= tot)
                    tot += a[i];
                else {
                    need += i - tot;
                    tot += a[i] + i - tot;   
                }    
              //  cout << need << tot << endl;
        }
        
        cout << "Case #" << t << ": " << need << endl;
            
    }    
}
