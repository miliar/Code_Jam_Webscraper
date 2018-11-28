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
    ll t,n,i;
    double time,val,c,f,x;
sc(t);
ll id=0;
    while(t--){
        id++;
        time=0.0;
        cin>>c>>f>>x;
        double num=x*f-2*c-c*f;
        double den=c*f;
        double val=num/den;
        if(val<0){
            n=0;
        }
        else if(val-(int)val==0){
            n=(int)val;
        }
        else{
            n=(int)val+1;
        }
      //  cout<<n<<endl;
        for(i=0;i<n;i++){
       //cout<<c/(double)(i*f+2)<<endl;
            time+=c/double(i*f+2);
        }
        time+=x/(double)(i*f+2);
        cout<<"Case #"<<id<<": ";
        printf("%0.7f\n",time);
        //<<endl;
    }

 return 0;
}

