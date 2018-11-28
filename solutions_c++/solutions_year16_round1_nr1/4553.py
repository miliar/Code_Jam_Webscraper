#include <bits/stdc++.h>

using namespace std;

set<string> dict;
string s;

void bfs(int i, string ss, bool fin){
    if(i==s.size()){
        dict.insert(ss);
        return;
    }

    if(fin){
        ss+=s[i];
    }else{
        ss=s[i]+ss;
    }

    bfs(i+1, ss, true);
    bfs(i+1, ss, false);
}

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    ifstream cin("A-small-attempt0.in");
    ofstream cout("smallOutput.txt");

    int tc, i;
    set<string>::reverse_iterator it;
    cin>>tc;
    i=1;
    string ss;
    while(i<=tc){
        cin>>s;
        dict.clear();
        ss="";
        bfs(0, ss, true);

        it=dict.rbegin();
        cout<<"Case #"<<i<<": "<<*it<<"\n";
        i++;
    }
    return 0;
}
