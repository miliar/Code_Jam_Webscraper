
/************** Elvis Rusnel Capia Quispe ***************/
#include <bits/stdc++.h>
#define f(i,x,y) for (int i = (x); i < (y); i++)
#define fd(i,x,y) for(int i = x; i>= y; i--)
#define FOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define vint vector<int>
#define pii pair<int,int>
#define vpii vector<pii>
#define ll long long
#define clr(A,x) memset(A, x, sizeof A)
#define pb push_back
#define fst first
#define snd second
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define MOD 1000000007
#define INF 1000000000
#define HASH unsigned long long
#define bug1(x) cout<<#x<<" = "<<x<<endl
#define bug2(x,y) cout<<#x<<" = "<<x<<" "<<#y<<" = "<<y<<endl
#define bug3(x,y,z) cout<<#x<<" = "<<x<<" "<<#y<<" = "<<y<<" "<<#z<<" = "<<z<<endl
#define bug4(x,y,z,m) cout<<#x<<" = "<<x<<" "<<#y<<" = "<<y<<" "<<#z<<" = "<<z<<" "<<#m<<" = "<<m<<endl
#define sc(x) scanf("%d",&x)
#define ana(x) cout<<"NO JUST FOR ME"<<endl

using namespace std;
vector<string> pal;
int NN;
string c;
void generar(int pos,int n,string num)
{   if(pos==n)  {   if(NN&1) c = num.substr(0,n - 1);
                    else c = num;
                    reverse(all(num));

                pal.pb(c + num);
                }
    else{
        for(int ini = (pos==0?1:0); ini < 10; ++ini)
           {    char aux  = ini+'0';
                generar(pos + 1,n,num + aux);
            }
    }
}

ll convertir(string aux)
{   ll ans ;
    istringstream cad(aux);
        cad>>ans;
    return ans;
}

bool valid[109999];

int main(){
    freopen("in.c","r",stdin);
    freopen("on.c","w",stdout);

    f(tam,1,10) // hasta solo 13 digitos ya que 100000000000000 no es jajajaj
    {   NN = tam;
        generar(0,(tam + 1) / 2,"");
    }
    //convertir a entero
    vector<ll> numeros;
    f(i,0,pal.size())
    numeros.pb(convertir(pal[i]));

    sort(all(numeros));
    NN = numeros.size();

    f(i,0,NN)
    valid[i] = false;

    f(i,0,NN)
    {   if(cua(numeros[i]) > numeros.back() ) break;
        //buscamos
        int pos = lower_bound(all(numeros),cua(numeros[i])) - numeros.begin();

        if(numeros[pos]==cua(numeros[i])) valid[pos] = true;
    }
    vector<ll> BONITOS;
    f(i,0,NN)
        if(valid[i]) BONITOS.pb(numeros[i]);

    NN = BONITOS.size();
    int tc  , nc = 1;
    ll x,y;
    sc(tc);

    while(tc--)
    {   cin>>x>>y;

        int ans = 0;
        f(i,0,NN)
            if(BONITOS[i] >=x && BONITOS[i]<=y) ++ans;
        printf("Case #%d: %d\n",nc++,ans);
    }

    return 0;
}

