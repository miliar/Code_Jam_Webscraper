#include <bits/stdc++.h>
#define MOD 1000000007
#define INF 1000000000
#define range(a, b, c) (a>=b && a<c)
#define mod(a) (a<0 ? -a : a)
#define stlfor(a, b) for(auto a=b.begin(); a!=b.end(); a++)
#define rstlfor(a, b) for(auto a=b.rbegin(); a!=b.rend(); a++)
#define mp make_pair
#define pb push_back
using namespace std;

void readStrn(char a[], int n)
{
    for(register long i=0; i<n; i++)
        a[i]=getchar();
    getchar();
}

void readStr(char a[], int &n)
{
    n=0;
    for(register char c=getchar(); c>='A' && c<='Z'; c=getchar())
        a[n++]=c;
}

long long readLI()
{
    register char c;
    for(c=getchar(); !(c>='0' && c<='9'); c=getchar());
    register long long a=c-'0';
    for(c=getchar(); c>='0' && c<='9'; c=getchar())
        a=(a<<3)+(a<<1)+c-'0';
    return a;
}

int main()
{
    int T=readLI(), n, ans[10], tmp;
    char a[2000];
    map<char, int> b;
    for(int t=1; t<=T; t++)
    {
        b.clear();
        readStr(a, n);
        for(int i=0; i<n; i++)
            b[a[i]]++;
        tmp = b['Z'];
        ans[0] = tmp;
        b['E'] -= tmp;
        b['R'] -= tmp;
        b['O'] -= tmp;
        tmp = b['W'];
        ans[2] = tmp;
        b['T'] -= tmp;
        b['O'] -= tmp;
        tmp = b['X'];
        ans[6] = tmp;
        b['I'] -= tmp;
        b['S'] -= tmp;
        tmp = b['G'];
        ans[8] = tmp;
        b['E'] -= tmp;
        b['I'] -= tmp;
        b['H'] -= tmp;
        b['T'] -= tmp;
        tmp = b['H'];
        ans[3] = tmp;
        b['E'] -= tmp;
        b['E'] -= tmp;
        b['R'] -= tmp;
        b['T'] -= tmp;
        tmp = b['U'];
        ans[4] = tmp;
        b['F'] -= tmp;
        b['R'] -= tmp;
        b['O'] -= tmp;
        tmp = b['F'];
        ans[5] = tmp;
        b['I'] -= tmp;
        b['V'] -= tmp;
        b['E'] -= tmp;
        tmp = b['V'];
        ans[7] = tmp;
        b['E'] -= 2*tmp;
        b['S'] -= tmp;
        b['N'] -= tmp;
        ans[1] = b['O'];
        ans[9] = b['I'];
        printf("Case #%i: ", t);
        for(int i=0; i<10; i++)
            for(int j=0; j<ans[i]; j++)
                putchar('0' + i);
        putchar('\n');
    }
	return 0;
}
