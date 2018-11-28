/*  
   Mayank Pratap Singh
   MNNIT, 2nd year IT
         
   AC ho.
*/
#include<bits/stdc++.h>
using namespace std;
#define ff first
#define ss second
#define pb push_back
#define mp make_pair

#define MOD 1000000007

typedef long long ll;
typedef long double ld;

const int INF=(int)(1e9);
const ll INF64=(ll)(1e18);
const ld EPS=1e-9;
const ld PI=3.1415926535897932384626433832795;


typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef vector<list<int> > vl;
typedef map<int,int> mi;
typedef map<string,int> ms;
typedef set<int> si;

int solve(string str){

   int len=str.size();

   string newstr;

   if(len==0)
   	   return 0;

   if(str[len-1]=='-'){

      newstr=str.substr(0,len-1);

      for(int i=0;i<(int)newstr.size();++i){

         if(newstr[i]=='+')
             newstr[i]='-';

         else
         	 newstr[i]='+';
      }

      return 1+solve(newstr);
   }	

   else{

      newstr=str.substr(0,len-1);

      return solve(newstr);
   }

}

int main(){

    int t;

    scanf("%d",&t);

    for(int k=1;k<=t;++k){

       string str;
       cin>>str;
       printf("Case #%d: %d\n",k,solve(str));

    }

	return 0;
}