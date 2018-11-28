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
int main()
{
   freopen ("input.in","r",stdin);
   freopen ("output.in","w",stdout);
   int t;
   cin>>t;
   map<LL,LL> m1,m2;
   m1[1]=1;
   m1[2]=1;
   m1[3]=1;
   m1[4]=1;
   m1[5]=1;
   m1[6]=1;
   m1[7]=1;
   m1[8]=1;
   m1[9]=1;
   m1[0]=1;
   LL temp,n;
   for (int Case = 0; Case < t; ++Case)
   {
      cin>>n;
      m2.clear();
      printf("Case #%d: ",Case+1);
      if(n==0)
      {
         cout<<"INSOMNIA"<<endl;
      }
      else
      {
         temp=n;
         LL i=1;
         while(m2!=m1)
         {
            temp=n*i;

            while(temp)
            {
               m2[temp%10]=1;
               temp/=10;
            }
            if(m2==m1)
            {
               cout<<n*i<<endl;
            }
            i++;
         }

      }


   }

}