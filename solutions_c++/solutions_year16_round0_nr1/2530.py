
/*    Challenge yourself with something you know you could never do, 
        and what you’ll find is that you can overcome anything        */

#include<bits/stdc++.h>
using namespace std;
#define ll long long 
#define MAX 200005
#define N 1000000007
#define pb push_back
#define MIN 5005
#define imax 2000000200
#define llmax 1000000002000000000ll
#define PI 3.141592653589793
#define eps 1e-9
#define F first
#define S second
#define vi vector<int>
#define vl vector<ll>

ll a[MAX];
string s,p;

int main()
{
    ios_base::sync_with_stdio(false);
    ll i,j,k,l,m,x,y,r,n,t;
    j=1;
    cin>>t;
    while(t--){
        cin>>n;
        if(n==0){
            cout<<"Case #"<<j<<": INSOMNIA"<<endl;
            j++;
            continue;
        }
        set<ll>myset;
        i=1;
        while(1){
            k=i*n;
            while(k>0){
                myset.insert(k%10);
                k=k/10;
            }
            if(myset.size()==10)
            break;
            i++;
        }
        ll msd=i*n;
        cout<<"Case #"<<j<<": "<<msd<<endl;
        j++;
    }
    return 0;
}
