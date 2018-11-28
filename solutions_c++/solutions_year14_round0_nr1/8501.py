/* Author : Pranav
BITS PILANI Hyderabad Campus */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
using namespace std;

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define fr(i,n) for(i=0; i<n; i++)
#define N 100005
#define mo 1000000007
#define f first
#define sc(x) scanf("%lld",&x);
#define pr(x) printf("%lld",x);
#define s second
typedef vector<int> vi;
typedef pair <int, int> paint;
typedef long long ll;
vector <long long> a,b;
int main()
{
    ll t,a[10][10],b[10][10],i,j,ans,ans2,res,ct,id=0;
sc(t);
    while(t--){
        ct=0;
        id++;
        sc(ans);
        ans--;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                sc(a[i][j]);
            }
        }
        sc(ans2);
        ans2--;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                sc(b[i][j]);
            }
        }
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                if(a[ans][i]==b[ans2][j]){
                    res=a[ans][i];
                    ct++;
                }
            }
        }
        if(ct==1){
            cout<<"Case #"<<id<<": "<<res<<endl;
        }
        else if(ct>1){
            cout<<"Case #"<<id<<": "<<"Bad magician!\n";
        }
        else{
            cout<<"Case #"<<id<<": "<<"Volunteer cheated!\n";
        }
    }

 return 0;
}


