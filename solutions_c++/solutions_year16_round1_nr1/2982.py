# include <bits/stdc++.h>
using namespace std;

int main(){
    /*
    freopen("0-small-attempt0.in", "r", stdin);
    freopen("0-small-output.txt", "w", stdout);
    */


    freopen("A-large.in", "r", stdin);
    freopen("A-large-output.txt", "w", stdout);


    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    int cases, caseno=0;
    char st[1009];
    cin >> cases;
    while(cases--){
        cin >> st;
        deque <char> DQ;
        DQ.push_back(st[0]);
        for (int i=1; st[i]; i++){
            if (st[i]>=DQ.front()) DQ.push_front(st[i]);
            else DQ.push_back(st[i]);
        }
        cout << "Case #" << ++caseno << ": ";
        while(!DQ.empty()){
            cout << DQ.front();
            DQ.pop_front();
        }
        cout << "\n";
    }
    return 0;
}
