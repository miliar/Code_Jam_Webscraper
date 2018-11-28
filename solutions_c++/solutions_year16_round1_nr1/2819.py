#include <bits/stdc++.h>
#define ll long long int
#define s(a) scanf("%lld", &a);
#define pb push_back
#define mp make_pair
#define f first
#define sc second
#define inf 10e16

using namespace std;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll t,n,i,j,k,l;
    s(t);
    for(ll tt=1;tt<=t;tt++) {
        char a[1111];
        scanf("%s",a);
        deque<char>q;
        q.push_back(a[0]);
        l=strlen(a);
        for(i=1;i<l;i++) {
            if(q.front()<=a[i]) {
                q.push_front(a[i]);
            }
            else {
                q.push_back(a[i]);
            }
        }
        cout<<"Case #"<<tt<<": ";
        while(!q.empty()) {
            cout<<q.front();
            q.pop_front();
        }
        cout<<endl;
    }
    return 0;
}
