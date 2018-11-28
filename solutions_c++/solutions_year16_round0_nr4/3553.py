#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#define lli long long int
#define pb push_back
#define mod 1000000007
#define pii pair<int,int>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,k,i,j,c,s,tc=0;
    cin>>t;
    while(t--){
        cin>>k>>c>>s;
        lli x=1;
        for(i=0;i<c-1;i++){
            x=x*k;
        }
        lli ans=1;
        printf("Case #%d: ",++tc);
        for(i=1;i<=s;i++){
            cout<<ans<<" ";
            ans+=x;
        }
        cout<<endl;
    }


    return 0;
}

