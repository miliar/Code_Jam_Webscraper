#include<stdio.h>
#include<iostream>
#include<vector>
#include<cstdlib>
#include<cstring>
#include<math.h>
#include<map>
#include<algorithm>
#include<queue>
#include<string>
#include<climits>
#include<bitset>
#include<set>
#include<functional>

using namespace std;
typedef long long int LL;

#ifdef _WIN32
#define gx getchar
#define px putchar
#define ps putchar(' ')
#define pn putchar('\n')
#else
#define gx getchar_unlocked
#define px putchar_unlocked
#define ps putchar_unlocked(' ')
#define pn putchar_unlocked('\n')
#endif

//input
void scan(int &n)
{
    int sign = 1;
    n = 0;
    char c = gx();
    while( c < '0' || c > '9' )
    {
        if( c == '-' ) sign = -1;
        c = gx();
    }
    while( c >= '0' && c <= '9' ) n = (n<<3) + (n<<1) + c - '0', c = gx();  n = n * sign;
}
void lscan(LL &n)
{
    int sign = 1;
    n = 0;
    char c = gx();
    while( c < '0' || c > '9' )
    {
        if( c == '-' )
        sign = -1;
        c = gx();
    }
    while( c >= '0' && c <= '9' ) n = (n<<3) + (n<<1) + c - '0', c = gx();  n = n * (LL)(sign);
}
int sscan(char a[])
{
    char c = gx();
    while(c==' ' || c=='\n') c=gx();
    int i=0;
    while(c!='\n')a[i++] = c,c=gx();
    a[i]=0;
    return i;
}
int wscan(char a[])
{
    char c = gx();
    while(c==' ' || c=='\n') c=gx();
    int i=0;
    while(c!='\n' && c!=' ')a[i++] = c,c=gx();
    a[i]=0;
    return i;
}

//output
void print(int n)
{
    if(n<0)
    {
        n=-n;
        px('-');
    }
    int i=10;
    char o[10];
    do{o[--i] = (n%10) + '0'; n/=10;}while(n);
    do{px(o[i]);}while(++i<10);
}
void lprint(LL n)
{
    if(n<0LL)
    {
        n=-n;
        px('-');
    }
    int i=21;
    char o[21];
    do{o[--i] = (n%10LL) + '0'; n/=10LL;}while(n);
    do{px(o[i]);}while(++i<21);
}
void sprint(const char a[])
{
    const char *p=a;
    while(*p)px(*p++);
}


typedef pair<int, int> pii;
typedef pair<LL, LL> pll;

const LL MOD = 1000000007LL;
const int SIZ = 1000001;

LL pow(LL a, LL b, LL m)
{
	LL x=1,y=a;
	while(b > 0)
	{
		if(b%2 == 1)
		{
			x=(x*y);
			if(x>m) x%=m;
		}
		y = (y*y);
		if(y>m) y%=m;
		b /= 2;
	}
	return x;
}

int mat[5][5];
int sign[5][5];
int mat1[5][5];

int main()
{
    mat[1][1] = 1;
    mat[1][2] = 2;
    mat[1][3] = 3;
    mat[1][4] = 4;
    
    mat[2][1] = 2;
    mat[2][2] = 1;
    mat[2][3] = 4;
    mat[2][4] = 3;
    
    mat[3][1] = 3;
    mat[3][2] = 4;
    mat[3][3] = 1;
    mat[3][4] = 2;
    
    mat[4][1] = 4;
    mat[4][2] = 3;
    mat[4][3] = 2;
    mat[4][4] = 1;
    
    
    
    sign[1][1] = 0;
    sign[1][2] = 0;
    sign[1][3] = 0;
    sign[1][4] = 0;
    
    sign[2][1] = 0;
    sign[2][2] = 1;
    sign[2][3] = 0;
    sign[2][4] = 1;
    
    sign[3][1] = 0;
    sign[3][2] = 1;
    sign[3][3] = 1;
    sign[3][4] = 0;
    
    sign[4][1] = 0;
    sign[4][2] = 0;
    sign[4][3] = 1;
    sign[4][4] = 1;
    
    mat1[1][1] = 1;
    mat1[1][2] = 2;
    mat1[1][3] = 3;
    mat1[1][4] = 4;
    
    mat1[2][1] = 2;
    mat1[2][2] = -1;
    mat1[2][3] = 4;
    mat1[2][4] = -3;
    
    mat1[3][1] = 3;
    mat1[3][2] = -4;
    mat1[3][3] = -1;
    mat1[3][4] = 2;
    
    mat1[4][1] = 4;
    mat1[4][2] = 3;
    mat1[4][3] = -2;
    mat1[4][4] = -1;
    
    
    int t,i,j,k,x,z,l,n,flag,q;
    string s,y;
    
    scan(t);
    for(int xx=1;xx<=t;xx++)
    {
        s.clear();
        y.clear();
        scan(l);
        scan(x);
        cin >> y;
        for(i=0;i<x;i++)
        {
            s += y;
        }
        n = l*x;
        for(i=0;i<n;i++)
        {
            if(s[i]=='i') s[i] = 2;
            if(s[i]=='j') s[i] = 3;
            if(s[i]=='k') s[i] = 4;
        }
        int a[n+1];
        int sn[n+1];
        a[0] = s[0];
        sn[0] = 0;
        //cout << sn[0] <<  " ";
        for(i=1;i<n;i++)
        {
            a[i] = mat[a[i-1]][s[i]];
            sn[i] = sn[i-1] + sign[a[i-1]][s[i]];
            //cout << sn[i] << " ";
        }
        //pn;
        flag = 0;
        
        x = n-2;
        z = n-1;
        
        if(n < 3)
        {
            printf("Case #%d: ",xx);
            cout << "NO" << endl;
            continue;
        }
        int c,temp;
        for(i=0;i<x;i++)
        {
            if( (sn[i]%2) != 0) continue;
            if(a[i]!=2) continue;
            if(flag) break;
            for(j=i+1;j<z;j++)
            {
                if(mat[a[i]][3] != a[j]) continue;
                c = sn[j] - sn[i];
                temp = a[j];
                if(c&1) temp *= -1;
                if( mat1[a[i]][3] != temp) continue;
                
                if(mat[a[j]][4] != a[n-1]) continue;
                c = sn[n-1] - sn[j];
                temp = a[n-1];
                if(c&1) temp *= -1;
                if( mat1[a[j]][4] != temp) continue;
                
                //cout << i << " " << j << endl;
                flag = 1;
                break;
            }
        }
        
        printf("Case #%d: ",xx);
        if(flag) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    
    return 0;
}
