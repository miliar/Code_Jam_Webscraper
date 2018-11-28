#include <bits/stdc++.h>

using namespace std;

vector<string> numbers = {"ZERO", "TWO", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "THREE", "NINE", "ONE"};
vector<string> numberssz = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
vector< vector<int> > ctr(10,vector<int>(26,0));
vector<char> numbers2 = {'0', '2', '4', '5', '6', '7', '8', '3', '9', '1'};
int c[26];

string solve(string &s, bool increasing){
    string ans = "";
    memset(c,0,sizeof c);
    for(int i=0; i<s.size(); i++)
        c[ s[i] - 'A' ]++;


    int i = (increasing ? 0 : numbers.size()-1);
    while(true){
        if( increasing && i >= numbers.size() ) break;
        else if( !increasing && i < 0 ) break;

        while(true){
            bool all = true;
            for(int k=0; k<26 && all; k++)
                all &= c[k] >= ctr[i][k];

            if( all ){
                for(int k=0; k<26; k++)
                    c[k] -= ctr[i][k];

                ans.push_back( numbers2[i] );
            }else break;
        }

        if( increasing ) i++;
        else i--;
    }

    sort(ans.begin(),ans.end());
    return ans;

}

int main(){
//    freopen("sample.in.c","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("ALARGE.out","w",stdout);

    int T;
    cin >> T;


    for(int i=0; i<numbers.size(); i++)
        for(auto &c : numbers[i])
            ctr[i][ c - 'A' ]++;



    string s,ans;

    for(int cases=1; cases<=T; cases++){
        cin >> s;

        ans = solve(s,true);
        bool xd = true;
        for(int i=0; i<26 && xd; i++) xd &= c[i] == 0;
//        cout << xd << " " << ans << endl;
        if( !xd ) ans = solve(s,false);
        for(int i=0; i<26; i++) if( c[i] ) cout << "kha " << char(i+'A') << endl;
        int sz = 0;
        for(int i=0; i<ans.size(); i++) sz += numberssz[ ans[i] - '0' ].size();
        if(sz != s.size()) cout << "WRONG SIZE " << sz << " " << s.size() << endl;

        cout << "Case #" << cases << ": " << ans << endl;
    }
}
