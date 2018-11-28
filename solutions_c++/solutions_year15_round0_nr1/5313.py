#include <bits/stdc++.h>

#define INF (1 << 29)
#define rep2(i,m,n) for(int i=(int)(m);i<(int)(n);i++)
#define rep(i,n) rep2(i,0,n)
#define EPS 1e-10

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

int main()
{
    int T;
    cin >> T;
    rep(case_num,T){
        int s;
        cin >> s;
        string str;
        cin >> str;
        int res = 0;
        int count = 0;
        int pos = 0;
        while(pos < str.size()){
            while(str[pos]>'0'&&pos>count){
                res++;
                count++;
            }
            count+=str[pos]-'0';
            pos++;
        }
        cout << "Case #" << case_num+1 << ": " << res << endl;
    }
    return 0;
}

