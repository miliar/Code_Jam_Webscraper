/*
TASK: Getting the Digits
LANG: C++
*/
#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
#define mp(x,y) make_pair((x),(y))
#define pb(x) push_back((x))
#define FOR(i,st,ed) for(int (i)=(st);(i)<(ed);(i)++)
typedef pair<int,int> PII;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long LL;

int N,M,T;
int co[127];
int num[10];
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k;
    int tt=0;
    cin >> T;
    string s;
    while(T--)
    {
        cin >> s;
        memset(num,0,sizeof num);
        memset(co,0,sizeof co);
        for(i=0;i<s.size();i++)
            co[s[i]]++;
        tt++;
        num[0]=co['Z'];
        co['Z']-=num[0];
        co['E']-=num[0];
        co['R']-=num[0];
        co['O']-=num[0];
        num[2]=co['W'];
        co['T']-=num[2];
        co['W']-=num[2];
        co['O']-=num[2];
        num[6]=co['X'];
        co['S']-=num[6];
        co['I']-=num[6];
        co['X']-=num[6];
        num[8]=co['G'];
        co['E']-=num[8];
        co['I']-=num[8];
        co['G']-=num[8];
        co['H']-=num[8];
        co['T']-=num[8];
        num[7]=co['S'];
        co['S']-=num[7];
        co['E']-=num[7];
        co['V']-=num[7];
        co['E']-=num[7];
        co['N']-=num[7];
        num[5]=co['V'];
        co['F']-=num[5];
        co['I']-=num[5];
        co['V']-=num[5];
        co['E']-=num[5];
        num[4]=co['F'];
        co['F']-=num[4];
        co['O']-=num[4];
        co['U']-=num[4];
        co['R']-=num[4];
        num[3]=co['T'];
        co['T']-=num[3];
        co['H']-=num[3];
        co['R']-=num[3];
        co['E']-=num[3];
        co['E']-=num[3];
        num[9]=co['I'];
        co['N']-=num[9];
        co['I']-=num[9];
        co['N']-=num[9];
        co['E']-=num[9];
        num[1]=co['O'];
        printf("Case #%d: ",tt);
        for(i=0;i<10;i++)
            for(j=0;j<num[i];j++)
                printf("%d",i);
        printf("\n");
    }
}
