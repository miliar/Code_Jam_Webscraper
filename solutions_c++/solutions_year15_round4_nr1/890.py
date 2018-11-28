//
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;


#define INF 2147483647
#define PI 3.1415926535897932384626433832795
long double eps = 1e-15;

#define all(cont) cont.begin(),cont.end()
#define tr(c, it) for(auto it = c.begin(); it != c.end(); it++)
#define display(c) cout<<endl;tr(c,it)cout<<*it<<' ';cout<<"\n\n";
#define F first
#define S second
#define mp make_pair

typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef double D;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

template<class T> T abs(T x) { return x > 0 ? x : -x; }

//GLOBAL
#define MOD 1000002013
int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0};
#define in(x,y) (((x)>=0) && ((y)>=0) && ((x)<r) && ((y)<c))
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int test_cases,Testno;
    ll i;
    char s[110][110];
    int countt,ii,jj,dir,j,flag;
    int r,c;

    cin>>test_cases;
    for(Testno=1;Testno<=test_cases;Testno++)
    {
        printf("Case #%d: ",Testno);
//___________________________________________
        cin>>r>>c;
        for(i=0;i<r;i++)cin>>s[i];
        countt=0;
//        cout<<endl;
        for(i=0;i<r;i++)for(j=0;j<c;j++)if(s[i][j]!='.'){
//            cout<<i<<j<<endl;
            if(s[i][j]=='^')dir=3;
            if(s[i][j]=='>')dir=0;
            if(s[i][j]=='v')dir=1;
            if(s[i][j]=='<')dir=2;
//            cerr<<'@'<<dir<<' ';
//cerr<<'*';
            for(ii=i,jj=j;;){

//      cerr<<'*';

                ii+=dx[dir];jj+=dy[dir];
//                                                            cout<<ii<<jj<<s[ii][jj];

                if(!in(ii,jj)){
//                        cerr<<'*';

                    flag=0;
                    for(dir=0;dir<4;dir++){
                        ii=i;jj=j;
                        for(;;){
//                                cerr<<'*';

                            ii+=dx[dir],jj+=dy[dir];
                            if(!in(ii,jj))break;
                            if(s[ii][jj]!='.'){flag=1;break;}
                        }
                    }
                    if(flag){countt++;
//                    cout<<i<<j;
                        goto Ld;
                    }
                    else{
                        cout<<"IMPOSSIBLE";
                        goto Done;
                    }
                }
                if(s[ii][jj]!='.'){break;}

            }
            Ld:;
//           cerr<<endl<<'-'<<countt<<endl<<endl;;;
        }
        cout<<countt;
//___________________________________________
        Done: printf("\n");
    }

return 0;
}
