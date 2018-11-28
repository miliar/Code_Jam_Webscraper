#include <bits/stdc++.h>
using namespace std;
int main(void){
    freopen("A-large.in", "r", stdin); freopen("C_output.txt", "w", stdout);
    int t, n, i, T, s;
    priority_queue<pair<int, char> > p;
    pair<int, char> temp1, temp2;
    cin>>t;
    for(T = 1; T <= t; T++){
        cin>>n;
        while( !p.empty()) p.pop();
        for(i = 0; i < n; i++){
            cin>>temp1.first;
            temp1.second = 'A' + i;
            p.push(temp1);
        }
        cout<<"Case #"<<T<<":";
        while( !p.empty()){
            s = p.size();
            temp1 = p.top(); p.pop();
            temp2 = p.top(); p.pop();
            if(temp1.first == temp2.first && (temp2.first != p.top().first) || s == 2){
                cout<<" "<<temp1.second<<temp2.second;
                temp1.first = --temp2.first;
            }else if(temp1.first - temp2.first >= 1){
                cout<<" "<<temp1.second<<temp1.second;
                temp1.first -= 2;
            }else{
                cout<<" "<<temp1.second;
                --temp1.first;
            }
            if(temp1.first) p.push(temp1); if(temp2.first) p.push(temp2);
        }
        cout<<endl;
    }
    fclose(stdin); fclose(stdout);
}
