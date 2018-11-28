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
   string s;
   LL count=0;
   for (int Case = 0; Case < t; ++Case)
   {
      cin>>s;
      count=0;

      int l=s.length();

      int i=l-1;
      while(i>=0&&s[i]=='+')
         i--;
      int j=0;
      while(i>=0)
      {
         while(i>=0&&s[i]=='+')
            i--;

         if(i<0)
            break;


         
         if(s[0]=='+')
         {
            j=0;
            while(j<l&&j<=i&&s[j]=='+')
            {  
               s[j]='-';
               j++;
            }
            count++;
         
         }
         else
         {

            for(int k=0;k<=i/2;k++)
            {
               swap(s[k],s[i-k]);
            }
            for(int k=0;k<=i;k++)
            {
               if(s[k]=='+')
                  s[k]='-';
               else
                  s[k]='+';
            }
            count++;
         }

      }
      // cout<<s<<" "<<i<<" ";
      printf("Case #%d: %lld\n",Case+1,count);
      


   }

}