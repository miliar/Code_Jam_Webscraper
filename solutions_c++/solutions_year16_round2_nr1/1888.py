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
    int T;

    sI(T);

    REP(a,T){
        string temp = GetString();

        int sizey = temp.size();
        map <char,int> frequency;
        REP(b, sizey){
            frequency[temp[b]]++;
        }

        string hasil = "";

        // Check 0
        if(frequency['Z'] > 0){
            int ukuran = frequency['Z'];
            for(int i = 1; i <= ukuran; i++){
                hasil = hasil + '0';
                frequency['Z']--;
                frequency['E']--;
                frequency['R']--;
                frequency['O']--;
            }
        }

        // Check 8
        if(frequency['G'] > 0){
            int ukuran = frequency['G'];
            for(int i = 1; i <= ukuran; i++){
                hasil = hasil + '8';
                frequency['E']--;
                frequency['I']--;
                frequency['G']--;
                frequency['H']--;
                frequency['T']--;
            }
        }

         // Check 6
        if(frequency['X'] > 0){
            int ukuran = frequency['X'];
            for(int i = 1; i <= ukuran; i++){
                hasil = hasil + '6';
                frequency['S']--;
                frequency['I']--;
                frequency['X']--;
            }
        }

        // Check 4
        if(frequency['U'] > 0){
            int ukuran = frequency['U'];
            for(int i = 1; i <= ukuran; i++){
                hasil = hasil + '4';
                frequency['F']--;
                frequency['O']--;
                frequency['U']--;
                frequency['R']--;
            }
        }

        // Check 2
        if(frequency['W'] > 0){
            int ukuran = frequency['W'];
            for(int i = 1; i <= ukuran; i++){
                hasil = hasil + '2';
                frequency['T']--;
                frequency['W']--;
                frequency['O']--;
            }
        }

        // Check 7
        if(frequency['S'] > 0){
            int ukuran = frequency['S'];
            for(int i = 1; i <= ukuran; i++){
                hasil = hasil + '7';
                frequency['S']--;
                frequency['E']--;
                frequency['V']--;
                frequency['E']--;
                frequency['N']--;
            }
        }

        // Check 5
        if(frequency['F'] > 0){
            int ukuran = frequency['F'];
            for(int i = 1; i <= ukuran; i++){
                hasil = hasil + '5';
                frequency['F']--;
                frequency['I']--;
                frequency['V']--;
                frequency['E']--;
            }
        }

        // Check 3
        if(frequency['H'] > 0){
            int ukuran = frequency['H'];
            for(int i = 1; i <= ukuran; i++){
                hasil = hasil + '3';
                frequency['T']--;
                frequency['H']--;
                frequency['R']--;
                frequency['E']--;
                frequency['E']--;
            }
        }

        // Check 1
        if(frequency['O'] > 0){
            int ukuran = frequency['O'];
            for(int i = 1; i <= ukuran; i++){
                hasil = hasil + '1';
                frequency['O']--;
                frequency['N']--;
                frequency['E']--;
            }
        }

        // Check 9
        if(frequency['I'] > 0){
            int ukuran = frequency['I'];
            for(int i = 1; i <= ukuran; i++){
                hasil = hasil + '9';
                frequency['N']--;
                frequency['I']--;
                frequency['N']--;
                frequency['E']--;
            }
        }

        sort(ALL(hasil));
        printf("Case #%d: %s\n",a+1,hasil.c_str());
    }

    return 0;
}
