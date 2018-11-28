#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cctype>
#define ll long long
#define ld long double
#define sqr(a) (a)*(a)
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define inf (int)1e9
using namespace std;
int t,n=4,z,b,a[20],x;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("A-small-attempt0.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>t;
    for(int q=1;q<=t;q++)
    {
        int k=0;
        for(int i=1;i<17;i++)
            a[i]=0;
        cin>>x;
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
            cin>>z;
            if (i+1==x) a[z]=1;}
        cin>>x;
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
            cin>>z;
            if (i+1==x && a[z]) {k++;b=z;}
        }
        cout<<"Case #"<<q<<": ";
        if (k==1) cout<<b;else
        if (k==0) cout<<"Volunteer cheated!";else
        cout<<"Bad magician!";
        cout<<endl;
    }
    return 0;
}
