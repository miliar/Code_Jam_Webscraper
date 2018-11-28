/*
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        ;;                                                             ;;
        ;;      -----------------------------------------------        ;;
        ;;      -----------------------------------------------        ;;
        ;;           |\    | | |       .-----. \     /                 ;;
        ;;           | \   | | |       |     |  \   /                  ;;
        ;;           |  \  | | |       |     |   \ /                   ;;
        ;;           |   \ | | |       |     |    |                    ;;
        ;;           |    \| | |______ |_____|    |                    ;;
        ;;      ------------------------------------------------       ;;
        ;;      ------------------------------------------------       ;;
        ;;                                                             ;;
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
*/
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<climits>
#include<cfloat>
#include<ctime>
#include<cassert>
#include<map>
#include<utility>
#include<set>
#include<iostream>
#include<memory>
#include<string>
#include<vector>
#include<algorithm>
#include<functional>
#include<sstream>
#include<complex>
#include<stack>
#include<queue>
#include<numeric>
#include<list>
#include<iomanip>
#include<fstream>
#include<locale>
#include<clocale>
#include<limits>

#define MX 20000
#define inf 1E20
#define PB push_back
#define vsort(v) sort(v.begin(),v.end())
#define loop(i,n) for(i=0;i<n;i++)
#define loop1(i,n) for(i=1;i<=n;i++)
#define rloop(i,n) for(i=n-1;i>=0;i--)
#define rloop1(i,n) for(i=n;i>=1;i--)
#define vloop(i,k,n) for(i=k;i<=n;i++)
#define rvloop(i,k,n) for(i=n;i>=k;i--)
#define SI(n) scanf("%d",&n);
#define SL(n) scanf("%lld",&n);
#define SD(n) scanf("%lf",&n);
#define WI(n) while(scanf("%d",&n))
#define WD(n) while(scanf("%lf",&n))
#define WIb(n) while(scanf("%d",&n) && n)
#define WDb(n) while(scanf("%lf",&n) && n)
#define WS(n) while(getline(cin,n))
#define s(k) k.size()

using namespace std;
string S[6];
int main()
{
    ofstream fout ("codejamout.out");
    ifstream fin ("codejamin.in");
    int test,kase,i,j,o,x,t,ans;
    fin>>test;
    for(kase=1; kase<=test; kase++)
    {
        bool say=false;
        ans=0;
        for(i=0; i<4; i++)
        {
            fin>>S[i];
            o=0;
            t=0;
            x=0;
            for(j=0; j<4; j++)
            {
                if(S[i][j]=='.') say=true;
                else if(S[i][j]=='X') x++;
                else if(S[i][j]=='O') o++;
                else t++;
            }
            if(o==4 || (o==3 && t==1)) ans=1;
            else if(x==4 || (x==3 && t==1)) ans=2;
        }
        if(ans==1) fout<<"Case #"<<kase<<": "<<"O won"<<endl;
        else if(ans==2) fout<<"Case #"<<kase<<": "<<"X won"<<endl;
        else
        {
            for(j=0; j<4; j++)
            {
                o=0;
                t=0;
                x=0;
                for(i=0; i<4; i++)
                {
                    if(S[i][j]=='.') say=true;
                    else if(S[i][j]=='X') x++;
                    else if(S[i][j]=='O') o++;
                    else t++;
                }
                if(o==4 || (o==3 && t==1)) ans=1;
                else if(x==4 || (x==3 && t==1)) ans=2;
            }
            if(ans==1) fout<<"Case #"<<kase<<": "<<"O won"<<endl;
            else if(ans==2) fout<<"Case #"<<kase<<": "<<"X won"<<endl;
            else
            {
                x=0;
                o=0;
                t=0;
                for(i=0; i<4; i++)
                {
                    if(S[i][i]=='.') say=true;
                    else if(S[i][i]=='X') x++;
                    else if(S[i][i]=='O') o++;
                    else t++;
                }
                if(o==4 || (o==3 && t==1)) ans=1;
                else if(x==4 || (x==3 && t==1)) ans=2;
                if(ans==1) fout<<"Case #"<<kase<<": "<<"O won"<<endl;
                else if(ans==2) fout<<"Case #"<<kase<<": "<<"X won"<<endl;
                else
                {
                    x=0;
                    o=0;
                    t=0;
                    j=3;
                    for(i=0; i<4; i++)
                    {
                        if(S[i][j]=='.') say=true;
                        else if(S[i][j]=='X') x++;
                        else if(S[i][j]=='O') o++;
                        else t++;
                        j--;
                    }
                    if(o==4 || (o==3 && t==1)) ans=1;
                    else if(x==4 || (x==3 && t==1)) ans=2;
                    if(ans==1) fout<<"Case #"<<kase<<": "<<"O won"<<endl;
                    else if(ans==2) fout<<"Case #"<<kase<<": "<<"X won"<<endl;
                    else if(say) fout<<"Case #"<<kase<<": "<<"Game has not completed"<<endl;
                    else fout<<"Case #"<<kase<<": "<<"Draw"<<endl;
                }
            }
        }
    }
    return 0;
}
