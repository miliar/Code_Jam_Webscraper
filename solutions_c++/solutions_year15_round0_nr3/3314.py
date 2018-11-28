#include<bits/stdc++.h>
using namespace std;

int rule[10][10];
int n,m;
string s_in,s_fin;
int a[20000];
int s[20000];
bool findi[20000];
int ans;

int getID(char x){
    if (x == 'i') return 2;
    if (x == 'j') return 3;
    if (x == 'k') return 4;
    return 1;
}

void output(int t,int x){
    cout << "Case #" << t << ": ";
    if (x) cout << "YES" << endl;
        else cout << "NO" << endl;
}

int main(){
    rule[1][1]=1; rule[1][2]=2;  rule[1][3]=3;  rule[1][4]=4;
    rule[2][1]=2; rule[2][2]=-1; rule[2][3]=4;  rule[2][4]=-3;
    rule[3][1]=3; rule[3][2]=-4; rule[3][3]=-1;  rule[3][4]=2;
    rule[4][1]=4; rule[4][2]=3; rule[4][3]=-2;  rule[4][4]=-1;

    int T_case;
    cin >> T_case;
    for (int tmp_case = 1;tmp_case <= T_case;++tmp_case){
        cin >> n >> m;
        cin >> s_in;
        s_fin = "";
        for (int i = 1;i <= m;++i) s_fin.append(s_in);
        for (int i = 1;i <= s_fin.length();++i)
            a[i] = getID(s_fin[i - 1]);
        n = n * m;
        s[1] = a[1];
        for (int i = 2;i <= n;++i)
        {
            s[i] = rule[ abs(s[i - 1]) ][ a[i] ];
            if (s[i - 1] < 0) s[i] *= -1;
        }

        if (n < 3){
            output(tmp_case,0);
            continue;
        }

        if (s[n] != -1){
            output(tmp_case,0);
            continue;
        }

        memset(findi,0,sizeof(findi));

        if (a[1] == 2) findi[1] = true;
        for (int i = 2;i <= n;++i) findi[i] = findi[i - 1] | (s[i] == 2);

        ans = 0;

        bool findk = 0;
        if (a[n] == 4) findk = 1;
        s[n] = a[n];
        for (int i = n - 1;i > 1;--i)
            if (findi[i - 1] && findk) ans = 1;
                else{
                    s[i] = rule[ a[i] ][ abs(s[i + 1]) ];
                    if (s[i + 1] < 0) s[i] *= -1;
                    if (s[i] == 4) findk = 1;
                }
        output(tmp_case,ans);
    }
    return 0;
}
