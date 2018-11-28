#include <bits/stdc++.h>

#define forn(i,n) for(int i = 0; i < n; i++)
//#define forit(it,c) for(auto it = c.begin(); it != c.end(); ++it)
#define WATCH(x) cout << #x << ": " << x << endl

using namespace std;

void exec(){

    vector< pair<int,int> > v;
    int n, buffer, sum = 0;
    bool end = false;

    cin >> n;

    forn(i, n){
        cin >> buffer;
        sum += buffer;
        v.push_back(make_pair(buffer, i));
    }

    sort(v.begin(), v.end(), greater< pair<int,int> >());
    if(sum % 2 == 1){
        printf("%c ", 'A' + v[0].second);
        v[0].first--;
    }

    while(!end){
        // forn(i, n) cout << v[i].first << char('A' + v[i].second) << " "; /////////
        // cout << endl; ////////////////
        sort(v.begin(), v.end(), greater< pair<int,int> >());
        if(v[0].first == 0) end = true;
        if(!end){
            if(v[0].first - v[1].first > 1){
                printf("%c%c ", ('A' + v[0].second), ('A' + v[0].second));
                v[0].first -= 2;
            }
            else {
                printf("%c%c ", ('A' + v[0].second), ('A' + v[1].second));
                v[0].first--;
                v[1].first--;
            }
        }
        // cout << endl; /////////////////
    }
    cout << endl;

}

int main(){

    int testCases;

    cin >> testCases;
    forn(tt, testCases){
        cout << "Case #" << tt + 1 << ": ";
        exec();
    }

    return 0;
}
