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

int main(){

   int t;

   scanf("%d",&t);

   for(int k=1;k<=t;++k){

       deque<char>mydick;
 

       string str;

       cin>>str;

       for(int i=0;i<(int)str.size();++i){

           if(i==0)
              mydick.pb(str[i]);   

           else{

               if(str[i]-'A'<mydick.front()-'A'){


                  mydick.pb(str[i]);

               }

               else
               	  mydick.push_front(str[i]);
               

           }

       }

       printf("Case #%d: ",k);

       while(!mydick.empty()){

           cout<<mydick.front();
           mydick.pop_front();

       }

       printf("\n");






   }

















	return 0;
}