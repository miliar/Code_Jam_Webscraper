#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ULL;
typedef long long LL;
typedef pair<int,int> pii;
typedef pair<pii,pii> ppi;
typedef pair<LL,LL> pll;
typedef pair<string,string> pss;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vii;
typedef vector<LL> vl;
typedef vector<vl> vvl;
typedef vector<string> vstr;
typedef vector<char> vc;
typedef map <int,int> mii;

double PI = acos(-1);

#define REP(i,n) for(int (i) = 0; (i) < (int)(n); (i)++)
#define READ_int(data) scanf("%d",&data);
#define RESET(c,v) memset(c, v, sizeof(c))
#define MAX(a,b) a = max(a,b)
#define MIN(a,b) a = min(a,b)
#define pb push_back
#define mp make_pair
#define ALL(vec) vec.begin(),vec.end()
#define sI(val) scanf("%d",&val)
#define sID(val,val2) scanf("%d %d",&val,&val2)
#define INF 2123123123

inline string IntToString(int a)
{
    char x[100];
    sprintf(x,"%d",a);
    string s = x;
    return s;
}

inline int StringToInt(string a)
{
    char x[100];
    int res;
    strcpy(x,a.c_str());
    sscanf(x,"%d",&res);
    return res;
}

inline string GetString(void)
{
    char x[1000005];
    scanf("%s",x);
    string s = x;
    return s;
}

// FPB gan
int gcd(int  a, int b)
{
    if(b == 0)return a;
    else return gcd(b,a%b);
}

//kpk gan
int lcm(int a,int b)
{
    return (a*(b/gcd(a,b)));
}

bitset<10000010> bs;
vi primes;

// Prima pertama terdapat di primes[1] yah :D
void sieve(LL upperbound)
{
    bs.set();
    bs[0]=bs[1]=0;
    primes.pb(0);
    for(LL i=2; i<=upperbound+1; i++)if(bs[i])
        {
            for(LL j=i*i; j<= upperbound+1; j+=i)bs[j] = 0;
            primes.pb((int) i);
        }
}

int main()
{
    int N,TC;
    sI(TC);

    string huruf = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    REP(a,TC){
        sI(N);

        int data[N+5];

        for(int i = 1; i <= N; i++){
            int temp;
            sI(temp);

            data[i] = temp;
        }

        printf("Case #%d:",a+1);
        while(1){
            int maks = 0;
            int pos1 = 1;
            int pos2 = 0;
            int count1 = 0;
            for(int i = 1; i <= N; i++){
                if( maks < data[i] ){
                    maks = data[i];
                    pos1 = i;
                    pos2 = 0;
                }

                if(maks == data[i]){
                    pos2 = i;
                }

                // Hitung lebih besar dari 0;
                if(data[i] == 1) count1++;
            }

            if(maks == 0){
                printf("\n");
                break;
            }

            printf(" %c",huruf[pos1]);
            data[pos1]--;

            if(pos2 != 0 && count1 != 3){
                printf("%c",huruf[pos2]);
                data[pos2]--;
            }
        }
    }

    return 0;
}
