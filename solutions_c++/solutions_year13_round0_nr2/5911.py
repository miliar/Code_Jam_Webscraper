#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<deque>
#include<set>
using namespace std;
#define ll long long
#define VI vector<ll>
#define VS vector<string>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back

int main() {
    int T;
    cin>>T;
    for (int t=0;t<T;t++) {
        cout<<"Case #"<<t+1<<": ";
            vector<VI> a;
            int n,m; cin>>n>>m;
            for (int i=0;i<n;i++) {
              VI v;
              for (int j=0;j<m;j++) { int x; cin>>x; v.PB(x);}
              a.PB(v);
            }
            bool ok=true;

            VI left;
            for (int i=0;i<n;i++) {
                int ma = -1;
                for (int j=0;j<m;j++) if (a[i][j]>ma) ma = a[i][j];
                left.PB(ma);
            }

            VI top;
            for (int j=0;j<m;j++) {
                int ma=-1;
                for (int i=0;i<n;i++) if (a[i][j]>ma) ma = a[i][j];
                top.PB(ma);
            } 

            for (int i=0;i<n;i++) for (int j=0;j<m;j++) if (a[i][j] !=
                    min(left[i],top[j]) ) ok = false;

            if (ok) cout<<"YES"; else cout<<"NO";


        cout<<endl;
    }
}
