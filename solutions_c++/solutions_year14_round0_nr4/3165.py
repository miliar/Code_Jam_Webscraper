#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>
#include <math.h>
#include <map>
#include <utility>
#include <fstream>
using namespace std;

#define mp make_pair
#define pb push_back
#define INF -1
#define MAX 10000007
#define X first
#define Y second
#define all(x) x.begin(),x.end()
#define fi freopen("D-large.in","r",stdin);
#define REP(i,n) for(int i=0;i<n;i++)
typedef pair<int,int> pii;

int main() {
    fi;
    freopen("out.out","w",stdout);

    int t,n;
    cin>>t;
    vector <double> a,b;
    double x;
    for(int cas=1;cas<=t;cas++) {
        a.clear();
        b.clear();
        cout<<"Case #"<<cas<<": ";
        cin>>n;
        for(int i=0;i<n;i++) {
            cin>>x;
            a.pb(x);
        }
        for(int j=0;j<n;j++) {
            cin>>x;
            b.pb(x);
        }
        sort(all(a));
        reverse(all(a));
        sort(all(b));
        reverse(all(b));

        int cnt=0,pos=0;
        for(int i=0;i<n;i++) {
            if(a[pos]>b[i]) {
                cnt++;
                pos++;
            }
        }
        cout<<cnt<<" ";

        cnt=0,pos=0;
        for(int i=0;i<n;i++) {
            if(b[pos]>a[i]) {
                cnt++;
                pos++;
            }
        }
        cnt=n-cnt;
        cout<<cnt<<"\n";
    }
}
