#include"iostream"
#include"vector"
#include"string"
#include"cstdio"
#include"cstdlib"
#include"cmath"
#include"algorithm"
#include"queue"
#include"cstring"
#include"map"
#include"set"
#include"fstream"
#include"sstream"
#include"numeric"
#include"stack"
#include"iomanip"
#include"bitset"
#include"list"
#include"functional"
#include"utility"
#include"ctime"
#include"cctype"
#include"cassert"
#include"exception"

using namespace std;

typedef long long ll;
const double eps=1e-6;
const int inf=0x3f3f3f3f;
const int hinf=0x3f3f3f3f;
const ll mod=1000000007;

#define fio freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#define fino freopen("input.txt","r",stdin);
#define ms(a,i) memset((a),(i),sz(a))
#define clr(x) memset(x,0,sz(x))
#define cdp(x) memset((x),-1,sizeof(x))
#define infi(x) memset(x,0x3f,sz(x))
#define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    int Case = 0;
    while(T--) {
        int n1 , n2;
        int Card[4];
        int All[4][4];
        cin>>n1;
        for(int i = 0 ; i < 4 ; i ++ )
            for(int j = 0 ; j < 4 ; j ++ )
                cin>>All[i][j];
        for(int i = 0 ; i < 4 ; i ++ )
            Card[i] = All[n1 - 1][i];
        cin>>n2;
        for(int i = 0 ; i < 4 ; i ++ )
            for(int j = 0 ; j < 4 ; j ++ )
                cin>>All[i][j];
        int Count = 0;
        int Ans;
        for(int i = 0 ; i < 4 ; i ++ )
            for(int j = 0 ; j < 4 ; j ++ )
                if(All[n2 - 1][i] == Card[j]) {
                    Count ++ ;
                    Ans = Card[j];
                }
        if(Count == 0)
            printf("Case #%d: Volunteer cheated!\n",++Case);
        else if(Count > 1)
            printf("Case #%d: Bad magician!\n",++Case);
        else
            printf("Case #%d: %d\n",++Case , Ans);
    }
    return 0;
}
