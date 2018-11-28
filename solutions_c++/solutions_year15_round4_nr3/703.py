// Program and program template by vvneagleone

#include<cstdio>
#include<iostream>
#include<iomanip>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
#include<climits>
#include<vector>
#include<utility>
#include<queue>
#include<set>
#include<map>
using namespace std;
typedef long long LL;
#define MOD 1000000007LL

#ifdef __GNUC__
    #if ( __GNUC__ >= 4 && __GNUC_MINOR__ >= 7 && __cplusplus > 201100L )
        #include<unordered_set>
        #include<unordered_map>
    #endif
#endif // __GNUC__

#ifdef __WIN32
    #define gx getchar
    #define px putchar
    #define ps putchar(' ')
    #define pn putchar('\n')
#else
    #define gx getchar_unlocked
    #define px putchar_unlocked
    #define ps putchar_unlocked(' ')
    #define pn putchar_unlocked('\n')
#endif // __WIN32

void scan(int &n){int sign=1;n=0;char c=gx();while(c<'0'||c>'9'){if(c=='-')sign=-1;c=gx();}while(c>='0'&&c<='9')n=(n<<3)+(n<<1)+c-'0',c=gx();n=n*sign;}
void lscan(LL &n){int sign=1;n=0;char c=gx();while(c<'0'||c>'9'){if(c=='-')sign=-1;c=gx();}while(c>='0'&&c<='9')n=(n<<3)+(n<<1)+c-'0',c=gx();n=n*(LL)(sign);}
int sscan(char a[]){char c=gx();while(c==' '||c=='\n')c=gx();int i=0;while(c!='\n')a[i++]=c,c=gx();a[i]=0;return i;}
int wscan(char a[]){char c=gx();while(c==' '||c=='\n')c=gx();int i=0;while(c!='\n'&&c!=' ')a[i++]=c,c=gx();a[i]=0;return i;}
void print(int n){if(n<0){n=-n;px('-');}int i=10;char o[10];do{o[--i]=(n%10)+'0';n/=10;}while(n);do{px(o[i]);}while(++i<10);}
void lprint(LL n){if(n<0LL){n=-n;px('-');}int i=21;char o[21];do{o[--i]=(n%10LL)+'0';n/=10LL;}while(n);do{px(o[i]);}while(++i<21);}
void sprint(const char*a){const char*p=a;while(*p)px(*p++);}
LL power(LL b,LL e,LL m=MOD){LL r=1;while(e){if(e&1)r=(r*b)%m;b=(b*b)%m;e>>=1;}return r;}
LL minv(LL a,LL m=MOD){LL c,t,q,x,y;c=m;x=0;y=1;while(a>1){q=a/c;t=c;c=a%c;a=t;t=x;x=y-q*x;y=t;}if(y<0)y+=m;return y;}
LL mmul(LL a,LL b,LL m=MOD){LL x=0,y=a%m;while(b){if(b&1)x=(x+y)%m;y=(y<<1)%m;b>>=1;}return x%m;}
LL absll(LL x){if(x<0)return -x;return x;}

int N;

int intersection( unordered_set<string>& x, unordered_set<string>& y ) {
    int ret = 0;
    for( auto it : x ) {
        if( y.find(it) != y.end() ) ++ret;
    }
    return ret;
}

int mark[25];
vector<string> v[25];
int mn;
unordered_set<string> eng, fr, orig;
unordered_map<string,int> enc, frc;
unordered_map<string,int>:: iterator mx;

int glans;

void gen( int i ) {
    if( i == N ) {
        //cout << "At end : glans = " << glans << " mn = " << mn << endl;
        if( glans < mn ) mn = glans;
        return;
    }

    gen(i+1);

    mark[i] = 1;
    // remove from enc
    for( auto it : v[i] ) {
        if( eng.find(it) != eng.end() ) continue;
        mx = enc.find( it );
        --mx->second;
        if(mx->second == 0) {
            if( fr.find(it) != fr.end() ) --glans;
            else if( frc.find(it)->second > 0 ) --glans;
        }
    }
    // add to frc
    for( auto it : v[i] ) {
        if( fr.find(it) != fr.end() ) continue;
        mx = frc.find( it );
        ++mx->second;
        if(mx->second == 1) {
            if( eng.find(it) != eng.end() ) ++glans;
            else if( enc.find(it)->second > 0 ) ++glans;
        }
    }

    gen(i+1);

    mark[i] = 0;
    // remove from frc
    for( auto it : v[i] ) {
        if( fr.find(it) != fr.end() ) continue;
        mx = frc.find( it );
        --mx->second;
        if(mx->second == 0) {
            if( eng.find(it) != eng.end() ) --glans;
            else if( enc.find(it)->second > 0 ) --glans;
        }
    }
    // add to enc
    for( auto it : v[i] ) {
        if( eng.find(it) != eng.end() ) continue;
        mx = enc.find( it );
        ++mx->second;
        if(mx->second == 1) {
            if( fr.find(it) != fr.end() ) ++glans;
            else if( frc.find(it)->second > 0 ) ++glans;
        }
    }
}

int main() {
    int t, T, i, j, k, l, m, anss;
    cin >> T;
    for( t = 1; t <= T; ++t ) {
        cin >> N;
        char ch;
        scanf("%c",&ch);

        eng.clear(); fr.clear();

        string str, k;
        getline(cin,str);
        for( j = 0; j < str.size(); ++j ) {
            if( str[j] == ' ' ) {
                eng.insert(k);
                k.clear();
            }
            else k += str[j];
        }
        eng.insert(k);

        str.clear(); k.clear();
        getline(cin,str);
        for( j = 0; j < str.size(); ++j ) {
            if( str[j] == ' ' ) {
                fr.insert(k);
                k.clear();
            }
            else k += str[j];
        }
        fr.insert(k);

        N -= 2;
        for( i = 0; i < N; ++i ) {
            str.clear(); k.clear();
            getline(cin,str);
            v[i].clear();
            for( j = 0; j < str.size(); ++j ) {
                if( str[j] == ' ' ) {
                    v[i].push_back(k);
                    k.clear();
                }
                else k += str[j];
            }
            v[i].push_back(k);
        }

        enc.clear(); frc.clear();
        for( j = 0; j < N; ++j ) {
            for( auto it : v[j] ) {
                enc.insert(make_pair(it,0));
                frc.insert(make_pair(it,0));
            }
        }
        anss = intersection( eng, fr );

/*cout << "English : " << endl;
for( auto it : eng ) cout << it << " ";
cout << endl << endl;
cout << "French : " << endl;
for( auto it : fr ) cout << it << " ";
cout << endl << endl;*/


        // set start
        glans = 0;
        for( i = 0; i < N; ++i ) {
            for( auto it : v[i] ) {
                //cout << "Checking " << it << endl;
                if( eng.find(it) != eng.end() ) continue;
                mx = enc.find( it );
                //if( mx == enc.end() ) cout << "WTF HAPPENED" << endl;
                fflush(stdout);
                ++mx->second;
                if(mx->second == 1) {
                    if( fr.find(it) != fr.end() ) {
                        ++glans;
                        //cout << "In french original" << endl;
                    }
                    else if( frc.find(it)->second > 0 ) {
                        ++glans;
                        //cout << "In french new" << endl;
                    }
                }
            }
        }
        //cout << "GLANS " << glans << endl;

        mn = INT_MAX;
        for( i = 0; i < N; ++i ) mark[i] = 0;
        gen(0);

        //cout << "anss " << anss << " mn " << mn << endl;
        cout << "Case #" << t << ": " << anss + mn << endl;
    }
    return 0;
}
