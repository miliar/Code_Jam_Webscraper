#include<bits/stdc++.h>
#include <stdio.h>
#include <conio.h>

//#include <ext/hash_map>
using namespace std;
//using namespace __gnu_cxx;

#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define loop(it, c) for (__typeof(c.begin()) it = c.begin(); it != c.end(); ++it)
#define fill(a, b) memset(a, b, sizeof(a))
#define present(container, element) (container.find(element) != container.end())
#define cpresent(container, element) (find(all(container),element) != container.end())
#define pb push_back
#define mp make_pair
#define rep(a,b) for(int i=a;i<b;i++)
#define bit(x) __builtin_popcountll(x)
#define S(x) (((long long)log10(x)) + 1)
#define ll long long
#define endn "\n"
typedef long long LL;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef vector<string> vs;

const double pi = 2*acos(0.0);
const string alphabetU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const string alphabetL = "abcdefghijklmnopqrstuvwxyz";
const double EPS = 1e-9;
const int INF = 1 << 28;
const long long INFL = 1LL << 62;
const double INFD = 1e+20;

/*********************************************************I/O******************************************************************/
int in(){int r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}
int inl(){LL r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}
string ins(){string s;while(!feof(stdin)){char c = fgetc(stdin);if(c == 13) continue;if(c == 10) return s;s += c;}return s;}
/********************************************************End I/O*****************************************n*********************/
void getline(char* entry){char c;string s;while((c=getchar())!='\n')s+=c;strcpy(entry,s.c_str());}
int toi(string x){
    int z;
    istringstream iss(x);
    iss>>z; return z;
}

int modulo ( int m, int n) { return m >= 0 ? m % n : ( n - abs ( m%n ) ) % n; }


int  main(){

    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int cases,def,clap_now,num;
    string adu;
    cin>>cases;
    for(int c=1;c<=cases;c++){
        def=clap_now=0;
        cin>>num>>adu;
        for(int i=0;i<=num;i++){
            if(clap_now<i){
                def+=i-clap_now;
                clap_now+=i-clap_now;
            }
            clap_now+=adu[i]-'0';
        }
        cout<<"Case #"<<c<<": "<<def<<endl;
    }
    return 0;
}
