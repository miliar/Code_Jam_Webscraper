#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<functional>
#include<string>
#define ld long double
#define ll long long int
#define max(a,b) a>b?a:b
#define min(a,b) a<b?a:b
#define fi(a,b,c) for(int a=b;a<c;a++)
#define fd(a,b,c) for(int a=b;a>c;a--)
using namespace std;
int n,total;
int main(){
   int t;cin>>t;
   for(int te=1;te<=t;te++){
      cin>>n;
      int nn=n;
      vector<int> pp(n);
      vector<string> ans;
      for(int i=0;i<n;i++){
         cin>>pp[i];
         total+=pp[i];
      }
      string temp="";
      for(int i=0;total;i++){
         if(pp[i%n]){
            pp[i%n]--;total--;
            temp=temp+(char)('A'+(i%n));
            if(temp.length()==2 || nn==1){
               ans.insert(ans.begin(),temp);
               temp="";
            }
            if(pp[i%n]==0)nn--;
         }
      }
      cout<<"Case #"<<te<<": ";
      for(int i=0;i<ans.size();i++){
         cout<<ans[i]<<' ';
      }
      cout<<endl;
   }
   return 0;
}

