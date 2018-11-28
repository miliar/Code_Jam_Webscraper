#include <bits/stdc++.h>
using namespace std;

const int MX=13;

string expand(char S, int level)
{
    if(level==0)
    {
        string res; res.resize(1); res[0]=S;
        return res;
    }

    char C[2];
    if(S=='R')
    {
        C[0]='R';
        C[1]='S';
    }
    else if(S=='P')
    {
        C[0]='P';
        C[1]='R';
    }
    else // S
    {
        C[0]='S';
        C[1]='P';
    }

    string S1=expand(C[0], level-1), S2=expand(C[1], level-1);
    if(S1<S2) return S1+S2;
    else return S2+S1;
}

string expand(string S)
{
    int N=S.size();
    //string R;
    //R.resize(2*N);

    stringstream ss;

    for(int i=0; i<N; i++)
    {
        if(S[i]=='R') ss<<"RS";
        else if(S[i]=='S') ss<<"PS";
        else ss<<"PR";
    }

    return ss.str();
}

int r[MX],p[MX],s[MX];

string solve(int N, int R, int P, int S)
{
    r[N]=R;
    p[N]=P;
    s[N]=S;

    for(int i=N-1; i>=0; i--)
    {


        int sn=p[i+1]+s[i+1]-r[i+1];
        int pn=r[i+1]+p[i+1]-s[i+1];
        int rn=r[i+1]+s[i+1]-p[i+1];

        if(sn<0 || pn <0 || rn <0) return "IMPOSSIBLE";
        assert(sn%2==0 && pn%2==0 && rn%2==0);
        //if(sn%2==1 || pn%2==1 || rn%2==1) return "IMPOSSIBLE"; //(in)sanity?

        s[i]=sn/2;
        p[i]=pn/2;
        r[i]=rn/2;

        //cout << "---" << r[i] << ' ' << p[i] << ' ' << s[i] << endl;
    }

    /*
    string result;
    if(r[0]==1) result="R";
    else if(s[0]==1) result="S";
    else result="P";

    for(int i=1; i<=N; i++) result=expand(result);
    */

    char c;
    if(r[0]==1) c='R';
    else if(p[0]==1) c='P';
    else c='S';

    string result=expand(c, N);

    //int cnt_S=0;
    //int cnt_R=0

    return result;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t=1; t<=T; t++)
    {
        int N, R, P, S;
        cin >> N >> R >> P >> S;
        //int result=solve(N);
        cout << "Case #" << t << ": " << solve(N, R, P, S) << endl;


    }
    return 0;
}
