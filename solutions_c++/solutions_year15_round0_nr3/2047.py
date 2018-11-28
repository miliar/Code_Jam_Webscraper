#include <iostream>
#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>
#include <map>
using namespace std;
typedef pair<char,char> cc;
typedef pair<char,bool> cb;
int main()
{
    ifstream cin("input.in");
    ofstream cout("output.out");
    map<cc,cb> Kefel;
    Kefel[cc('1','1')] = cb('1',0);
    Kefel[cc('i','1')] = cb('i',0);
    Kefel[cc('j','1')] = cb('j',0);
    Kefel[cc('k','1')] = cb('k',0);
    Kefel[cc('1','i')] = cb('i',0);
    Kefel[cc('i','i')] = cb('1',1);
    Kefel[cc('j','i')] = cb('k',1);
    Kefel[cc('k','i')] = cb('j',0);
    Kefel[cc('1','j')] = cb('j',0);
    Kefel[cc('i','j')] = cb('k',0);
    Kefel[cc('j','j')] = cb('1',1);
    Kefel[cc('k','j')] = cb('i',1);
    Kefel[cc('1','k')] = cb('k',0);
    Kefel[cc('i','k')] = cb('j',1);
    Kefel[cc('j','k')] = cb('i',0);
    Kefel[cc('k','k')] = cb('1',1);
    int t; cin >> t;
    for(int a = 0;a<t;a++){
        int l,x; cin >> l >> x;
        string s;
        cin >> s;
        string newS = "";
        for(int i = 0;i<x;i++){
            newS += s;
        }
        cb now = cb('1',0);
        for(int i = 0;i<newS.size();i++){
            char newC = Kefel[cc(now.first,newS[i])].first;
            bool newSign = Kefel[cc(now.first,newS[i])].second ^ now.second;
            now = cb(newC,newSign);
        }
        if(now != cb('1',1)){
            cout << "Case #"<< a+1 <<": NO\n";
            continue;
        }
        now = cb('1',0);
        int first_ind = 0;
        for(int i = 0;i<newS.size() && now != cb('i',0);i++,first_ind++){
            char newC = Kefel[cc(now.first,newS[i])].first;
            bool newSign = Kefel[cc(now.first,newS[i])].second ^ now.second;
            now = cb(newC,newSign);
        }
        int second_ind = newS.size()-1;
        now = cb('1',0);
        for(int i = newS.size()-1;i>=0 && now != cb('k',0);i--,second_ind--){
            char newC = Kefel[cc(newS[i],now.first)].first;
            bool newSign = Kefel[cc(newS[i],now.first)].second ^ now.second;
            now = cb(newC,newSign);
        }
        if(--first_ind < ++second_ind){
            cout << "Case #"<< a+1 <<": YES\n";
            continue;
        }
        else{
            cout << "Case #"<< a+1 <<": NO\n";
            continue;
        }
    }
    return 0;
}
