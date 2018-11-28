#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int t,n;
int r1,r2;
vector<double> v1;
vector<double> v2;

int main() {
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> t;
    for(int i=1;i<=t;i++) {
        cin >> n;
        v1.clear();
        v2.clear();
        for(int j=0;j<n;j++) {
            double tmp;
            cin >> tmp;
            v1.push_back(tmp);
        }
        for(int j=0;j<n;j++) {
            double tmp;
            cin >> tmp;
            v2.push_back(tmp);
        }
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        for(int j=0;j<n;j++) {
            v1.push_back(v1[j]);
            v2.push_back(v2[j]);
        }
        r1 = 0,r2 = 1005;
        for(int j=0;j<n;j++) {
            for(int k=0;k<n;k++) {
                int m1 = 0,m2 = 0;
                for(int l=0;l<n;l++) {
                    if(v1[j+l] > v2[k+l]) m1 ++;
                    else m2 ++;
                }
                r1 = max(r1,m1);
                r2 = min(r2,n-m2);
            }
        }
        cout << "Case #" << i << ": " << r1 << " " << r2 << endl;
    }
    return 0;
}
