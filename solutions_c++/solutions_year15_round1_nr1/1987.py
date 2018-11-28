#include<queue>
#include<stack>
#include<string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <sstream>
#include<map>
#include<set>
#include<cstring>
#include <ctime>
#include<iostream>
#include<fstream>
using namespace std;
#define sz     size()
#define pb push_back
#define mp make_pair
#define fo(i, n) for ( i = 1; i <= (int)(n); i++)
#define fr(i, k, n) for ( i = k; i <= (int)(n); i++)
#define sortvektor(s)   sort((s).begin(),(s).end())
#define reversevektor(s)   reverse((s).begin(),(s).end())
#define fro(i, n) for ( i = 0; i < (int)(n); i++)
#define meset(x,y) memset((x),(y),sizeof((x)))
long long stoll (string target) { stringstream s; s << target; long long w; s >> w; return w;}
int stoi (string target) { stringstream s; s << target; int w; s >> w; return w;}
string itos (int i) {stringstream s; s << i; return s.str();}
string lltos (long long i) {stringstream s; s << i; return s.str();}


int main()
{
ios::sync_with_stdio(false); //

  freopen("input.txt","r",stdin);

bool ok=true,final=false;
int i,j,k,n,m; int t;
int pom,mom,g,f;
int odgovor,br;
int a[10001];
bool b[1001];
   freopen("output.txt","w",stdout);
 cin>>t;
 for(int z=1;z<=t;z++)
 {

    cin>>n;
     fo(i,n ) cin>>a[i];

     br=0;
     fr(i,2,n)
     if (a[i]<a[i-1]) br+=a[i-1]-a[i];
cout<<"Case #"<<z<<": "<<br;

br=0;
fr(i,2,n)
if (a[i]<a[i-1])
br=max(br,a[i-1]-a[i]);
f=0;
fo(i,n-1)
f+=min(br,a[i]);
cout<<" "<<f<<endl;

 }



   return 0;
}
