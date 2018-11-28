#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
#define mk make_pair
#define pb push_back
#define fst first
#define snd second

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;

map<char,int> who;
string str;
#define N 100000

int opm[][5] = { {0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int op( int a, int b ) {
        bool neg = a<0;
        if( b < 0 ) neg = !neg;

        //cout << a <<" " << b << endl;
        int r = opm[abs(a)][abs(b)];
        if( neg ) r *= -1;
        return r;
}

int dp[N][5];

bool f( int i, int wh ) {
        if( i == str.size() ) return wh==5;
        if( wh == 5 ) {
         //       cout << i << "!"<<endl;
                return false;
        }

        if( dp[i][wh] != -1 )
                return dp[i][wh];
        //cout << i << " " << wh << endl;

        bool ret = false;
        int mu = 1;
        for( int j = i; !ret && j<str.size(); j++ )
        {
                mu = op(mu,who[str[j]]);
                if( mu == wh )
                {
                        ret |= f(j+1,wh+1);
                }
        }
        return dp[i][wh] = ret;
}

int main(){
        who['i'] = 2;
        who['j'] = 3;
        who['k'] = 4;

        int t,ca=1;
        cin >> t;

        while (t-- )
        {
                str.clear();
                memset( dp, -1, sizeof dp );

                int l,x;
                string tmp;

                cin >> l >> x;
                cin >> tmp;

                for( int i = 0; i<x; i++ )
                        str.append(tmp);
                cout << "Case #" << ca++ << ": " << ((f(0,2))?"YES":"NO") <<  "\n";
        }

        return 0;
}
