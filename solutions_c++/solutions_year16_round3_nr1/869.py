# include <bits/stdc++.h>
using namespace std;

struct senator{
    int num, type;
    bool operator < (const senator &n) const{
        return num < n.num;
    }
};

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large-output.txt", "w", stdout);
    int cases, caseno=0, n, p;
    priority_queue <senator> S;
    string send;
    senator temp;
    cin >> cases;
    while(cases--){
        cin >> n;
        for (int i=0; i<n; i++){
            cin >> p;
            temp.type = i;
            temp.num = p;
            S.push(temp);
        }
        cout << "Case #" << ++caseno << ":";
        while(true){
            send = "";
            if (S.size()<=2) break;
            temp = S.top();
            S.pop();
            send += (temp.type + 'A');
            temp.num--;
            if (temp.num) S.push(temp);
            if (S.size()<=2){
                cout << " " << send;
                break;
            }
            temp = S.top();
            S.pop();
            send += (temp.type + 'A');
            temp.num--;
            if (temp.num) S.push(temp);
            cout << " " << send;
        }
        while(!S.empty()){
            send = "";
            temp = S.top();
            S.pop();
            send += (temp.type + 'A');
            temp.num--;
            if (temp.num) S.push(temp);
            if (S.empty()){
                cout << " " << send;
                break;
            }
            temp = S.top();
            S.pop();
            send += (temp.type + 'A');
            temp.num--;
            if (temp.num) S.push(temp);
            cout << " " << send;
        }
        cout << endl;
    }
    return 0;
}
