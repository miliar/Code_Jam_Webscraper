
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
    cin>>t;
    k=1;
    while(t--){
        cin>>s;
        //cout<<s<<endl;
        ll cnt[26];
        vector<ll>v;
        v.clear();
        for(i=0;i<26;i++){
            cnt[i]=0;
        }
        for(i=0;i<s.length();i++){
            cnt[s[i]-65]++;
            if(s[i]=='Z'){
                v.pb(0);
            }
            if(s[i]=='W'){
                v.pb(2);
            }
            if(s[i]=='U'){
                v.pb(4);
            }
            if(s[i]=='X'){
                v.pb(6);
            }
            if(s[i]=='G'){
                v.pb(8);
            }
        }
        ll one=0,sev=0;
        for(i=0;i<(cnt[14]-cnt[25]-cnt[22]-cnt[20]);i++){
            v.pb(1);
            one++;
        }
        for(i=0;i<cnt[18]-cnt[23];i++){
            v.pb(7);
            sev++;
        }
        for(i=0;i<cnt[7]-cnt[6];i++){
            v.pb(3);
        }
        for(i=0;i<cnt[5]-cnt[20];i++){
            v.pb(5);
        }
        for(i=0;i<(cnt[13]-one-sev)/2;i++){
            v.pb(9);
        }
        //cout<<one<<sev<<endl;
        cout<<"Case #"<<k<<": ";
        sort(v.begin(),v.end());
        for(i=0;i<v.size();i++)
            cout<<v[i];
        cout<<endl;
        k++;
    }
    return 0;
}
