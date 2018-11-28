#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
#define sz(v) (int)(v.size())
#define clr(v, d) memset(v, d, sizeof(v))
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define MAX 110


using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

const int OO = (int)1e9+7;
const int MX = (int)1e3+7;
const int mod = (int)1e9+7;

int res, n;
string s;

void fix(int idx){

    int j = 0;

    if(s[j]=='+'){
        while(s[j]=='+'){
            s[j++] = '-';
        }
        res++;
    }

    reverse(s.begin(), s.begin()+idx+1);
    for(int i=0; i<=idx; i++){
        s[i] = (s[i]=='+'? '-' : '+');
    }

    res++;
}

int main(void){

    ios_base::sync_with_stdio(false);

    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;

    for(int cc=1; cc<=t; cc++){

        cin>>s;

        cout<<"Case #"<<cc<<": ";

        res = 0;
        n = s.length();

        for(int i=n-1; i>=0; i--){
            if(s[i]=='-'){
                fix(i);
            }
        }

        cout<<res<<"\n";
    }

    return 0;
}
