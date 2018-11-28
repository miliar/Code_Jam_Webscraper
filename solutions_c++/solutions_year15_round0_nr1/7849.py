#include<bits/stdc++.h>
#define ll long long

#define read(n) scanf("%d",&n)
#define readLL(n) scanf("%lld",&n)
#define readS(a) scanf("%s",a)

#define pn(n) printf("%d",n)
#define ps() putchar(' ')
#define pl() putchar('\n')

#define rep(i,n) for(int i=0; i<n; i++)
#define fup(i,a,b) for(int i=a; i<=b; i++)
#define fdown(i,a,b) for(int i=a; i>=b; i--)
#define fcond(i,a,cond) for(int i=a; cond; i++)

#define vi vector<int>
#define vvi vector<vector<int> >

using namespace std;


int main()
{
    freopen("input","r",stdin);
    int t;
    read(t);
    for(int j=1; j<=t; j++)
    {
        int smax;
        read(smax);

        int A[smax+1];
        int B[smax+1];

        char str[smax+4];
        readS(str);

        int minFriends = 0;

        for(int i=0; i<=smax; i++)
        {
            A[i] = str[i]-'0';
        }
        B[0] = A[0];
        for(int i=0; i<smax; i++)
        {
            if(B[i] < i+1) {
                minFriends += i+1 - B[i];
                B[i] = i+1;
            }
            B[i+1] = B[i]+A[i+1];
        }
        printf("Case #%d: %d\n",j,minFriends);
    }
    return 0;
}



