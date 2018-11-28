// freopen ("input.in","r",stdin);
// freopen ("output.in","w",stdout);
#include<bits/stdc++.h>
#define M 1000000007
#define INF 1000000000000000007LL
#define DMAX 8
#define PI 3.14159265358979323
using namespace std;
#define pb push_back
#define mp make_pair
// #define EPS 1e-7
typedef long long LL;
long long expo(LL a,LL b,LL m){
   LL result = 1;
   while (b){
      if (b&1){
         result=  (result*a)%m;
      }
      b= (b >>1)%m ;
      a= (a*a)%m;
   }
  return result;
}
double expof(double a,int b){
   double result = 1;
   while (b){
      if (b&1){
         result=  (result*a);
      }
      b= (b >>1);
      a= (a*a);
   }
  return result;
} 
// void dfs()
// {
//   int dir[DMAX][2] = {{1, 0},{0, 1}, {0, -1}, {-1, 0},{1, 1}, {1, -1}, {-1, -1}, {-1, 1}};
//   for (int k = 0; k < DMAX; ++k)
//   {
//     int dx = i + dir[k][0];
//     int dy = j + dir[k][1];
   
//     if (0 <= dx and dx < n and 0 <= dy and dy < n and str[dx][dy] == '*')
//        cnt++;
//   }
 
// }
int a[16]={0};
LL n;
LL compx(LL x)
{
   LL ans=0;
   for(int i=0,j=n-1;i<n&&j>=0;i++,j--)
   {
      ans+= expo(x,i,INF)*a[j];

   }
   LL s=sqrt(ans);
   for(int i=2;i<=s;i++)
   {
      if(ans%i==0)
         return i;
   }
   return -1;
}
void fn(LL i,LL *j)
{
   if(*j==0)
      return;
   if(i==n-1)
   {
      int x[10]={0};

      for (int k=2;k<=10;++k)
      {
         x[k]=compx(k);
      }

      for (int k =2; k <=10; ++k)
      {
         if(x[k]==-1)
            return;
      }

      
      
      for (int k = 0; k <=n-1; ++k)
      {
         cout<<a[k];
      }
      cout<<" ";
      for (int k =2; k <=10; ++k)
      {
         cout<<x[k]<<" ";
      }
      cout<<endl;
      (*j)--;
      return;
      

   }
   a[i]=0;
   fn(i+1,j);
   a[i]=1;
   fn(i+1,j);
}

int main()
{
   freopen ("input.in","r",stdin);
   freopen ("output.in","w",stdout);
   int t;
   cin>>t;
   LL j;
   
   
   for (int Case = 0; Case < t; ++Case)
   {
      cin>>n>>j;
      a[0]=a[n-1]=1;
      printf("Case #%d:\n",Case+1);
      fn(1,&j);
   }

}