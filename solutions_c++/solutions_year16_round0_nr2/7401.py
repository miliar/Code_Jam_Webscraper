//Md. Ahsan Kabir Shohagh
#include<bits/stdc++.h>
using namespace std;
#define sz 100000
#define pb(a) push_back(a)
#define ll long long
#define ull unsigned long long
#define fread freopen("input.txt","r",stdin)
#define fwrite freopen("output.txt","w",stdout)
#define inf (1<<29)
#define mem(abc,z) memset(abc,z,sizeof(abc))
#define PI acos(-1)
#define quick ios_base::sync_with_stdio(0)

int main(){
   fread;
   fwrite;
   int t,ans,len;
   string s;
   char last;
   scanf("%d",&t);
   for(int ca=1;ca<=t;ca++){
      cin>>s;
      ans=0;
      len=s.size();
      last='*';
      for(int i=0;i<len;){
         while(i<len && s[i]=='+'){
            i++;
            last='+';
         }
         ans+=(last=='+');
         while(i<len && s[i]=='-'){
            i++;
            last='-';
         }
         ans+=(last=='-');
      }
      printf("Case #%d: %d\n",ca,ans-(last=='+'));
   }
   return 0;
}
/*
5
-
-+
+-
+++
--+-
*/
