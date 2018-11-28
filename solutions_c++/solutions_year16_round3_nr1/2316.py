#include <bits/stdc++.h>
#define ALL(x) x.begin(),x.end()
using namespace std;
typedef pair<int,int> ii;

char ci(int a){
    return (char)(a+'A');
}
int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int t,n,i,j;
    vector<ii> pares;
    cin >> t;
    for(int caso = 1;caso<=t;caso++){
        cout << "Case #" << caso << ":";
        pares.clear();
        cin >> n;
        for(j=0;j<n;j++){
            cin >> i;
            pares.push_back( ii(i,j) );
        }
        int sz  = pares.size() - 1;

        while(pares.size() > 2){
            sort(ALL(pares));
            if( pares.size() == 3){
                if(pares[0].first == 1 &&
                   pares[1].first == 1 &&
                   pares[2].first == 1){
                    cout << " " << ci(pares[2].second);
                    pares.erase(pares.begin()+2);
                   break;
                   }
            }
            if ( pares[sz].first == pares[sz-1].first ){
                cout << " " << ci(pares[sz].second) << ci(pares[sz-1].second);
                pares[sz].first --;
                pares[sz-1].first--;

                if(pares[sz].first == 0){
                    pares.erase(pares.begin()+sz);
                    sz--;
                    if(pares[sz].first == 0){
                        pares.erase(pares.begin()+sz);
                        sz--;
                    }
                }
                else if (pares[sz-1].first == 0){
                    pares.erase(pares.begin()+sz-1);
                    sz--;
                }
            }
            else {
                cout << " " << ci(pares[sz].second);
                pares[sz].first--;
                if(pares[sz].first == 0 ){
                    pares.erase(pares.begin()+sz);
                    sz--;
                }
            }
        }
        if(pares.size() == 2){
            while(pares[0].first > pares[1].first ){
                cout << " " << ci(pares[0].second);
                pares[0].first--;
            }
            while(pares[1].first > pares[0].first ){
                cout << " " << ci(pares[1].second);
                pares[1].first--;
            }
            while( pares[0].first--){
                cout << " " << ci(pares[0].second) << ci(pares[1].second);
            }
        }
        else if( pares.size() == 1){
            int t = pares[0].first;
            while(t--){
                cout << " " << ci(pares[0].second);
            }
        }
        cout << "\n";
    }
    return 0;
}
