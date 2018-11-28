//AUTOR:MURRUGARRA JEFFRI ERWIN
//UNIVERSIDAD: UNIVERSIDAD NACIONAL DE TRUJILLO
#include <bits/stdc++.h>

#define REP(i, a) for( int i = 0; i < a; i++ )
#define RFOR(i,x,y) for(int i = x; i>= y; i--)
#define FOR(i,x,y) for (int i = x; i < y; i++)
#define ITFOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define VE vector <int>
#define mset(A,x) memset(A, x, sizeof A)
#define PB push_back
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define debug(x) cout <<#x << " = " << x << endl
#define adebug(x,n) cout <<#x<<endl; REP(i,n)cout<<x[i]<<char(i+1==n?10:32)
#define mdebug(x,m,n) cout <<#x<<endl; REP(i,m)REP(j,n)cout<<x[i][j]<<char(j+1==n?10:32)
#define LSOne(S) (S&(-S))

using namespace std;

#define ll long long
#define lli long long int
#define PI acos(-1.0)
#define ii pair<int,int>
#define inf_ll (((1LL<<62)-1)<<1)+1
#define inf_i 1<<30-1

int main(){
/*
   freopen("A-large.in", "r", stdin);
   freopen("A-large.txt", "w", stdout);
*/
char cadg[]={"ZXWUGFVHIO"},cadz[]={"ZERO"},cado[]={"ONE"},cadt[]={"TWO"},cadth[]={"THREE"},cadf[]={"FOUR"},cadfi[]{"FIVE"},cads[]={"SIX"},cadse[]{"SEVEN"},cade[]={"EIGHT"},cadn[]={"NINE"};
map<char,int>freq;
int casos;
scanf("%d",&casos);
cin.ignore();
REP(k,casos)
{
    int val;
    string cad;
    vector<int>re;
    getline(cin,cad);
    REP(i,cad.length())
    {
        freq[cad[i]]++;
    }
    REP(i,strlen(cadg))
    {
        if(freq.count(cadg[i])>0)
        {
            val=freq[cadg[i]];
                    if(cadg[i]=='Z')
                    {
                        REP(j,strlen(cadz))
                        {
                            freq[cadz[j]]-=val;
                        }
                        REP(j,val)
                        {
                            re.push_back(0);
                        }
                    }
                    else if(cadg[i]=='O')
                    {
                        REP(j,strlen(cado))
                        {
                            freq[cado[j]]-=val;
                        }
                        REP(j,val)
                        {
                            re.push_back(1);
                        }
                    }
                     else if(cadg[i]=='W')
                    {
                        REP(j,strlen(cadt))
                        {
                            freq[cadt[j]]-=val;
                        }
                        REP(j,val)
                        {
                            re.push_back(2);
                        }
                    }
                     else if(cadg[i]=='H')
                    {
                        REP(j,strlen(cadth))
                        {
                            freq[cadth[j]]-=val;
                        }
                        REP(j,val)
                        {
                            re.push_back(3);
                        }
                    }
                     else if(cadg[i]=='U')
                    {
                        REP(j,strlen(cadf))
                        {
                            freq[cadf[j]]-=val;
                        }
                        REP(j,val)
                        {
                            re.push_back(4);
                        }
                    }
                     else if(cadg[i]=='F')
                    {
                        REP(j,strlen(cadfi))
                        {
                            freq[cadfi[j]]-=val;
                        }
                        REP(j,val)
                        {
                            re.push_back(5);
                        }
                    }
                     else if(cadg[i]=='X')
                    {
                        REP(j,strlen(cads))
                        {
                            freq[cads[j]]-=val;
                        }
                        REP(j,val)
                        {
                            re.push_back(6);
                        }
                    }
                     else if(cadg[i]=='V')
                    {
                        REP(j,strlen(cadse))
                        {
                            freq[cadse[j]]-=val;
                        }
                        REP(j,val)
                        {
                            re.push_back(7);
                        }
                    }
                    else if(cadg[i]=='G')
                    {
                        REP(j,strlen(cade))
                        {
                            freq[cade[j]]-=val;
                        }
                        REP(j,val)
                        {
                            re.push_back(8);
                        }
                    }
                    else if(cadg[i]=='I')
                    {
                        REP(j,strlen(cadn))
                        {
                            freq[cadn[j]]-=val;
                        }
                        REP(j,val)
                        {
                            re.push_back(9);
                        }
                    }
        }
    }
    sort(all(re));
    cout<<"Case #"<<k+1<<": ";
    REP(i,re.size())
    {
        cout<<re[i];
    }
    cout<<endl;
}

/*
    fclose(stdin);
    fclose(stdout);
*/
    return 0;
}


