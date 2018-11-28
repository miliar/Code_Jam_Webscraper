#include <fstream>
#include <cstring>
#include <map>
#include <cstdio>
#define LM 4010
#define DM 20
#define INF 0x3f3f3f3f

using namespace std;

ifstream dic("dictionary.txt");
ifstream f("test.in");
ofstream g("test.out");

int T, TI;
int N;
string S;
string d;
map<long long, int> Map;
int DP[LM][LM];

void Precalc ()
{
    int NR=521196;
    int i, j, k, l;
    long long Code;

    for (; NR>=1; NR--)
    {
        dic >> d;
        l=d.size();
        d=' '+d;
        Code=0;

        for (i=1; i<=l; i++)
            Code=1LL*Code*29+d[i]-'a'+1;
        Map[Code]++;

        for (j=1; j<=l; j++)
        {
            Code=0;
            for (i=1; i<=l; i++)
            {
                Code=1LL*Code*29;
                if (i==j)
                    Code+=1LL*28;
                else
                    Code+=1LL*d[i]-'a'+1;
            }
            Map[Code]++;
        }
        for (j=1; j<=l; j++)
            for (k=j+5; k<=l; k++)
            {
                Code=0;
                for (i=1; i<=l; i++)
                {
                    Code=1LL*Code*29;
                    if (i==j || i==k)
                        Code+=1LL*28;
                    else
                        Code+=1LL*d[i]-'a'+1;
                }
                Map[Code]++;
            }
    }

    dic.close();
}

int Solve ()
{
    int i, j, k, l, mod, s , e, last;

    long long Code;
    memset(DP, INF, sizeof(DP));
    DP[0][0]=0;

    f >> S;
    N=S.size();
    S=' '+S;

    for (s=0; s<N; s++)
        for (last=0; last<=s; last++)
        for (e=s+1; e<=s+11 && e<=N; e++)
        {
            l=e-s;

            Code=0;
            for (i=s+1; i<=e; i++)
                Code=1LL*Code*29+S[i]-'a'+1;

            if (Map[Code]!=0)
            {
                DP[e][last]=min(DP[e][last], DP[s][last]);
                continue;
            }

            bool ok=0;
            for (j=s+1; j<=e; j++)
            {
                Code=0;
                for (i=s+1; i<=e; i++)
                {
                    Code=1LL*Code*29;
                    if (i==j)
                        Code+=1LL*28;
                    else
                        Code+=1LL*S[i]-'a'+1;
                }
                if (Map[Code]!=0 && (j-last>4 || last==0))
                {
                    DP[e][j]=min(DP[e][j], 1+DP[s][last]);
                    //ok=1;
                    //break;
                }
            }
            //if (ok) continue;
            ok=0;

            for (j=s+1; j<=e; j++)
                for (k=j+5; k<=e; k++)
                {
                    Code=0;
                    for (i=s+1; i<=e; i++)
                    {
                        Code=1LL*Code*29;
                        if (i==j || i==k)
                            Code+=1LL*28;
                        else
                            Code+=1LL*S[i]-'a'+1;
                    }
                    if (Map[Code]!=0 && (j-last>4 || last==0))
                    {
                        DP[e][k]=min(DP[e][k], 2+DP[s][last]);
                        //ok=1;
                        //break;
                    }
                }
        }

    int ANS=INF;
    for (i=0; i<=N; i++)
        ANS=min(ANS, DP[N][i]);

    return ANS;
}


int main ()
{
    Precalc();

    f >> T;
    for (TI=1; TI<=T; TI++)
    {
        g << "Case #" << TI << ": ";
        g << Solve() << '\n';
    }

    f.close();
    g.close();

    return 0;
}

