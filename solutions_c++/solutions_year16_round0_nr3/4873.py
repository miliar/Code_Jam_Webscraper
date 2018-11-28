#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<int(n);i++)
#define forsn(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define dforsn(i,s,n) for(int i=(int)(n-1);i>=int(s);i--)
#define si(a) ((int)(a).size())
#define pb push_back
#define mp make_pair
//#define endl '\n'
#define all(a) a.begin(),a.end()
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long int tint;


const string NUM = "1111111111111111";

vector<pair<string,vi> > res;

tint mpow(tint a,int b){
    tint res =1;
    forn(i,b){res*=a;
    }
    return res;
}

int check(string s, tint i){
    tint n = 0;
    dforsn(j,0,si(s)){
        n += (tint)((tint)(s[j]-'0') * (tint)mpow(i,(tint)(si(s)-1-j)));
    }



    for(tint j = 2;j*j < n;j++){
        if(n%j==0)return j;
    }
    return -1;
}

void makenum(string s,int i){
    if(si(res)>=50)return;
    if(i == 15){
        pair<string,vi> a;
        a.first=s;
        forsn(i,2,11){
            int div =check(s,i);
            if(div == -1)return;
            a.second.pb(div);
        }
        res.pb(a);
        return;
    }

    s[i]='0';
    makenum(s,i+1);
    s[i]='1';
    makenum(s,i+1);
    return;
}

int main() {
	//ios_base::sync_with_stdio(false); cin.tie(0);
	freopen("C.out","w",stdout);

    //cerr << (NUM[si(NUM)-1]-'0') * pow(5,0) << endl;

    makenum(NUM,1);

    cout << "Case #1:" << endl;
    forn(i,si(res)){
        cout << res[i].first;
        forn(j,9)cout << " " << (res[i].second)[j];
        cout << endl;
    }


	return 0;
}
