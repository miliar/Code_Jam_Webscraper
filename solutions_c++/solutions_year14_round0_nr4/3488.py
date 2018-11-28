/*
* Author: Ikshu Bhalla
* Language: C++
*/
#include<bits/stdc++.h>
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define vi vector<int>
#define vs vector<string>
#define vvi vector<vector<int> >
#define vpii vector<pair<int,int> >
#define fori(s,e) for(i=s;i<=e;i++)
#define forj(s,e) for(j=s;j<=e;j++)
#define fork(s,e) for(k=s;k<=e;k++)
#define rep(i,s,e) for(int i=s;i<=e;i++)
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define ull unsigned long long
#define ll long long
#define imax INT_MAX
#define imin INT_MIN
#define sz(x) (int)x.size()
#define ln(s) s.length()
#define ppb pop_back
#define max(a,b) (a)>(b)?(a):(b)
#define min(a,b) (a)<(b)?(a):(b)
#define all(x) x.begin(),x.end()
#define mem(x,y) memset(x,y,sizeof(x));
#define pii pair<int,int>
#define psi pair<string,int>
#define in(c,x) scanf("%"#c,&x)
#define out(c,x) printf("%"#c" ",x)
#define aa first
#define bb second
#define Endl endl
using namespace std;
int readint()
{
    int t=0;
    char c,ch;
    ch=getchar();
    if (ch=='-') c=getchar();
    else c=ch;
    while(c<'0' || c>'9')
        c=getchar();
    while(c>='0' && c<='9')
    {
        t=(t<<3)+(t<<1)+c-'0';
        c=getchar();
    }
    if (ch=='-' ) return -t;
    else return t;
}

int main()
{
    ios::sync_with_stdio(false);
    int i,j,k,n,m,t,T;
    freopen("D-large.in","r",stdin);
    freopen("OutDLarge.txt","w",stdout);
    cin>>t;
    T=t;
    while(t--)
    {
        cin>>n;
        double arr[n],brr[n];
        fori(0,n-1) cin>>arr[i];
        fori(0,n-1) cin>>brr[i];
        sort(arr,arr+n);
        sort(brr,brr+n);
        int i=0,j=0;
        int x=0,z=0;
        while(i<n)
        {
            if (upper_bound(brr+j,brr+n,arr[i])!=brr+n)
            {
                j=upper_bound(brr+j,brr+n,arr[i])-brr+1;
                i++;
            }
            else
            {
                z=(n-i);
                break;
            }
        }
        i=n-1,j=n-1;
        while(i>=0&&j>=0)
        {
            if (arr[i]>brr[j])
            {
                i--;
                j--;
                x++;

            }
            else if (arr[i]<brr[j])
            {
                j--;
            }
        }
        cout<< "Case #"<<T-t<< ": ";
        cout<<x<<" "<<z<<endl;
    }
    return 0;
}
