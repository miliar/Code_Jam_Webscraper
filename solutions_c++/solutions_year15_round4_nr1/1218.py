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

int r, c;
int a[105][105];
int s[105][105];

int nexti, nextj;
void getnext( int i, int j, int& dir ) {
    switch(dir) {
        case 1:
            while( i >= 0 ) {
                --i;
                if( i < 0 ) break;
                if( a[i][j] ) {
                    nexti = i;
                    nextj = j;
                    return;
                }
            }
            nexti = -1;
            return;
        case 2:
            while( j < c ) {
                ++j;
                if( j >= c ) break;
                if( a[i][j] ) {
                    nexti = i;
                    nextj = j;
                    return;
                }
            }
            nexti = -1;
            return;
        case 3:
            while( i < r ) {
                ++i;
                if( i >= r ) break;
                if( a[i][j] ) {
                    nexti = i;
                    nextj = j;
                    return;
                }
            }
            nexti = -1;
            return;
        case 4:
            while( j >= 0 ) {
                --j;
                if( j < 0 ) break;
                if( a[i][j] ) {
                    nexti = i;
                    nextj = j;
                    return;
                }
            }
            nexti = -1;
            return;
    }
}

void trace( int ii, int jj ) {
    nexti = ii; nextj = jj;
    int previ, prevj;
    while( 1 ) {
        previ = nexti; prevj = nextj;
        getnext( nexti, nextj, a[nexti][nextj] );
        if( nexti == -1 ) break;
        s[previ][prevj] = 1;
        if( s[nexti][nextj] ) break;
    }
    if( nexti == -1 ) {
        s[previ][prevj] = 2;
    }
}

int ctt;
bool flag;

void trace2( int ii, int jj, int & dir ) {
    //go up
    int x, y;
    if( dir != 1 ) {
        //cout << "GOING UP" << endl;
        x = ii-1, y = jj;
        while( x >= 0 ) {
            if( s[x][y] ) break;
            --x;
        }
        if( x >= 0 ) {
            if( s[x][y] == 1 ) {
                s[ii][jj] = 1;
                ++ctt;
                return;
            }
            else {
                s[ii][jj] = 1;
                s[x][y] = 1;
                ctt += 2;
                return;
            }
        }
    }

    // go right
    if( dir != 2 ) {
            //cout << "GOING right" << endl;
        x = ii, y = jj+1;
        while( y < c ) {
            if( s[x][y] ) break;
            ++y;
        }
        if( y < c ) {
            if( s[x][y] == 1 ) {
                s[ii][jj] = 1;
                ++ctt;
                return;
            }
            else {
                s[ii][jj] = 1;
                s[x][y] = 1;
                ctt += 2;
                return;
            }
        }
    }

    // go down
    if( dir != 3 ) {
            //cout << "GOING down" << endl;
        x = ii+1, y = jj;
        //cout << "X and Y " << x << " " << y << endl;
        while( x < r ) {
            if( s[x][y] ) break;
            ++x;
        }
        if( x < r ) {
            if( s[x][y] == 1 ) {
                s[ii][jj] = 1;
                ++ctt;
                return;
            }
            else {
                s[ii][jj] = 1;
                s[x][y] = 1;
                ctt += 2;
                return;
            }
        }
    }

    // go left
    if( dir != 4 ) {
            //cout << "GOING LEFT" << endl;
        x = ii, y = jj-1;
        while( y >= 0 ) {
            if( s[x][y] ) break;
            --y;
        }
        if( y >= 0 ) {
            if( s[x][y] == 1 ) {
                s[ii][jj] = 1;
                ++ctt;
                return;
            }
            else {
                s[ii][jj] = 1;
                s[x][y] = 1;
                ctt += 2;
                return;
            }
        }
    }

    flag = 1;
}

int main() {
    int t, T, i, j, k, l, m, ans;
    cin >> T;
    char xx;
    for( t = 1; t <= T; ++t ) {
        cin >> r >> c;
        for( i = 0; i < r; ++i ) {
            for( j = 0; j < c; ++j ) {
                cin >> xx;
                if( xx == '^' ) a[i][j] = 1; // up
                else if( xx == '>' ) a[i][j] = 2; // right
                else if( xx == 'v' ) a[i][j] = 3; // down
                else if( xx == '<' ) a[i][j] = 4; // left
                else a[i][j] = 0;
                s[i][j] = 0;
            }
        }
        /*if( t == 68 ) {
            for( i = 0; i < r; ++i ) {
                for( j = 0; j < c; ++j ) {
                    cout << a[i][j] << " ";
                }
                cout << endl;
            }
        }*/
        for( i = 0; i < r; ++i ) {
            for( j = 0; j < c; ++j ) {
                if( a[i][j] != 0 && s[i][j] == 0 ) {
                    trace(i,j);
                    /*cout << "Tracing " << i << " " << j << endl;
                    for( int i = 0; i < r; ++i ) {
                        for( int j = 0; j < c; ++j ) {
                            cout << s[i][j] << " ";
                        }
                        cout << endl;
                    }*/
                }
            }
        }

        ctt = 0;
        flag = 0;
        for( i = 0; i < r; ++i ) {
            for( j = 0; j < c; ++j ) {
                if( s[i][j] == 2 ) {
                    flag = 0;
                    trace2(i,j,a[i][j]);
                    if(flag == 1) break;
                }
            }
            if( flag) break;
        }
        if( flag ) cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        else cout << "Case #" << t << ": " << ctt << endl;
    }
    return 0;
}
