#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<stack>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<deque>

using namespace std;

#define mem(a) memset(a,-1,sizeof(a))
#define all(a) a.begin(),a.end()
#define clr(a) memset(a,0,sizeof(a))
#define pb push_back
#define pi acos(-1.0)


#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define myabs(a) ((a)<0?(-(a)):(a))
#define max3(a,b,c) max(a,max(b,c))
#define min3(a,b,c) min(a,min(b,c))

#define read freopen("input.txt", "r", stdin)
#define write freopen("output.txt", "w", stdout)
#define ll long long

#define S1(a) scanf("%d",&a)
#define S2(a,b) scanf("%d %d",&a,&b)
#define p1(a,b) printf("Case: %d: %d\n",a,b)
#define p2(a,b) printf("%d %d\n",a,b)

#define rep(i,n) for(int i=0;i<n;i++)
#define rep1(i,n) for(int i=1;i<=n;i++)

#define EPS 1e-9
#define MOD 1073741824
#define INF INT_MAX/3
#define MX 100010

int gcd (int a, int b)
{
    if (b > a) return gcd (b,a);
    return (b == 0) ? a : gcd (b, a%b);
}
int dx[]={-2, -1, 1, 2, 2, 2, 1, -1, -2};
int dy[]={-1, -2, -2, -1, 1, 2, 2, 1};

struct node{ ///sorts the string of the struct in acending order lexicographically
    char a[109];
}arr[100];

bool cmp(node a1,node a2)
{
    return strcmp(a1.a,a2.a)<0;
}

int low,high,loc,mid,a[1009];
int bin_search(int n,int k)
{
  low=0; high=n; loc=-1;
  int value=k;
  while(low<=high && loc==-1){
  mid=(low+high)/2;
  if(value<a[mid])high=mid-1;
  else if(value>a[mid])low=mid+1;
  else loc=mid;
  }
 return loc;
}





int fx[]={0,0,+1,-1,-1,+1,+1,-1};
int fy[]={+1,-1,0,0,-1,-1,+1,+1};


int main()
{
  int i,j,k,n,t,cas=0;
  char str[1009];
  freopen("in.txt","r",stdin);
  scanf("%d",&t);
  while(t--){
     scanf("%d",&n);
     getchar();
     scanf("%s",str);

     int count=0;
     vector<int>v;
     for(i=0;i<=n;i++){
        k=str[i]-48;
        if(i>0)k+=v[i-1];
        v.push_back(k);
     }
     bool f=0;

     for(i=1;i<=n;i++){
        if(v[i-1]<i){
			j=i-v[i-1];
                count+=j;
                f=1;
                v[i-1]+=j;
        }
        if(f){

            for(k=i;k<=n;k++){
                v[k]+=j;
            }
//			for(k=0;k<=n;k++){
//				cout<<v[k]<<" ";
//			}
//			cout<<endl;
            f=0;
        }
     }
     printf("Case #%d: %d\n",++cas,count);
  }
  return 0;
}
