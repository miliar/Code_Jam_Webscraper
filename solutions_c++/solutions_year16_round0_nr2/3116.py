#include<bits/stdc++.h>
#include <cstring>

#define mod 1000000007
#define inf 1000000009
#define MX 501

#define pb push_back
#define mp make_pair
#define ll long long
#define gc getchar
#define vi vector<int>
#define rep(i, n) for(int i=0; i<n; i++)

using namespace std;
char s[101];

int n, d[1027];
int cmask(int,int);
int Sol(int m)
{
    //if(m>1023) return 0;
    if(d[m]!=-1) return d[m];
    int b, a=inf;
    for(int I=0; I<n; I++)
    {
        b=cmask(m, I);
        printf("%d\n", b);
        if(b!=m)
        { b=Sol(b); if(a>b) a=b; }
    }
    printf("%d %d\n", m, a+1);
    d[m]=a+1;
    return a+1;
}

int cmask(int m, int I)
{
    bool b1, b2;
    for(int j=0; j<I/2; j++)
    {
        b1=!(m&(1<<j));
        b2=!(m&(1<<(I-j)));
        if(b1==b2)
        {
            m^=(1<<j);
            m^=(1<<(I-j));
        }
    }
    m^=(1<<(I/2));
    return m;
}

int main() {
	#ifndef ONLINE_JUDGE
    freopen("C:\\Users\\yashvir\\Downloads\\B-large.in","r",stdin);
    //freopen("C:\\Users\\yashvir\\Downloads\\B-small-attempt0.in","r",stdin);
    //freopen("in.txt","r",stdin);
    freopen("out.txt", "w", stdout);
    #endif // ONLINE_JUDGE
    int t, a, j, I, ans;
    char p;
    memset(d, -1, sizeof d);
    d[0]=0;
    scanf("%d", &t);
    for(I=1; I<=t; I++)
    {
         scanf("%s", s);
         p=s[0];
         ans=0;
         for(j=1; s[j]; j++)
         if(s[j]!=p) { ans++; p=s[j]; }
         if(s[j-1]=='-') ans++;
         //n=j;
         //printf("%d\n", a);
         //d[(1<<n)-1]=1;
         printf("Case #%d: %d\n", I, ans);
    }

    return 0;
}
