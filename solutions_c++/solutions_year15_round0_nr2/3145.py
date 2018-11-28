#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int a[1005];

int main() {
    freopen("/Users/pfctgeorge/Documents/Programs/Google Code Jam 2015 Qualification/B.txt","r",stdin);
    freopen("/Users/pfctgeorge/Documents/Programs/Google Code Jam 2015 Qualification/B.out","w",stdout);
    int T;
    cin >> T;
    int ca = 0;
    while (T--) {
        int n;
        cin>>n;
        int m = 0;
        for (int i=0;i<n;i++) {
            cin>>a[i];
            m = max(m, a[i]);
        }
        sort(a,a+n);
        for (int i=1000;i>=1;i--) {
            int spec = 0;
            for (int j=0;j<n;j++) {
                if (a[j] > i) {
                    int now = a[j];
                    while (now > i) {
                        now -= i;
                        spec ++;
                    }
                }
            }
            m = min(m, spec + i);
        }
        cout << "Case #" << ++ca << ": " << m << endl;
    }
}