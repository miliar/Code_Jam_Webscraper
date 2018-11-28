#include <bits/stdc++.h>
using namespace std;
#define LL long long int
#define SI short int
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pbc pair<bool,char>
#define pcc pair<char,char>
#define vi vector<int>
#define vii vector<vector<int> >
#define vb vector<bool>
#define FOR(i,st,end) for(int (i)=(st);i<(end);i++)
#define FORD(i,st,end) for(int (i)=(st);i>=(end);i--)
#define FASTIO ios::sync_with_stdio(false);
#define ABS(i) ((i)>0)?(i):(-(i))
#define sci(m) scanf(" %d",&m)
#define SORT(x) sort(x.begin(),x.end())
#define MOD 1000000007

int main(void){
    string s;
    int T;
    sci(T);
    FOR(t,0,T){
        cin>>s;
        printf("Case #%d: ",t+1);
        int moves = 0,idx = 0;
        if(s[0]=='-'){
            while(idx<s.length() && s[idx]=='-')
                idx++;
            moves = 1;
        }
        else moves = 0;
        while(idx<s.length()){
            //present at +
            while(idx<s.length() && s[idx]=='+')
                idx++;
            if(idx<s.length()){
                //found a -.
                moves+=2;
                while(idx<s.length() && s[idx]=='-')
                    idx++;
            }
        }
        printf("%d\n",moves);
    }
    return 0;
}
