
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

void fun(ll x, ll y){
    //cout<<x<<" "<<y<<endl;
    //cout<<s<<endl;
    for(ll i=x;i<=y;i++){
        if(s[i]=='+') s[i]='-';
        else s[i]='+';        
    }
    //cout<<s<<endl;
    while(x<y){
        swap(s[x],s[y]);
        x++;
        y--;
    }
    //cout<<s<<endl;
}
ll cnt(ll x){
    ll ct=0;
    for(ll i=0;i<=x;i++){
        if(s[i]=='+')
        ct++;
        else break;
    }
    return ct;
}
int main()
{
    ios_base::sync_with_stdio(false);
    ll i,j,k,l,m,x,y,r,n,t;
    k=1;
    cin>>t;
    while(t--){
        cin>>s;
        ll msd=0;
        for(i=s.length()-1;i>=0;i--){
            if(s[i]=='+'){
                continue;
            }
            else{
                if(s[0]=='+'){
                    j=cnt(i);
                    fun(0,j-1);
                    msd++;
                    fun(0,i);
                    msd++;
                }
                else{
                    fun(0,i);
                    msd++;
                }
            }
        }
        cout<<"Case #"<<k<<": "<<msd<<endl;
        k++;
    }    
    return 0;
}
