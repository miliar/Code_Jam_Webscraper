#include <iostream>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

int n,m;
string a[10];
int b[10];
set<string> c[10];
int d[10];

int main() {
    int TT;
    cin>>TT;
    for(int T=1;T<=TT;T++) {
        cin>>m>>n;
        for(int i=0;i<m;i++) cin>>a[i];
        int ans=0,ans2=0;
        for(int i=0;i<=m;i++) b[i]=0;
        while(b[m]==0) {
            int sum=0;
            for(int i=0;i<n;i++) {
                d[i]=0;
                c[i].clear();
                c[i].insert("");
            }
            for(int i=0;i<m;i++) {
                int k=b[i];
                d[k]=1;
                string s=a[i];
                while(s.size()>0) {
                    if (c[k].count(s)==0) {
                        c[k].insert(s);
                    }
                    s.resize(s.size()-1);
                }
            }
            int cc=0;
            for(int i=0;i<n;i++) {
                cc+=d[i];
                sum+=c[i].size();
            }
            if (cc==n) {
                if (sum==ans) ans2++;
                else if (sum>ans) {
                    ans=sum;
                    ans2=1;
                }
            }
            if (n==1) break;
            int j=0;
            while(b[j]==n-1) j++;
            b[j]++;
            for(int i=0;i<j;i++) b[i]=0;
        }
        cout<<"Case #"<<T<<": ";
        cout<<ans<<' '<<ans2;
        cout<<endl;
    }
    return 0;
}