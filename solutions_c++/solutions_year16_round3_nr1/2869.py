#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int t,n;
    pair<int, char> P[30];
    cin>>t;
    for (int T=1; T <= t; T++) {
        cin>>n;
        for (int i=0; i < n; i++) {
            cin>>P[i].first;
            P[i].second='A'+i;
        }
        cout<<"Case #"<<T<<": ";
        while(1) {
            sort(P,P+n);
            if(P[n-1].first==0) break;
            if(n>=3 && P[n-3].first==1 && P[n-1].first==1) {
                cout<<P[n-1].second<<" ";
                cout<<P[n-2].second<<P[n-3].second<<" ";
                P[n-1].first--;
                P[n-2].first--;
                P[n-3].first--;
                continue;
            }
            if(P[n-1].first==P[n-2].first) {
                cout<<P[n-1].second<<P[n-2].second<<" ";
                P[n-1].first--;
                P[n-2].first--;
            } else {
                cout<<P[n-1].second<<P[n-1].second<<" ";
                P[n-1].first-=2;
            }
        }
        cout<<"\n";
    }
}
