
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
vector<string> myset;

ll power(ll a, ll b){
    ll res=1;
    while(b>0){
        if(b&1) res=res*a;
        a=a*a;
        b=b/2;
    }
    return res;
}

void check(string s){
    ll i;
    for(i=0;i<s.length();i++){
        if(i==s.length()-1){
            if(s[i]=='1')
                break;
        }
        if(s[i]=='1' && s[i+1]=='1')
            i++;
        else if(s[i]=='1')
            break;
    }
    if(i==s.length()){
        s="11"+s+"11";
        myset.pb(s);
        //cout<<myset.size()<<endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    ll i,j,k,l,m,x,y,r,n,t;
    cin>>t;
    while(t--){
        cin>>n>>k;
        for(i=0;i<power(2,n-4);i++){
            j=0;
            l=i;
            s="";
            while(j<n-4){
                if(l%2==0){
                    s+='0';
                }
                else{
                    s+='1';
                }
                j++;
                l=l/2;
            }
            //cout<<i<<" "<<s<<endl;
            check(s);
            if(myset.size()==k){
                break;
            }
        }
        cout<<"Case #1:"<<endl;
        for(i=0;i<myset.size();i++){
            cout<<myset[i]<<" ";
            for(j=3;j<=11;j++){
                cout<<j<<" ";
            }
            cout<<endl;
        }
    }    
    return 0;
}
