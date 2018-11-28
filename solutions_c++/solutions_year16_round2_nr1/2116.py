#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long long LL;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#ifdef DEBUG
    #define cek(x) cout<<x
#else
    #define cek(x) if(false){}
#endif // DEBUG

#define fi first
#define se second
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define EPS 1e-9
#define PI acos(-1.0)
#define pb push_back
#define TC() while(tc--)
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORN(i,n) for(int i=0;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define REPN(i,a,b) for(int i=a;i<=b;i++)
#define reset(a,b) memset(a,b,sizeof(a))
#define sci(x) scanf("%d",&x)
#define scs(x) scanf("%s",&x)

int reduceA(char x) {
    return x - 'A';
}

int main(void){
    freopen("D:/Code/A-large.in","r",stdin);
    freopen("D:/Code/out.txt","w",stdout);

    int tc;
    sci(tc);

    char arr[2010];
    int chara[30];
    int ans[20];



    FOR(i,tc)
    {
        reset(arr,0);
        reset(chara,0);
        reset(ans,0);

        scs(arr);

        FOR(ii,strlen(arr)){
            int cnt = arr[ii]-'A';
            chara[cnt]++;
        }
        //0
        while(chara[reduceA('Z')]>0)
        {
            ans[0]++;
            chara[reduceA('Z')]--;
            chara[reduceA('E')]--;
            chara[reduceA('R')]--;
            chara[reduceA('O')]--;
        }

        //2
        while(chara[reduceA('W')]>0)
        {
            ans[2]++;
            chara[reduceA('T')]--;
            chara[reduceA('W')]--;
            chara[reduceA('O')]--;
        }

        //6
        while(chara[reduceA('X')]>0)
        {
            ans[6]++;
            chara[reduceA('S')]--;
            chara[reduceA('I')]--;
            chara[reduceA('X')]--;
        }

        //4
        while(chara[reduceA('U')]>0)
        {
            ans[4]++;
            chara[reduceA('F')]--;
            chara[reduceA('O')]--;
            chara[reduceA('U')]--;
            chara[reduceA('R')]--;
        }

        //8
        while(chara[reduceA('G')]>0)
        {
            ans[8]++;
            chara[reduceA('E')]--;
            chara[reduceA('I')]--;
            chara[reduceA('G')]--;
            chara[reduceA('H')]--;
            chara[reduceA('T')]--;
        }

        //3
        while(chara[reduceA('R')]>0)
        {
            ans[3]++;
            chara[reduceA('T')]--;
            chara[reduceA('H')]--;
            chara[reduceA('R')]--;
            chara[reduceA('E')]--;
            chara[reduceA('E')]--;
        }

        //5
        while(chara[reduceA('F')]>0)
        {
            ans[5]++;
            chara[reduceA('F')]--;
            chara[reduceA('I')]--;
            chara[reduceA('V')]--;
            chara[reduceA('E')]--;
        }

        //7
        while(chara[reduceA('V')]>0)
        {
            ans[7]++;
            chara[reduceA('S')]--;
            chara[reduceA('E')]--;
            chara[reduceA('V')]--;
            chara[reduceA('E')]--;
            chara[reduceA('N')]--;
        }

        //1
        while(chara[reduceA('O')]>0)
        {
            ans[1]++;
            chara[reduceA('O')]--;
            chara[reduceA('N')]--;
            chara[reduceA('E')]--;
        }

        //9
        while(chara[reduceA('N')]>0)
        {
            ans[9]++;
            chara[reduceA('N')]--;
            chara[reduceA('I')]--;
            chara[reduceA('N')]--;
            chara[reduceA('E')]--;
        }

        cout << "Case #" << i+1 << ": " ;
        FOR(ii,10) {
            FOR(iii,ans[ii]) cout << ii;
        }
        cout << endl;
    }


    return 0;
}
