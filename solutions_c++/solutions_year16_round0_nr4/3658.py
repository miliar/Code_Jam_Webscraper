#include<bits/stdc++.h>

#define llu unsigned long long
#define ll long long
#define pi 3.141592
#define nl printf("\n")
#define f(i,l1,l2) for(i=l1;i<l2;i++)
#define gc getchar_unlocked
#define vi vector<int>
#define vit vi::iterator
#define all(c) c.begin(), c.end()
#define pb push_back
#define endl "\n"
#define mp make_pair
#define CLR(x) memset(x, 0, sizeof x)
#define F first
#define S second
using namespace std;

/*void fin(int &x)
{
int i=0;x=0;
register int c=gc();
while(c<48||c>57)
c=gc();
while(c>47&&c<58)
{
x=(x<<1)+(x<<3) + c-48;
i++;
c=gc();
}
}*/

int c2b(int x, int n)
{

}

int main()
{
    //std::ios::sync_with_stdio(false);
    //cin.tie(0);
    ll int t,i,j,n,m,e;
    cin>>t;
    j = 1;
    while(t--)
    {
    	int k,c,s;
    	cin>>k>>c>>s;
        
    	cout<<"Case #"<<j<<": ";
        f(i,1,k+1)
            cout<<i<<" ";
        cout<<endl;
        j++;
    }

    return 0;
}



