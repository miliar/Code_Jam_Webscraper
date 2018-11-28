
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
deque<char>q;
int main()
{
    ios_base::sync_with_stdio(false);
    ll i,j,k,l,m,x,y,r,n,t;
    cin>>t;
    k=1;
    while(t--){
        cin>>s;
        q.clear();
        for(i=0;i<s.length();i++){
            if(q.empty()){
                q.push_front(s[i]);
            }
            else{
                if(s[i]>=q[0]){
                    q.push_front(s[i]);
                }
                else{
                    q.push_back(s[i]);
                }
            }
        }
        cout<<"Case #"<<k<<": ";
        for(i=0;i<s.length();i++){
            cout<<q[i];
        }
        cout<<endl;
        k++;
    }
    return 0;
}
