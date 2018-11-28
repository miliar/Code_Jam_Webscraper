#include <bits/stdc++.h>

using namespace std;

int n, k;
long double t[201][201], b[201];
vector<long double> v;

int main()
{
    freopen("B.in","r",stdin);
    freopen("out.txt","w",stdout);
    int q;
    cin >> q;
    t[0][0]=1;
    for(int x=0;x<q;x++) {
        cin >> n>> k;
        for(int i=0;i<n;i++) cin >> b[i];
        sort(b,b+n);
        long double ki=0;
        for(int i=0;i<=k;i++) {
            v.clear();
            v.push_back(0);
            for(int j=0;j<i;j++) v.push_back(b[j]);
            for(int j=n-(k-i);j<n;j++) v.push_back(b[j]);
            for(int j=1;j<=k;j++) {
                t[j][0]=(1-v[j])*t[j-1][0];
                for(int l=1;l<=j;l++) t[j][l]=v[j]*t[j-1][l-1]+(1-v[j])*t[j-1][l];
            }
            if(t[k][k/2]>ki) ki=t[k][k/2];
        }
        cout << "CASE #" << x+1 << ": ";
        cout << ki << endl;

    }
    return 0;
}
