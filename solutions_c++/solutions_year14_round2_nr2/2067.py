#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
#include<algorithm>
#include<vector>
#include<set>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
#define MOD 1000000009


template <typename X> X gcd(X a, X b){if(!b)return a; else return gcd(b, a%b);}
long count_bits(long n) {     
  unsigned int c; // c accumulates the total bits set in v
  for (c = 0; n; c++) 
    n &= n - 1; // clear the least significant bit set
  return c;
}
int main()
{
freopen("C:/Users/UMANG JALAN/Desktop/CODE/inp.txt","r",stdin);
freopen("C:/Users/UMANG JALAN/Desktop/CODE/out.txt","w",stdout);
int t,a,b,k;
int z=1;
scanf("%d",&t);
while(t--)
{
  scanf("%d %d %d",&a,&b,&k);
  int cnt=0;
  for(int i=0;i<a;i++)
  {
        for(int j=0;j<b;j++)
        {
            if((i&j) < k) cnt++;
           // cout<<(i&j)<<"\n";
        }
    }
    printf("Case #%d: %d\n",z,cnt); z++;
  
}
}
