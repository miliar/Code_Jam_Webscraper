#include <bits/stdc++.h>
using namespace std;
int t;
long long poww(long long x, int ex){
    long long alt = 1;
    for(int i=0;i<ex;i++){
        alt*=x;
    }
    return alt;
}
int main()
{
    freopen("stuff.in","r",stdin);
    freopen("stuff.out","w",stdout);
    long long k,c,s;
    cin >> t;
    for(int i=0;i<t;i++){
        cin >> k >> c >> s;
        cout << "CASE #" << (i+1) << ":" << " ";
        long long stuff = poww(k,c);
        long long other = stuff/k;
        long long start = 1;
        for(int j=0;j<k;j++){
            cout << start << " ";
            start += other;
        }
        cout << endl;
    }
    return 0;
}
