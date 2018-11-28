#include <bits/stdc++.h>

using namespace std;

int n, t[3][13][3];
string s[3][13];


int main()
{
    freopen("A.in","r",stdin);
    freopen("out.txt","w",stdout);
    s[0][0]="R";
    s[1][0]="P";
    s[2][0]="S";
    t[0][0][0]=t[1][0][1]=t[2][0][2]=1;
    for(int i=1;i<13;i++) {
        for(int j=0;j<3;j++) {
            string s1=s[j][i-1];
            string s2=s[(j+2)%3][i-1];
            if(s1<s2) s[j][i]=s1+s2;
            else s[j][i]=s2+s1;
            for(int k=0;k<3;k++) {
                t[j][i][k]=t[j][i-1][k]+t[(j+2)%3][i-1][k];
            }
        }
    }
    int q;
    cin >> q;
    for(int x=0;x<q;x++) {
        int N,R,P,S;
        cin >> N >> R >> P >> S;
        int ki=3;
        cout << "CASE #" << x+1 << ": ";
        for(int i=0;i<3;i++) if(R==t[i][N][0] && P==t[i][N][1] && S==t[i][N][2]) ki=i;
        if(ki==3) cout << "IMPOSSIBLE" << endl;
        else cout << s[ki][N] << endl;
    }
    return 0;
}
