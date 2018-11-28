#include <bits/stdc++.h>
using namespace std;
#define MAXN 55

int pieces[3*MAXN][2*MAXN];
int cnt[2525];

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("Bout.out","w",stdout);
    int t;
    cin >> t;
    for(int IN=0; IN<t; ++IN){
        int n;
        cin >> n;
        for(int i=0; i<2*n-1; ++i){
            for(int j=0; j<n; ++j){
                cin >> pieces[i][j];
                cnt[pieces[i][j]]++;
            }
        }
        vector<int>missing;
        for(int i=0; i<2*n-1; ++i){
            for(int j=0; j<n; ++j){
                if(cnt[pieces[i][j]]%2){
                    missing.push_back(pieces[i][j]);
                    cnt[pieces[i][j]] = 0;
                }
            }
        }
        //vector<int>a = unique(missing.begin(), missing.end());
        sort(missing.begin(),missing.end());
        cout << "Case #" << IN+1 << ": ";
        for(int i=0; i<missing.size(); ++i)
            cout << missing[i] << " ";
        cout << endl;
    }
}
