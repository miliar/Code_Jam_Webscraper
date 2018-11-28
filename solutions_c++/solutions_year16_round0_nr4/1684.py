#include<iostream>
#include<stdio.h>
#include<string.h>
#include<vector>
#include<queue>
#include<algorithm>
#include<set>
#include<math.h>
#include<map>
using namespace std;

#define mp make_pair
#define pb push_back

long long t,n,k,c,s;

int main()
{
    freopen ("D-small-attempt2.in","r",stdin);
    freopen ("op4-13.out","w",stdout);
    cin>>t;
    for(int cas=1;cas<=t;cas++) {
        cin>>k>>c>>s;
        if(c>k)
            c=k;
        /*
        if( (k+c-1)/c > s) {
            cout<<"Case #"<<cas<<": IMPOSSIBLE\n";
            continue;
        }
        */
        cout<<"Case #"<<cas<<": ";
        /*
        int j=0;
        for(j=0;j<(k/c);j++) {
            long long temp=0;
            for(int i=1;i<c;i++) {
                temp = temp + i*(long long)pow(k,c-i-1) + (c*j)*(long long)pow(k,c-i);
            }
            temp=temp+(c*j)+1;
            cout<<temp<<" ";
        }
        if(k%c!=0) {
            long long temp=0;
            temp=temp+(c*j)*(long long)pow(k,c-1);
            for(int i=1;i<k%c;i++) {
                temp = temp + i*(long long)pow(k,c-i-1) + ((i==(k%c)-1) ? 0 : (c*j)*(long long)pow(k,c-i-1));
            }
            temp=temp+(c*j)+1;
            cout<<temp<<" ";
        }
        */
        for(int i=1;i<=k;i++) {
            cout<<i<<" ";
        }
        cout<<"\n";
    }
}
