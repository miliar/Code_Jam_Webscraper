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

    for(int j=1;j<=t;++j){ 

       string str;   

       cin>>str;

      // cout<<str<<"\n";

       map<int,int>ans;

       int count[26]={0};

       for(int i=0;i<(int)str.size();++i){

           count[str[i]-'A']++;
       }

    
       ans[0]=count['Z'-'A'];

       count['E'-'A']-=count['Z'-'A'];
       count['R'-'A']-=count['Z'-'A'];
       count['O'-'A']-=count['Z'-'A'];

      
       
       ans[2]=count['W'-'A'];

       count['T'-'A']-=count['W'-'A'];
       count['O'-'A']-=count['W'-'A'];

     
 

       ans[6]=count['X'-'A'];

       count['S'-'A']-=count['X'-'A'];
       count['I'-'A']-=count['X'-'A'];



       ans[4]=count['U'-'A'];

       count['F'-'A']-=count['U'-'A'];
       count['O'-'A']-=count['U'-'A'];
       count['R'-'A']-=count['U'-'A'];

    

       ans[8]=count['G'-'A'];

       count['E'-'A']-=count['G'-'A'];
       count['I'-'A']-=count['G'-'A'];
       count['H'-'A']-=count['G'-'A'];
       count['T'-'A']-=count['G'-'A'];


       ans[3]=count['R'-'A'];

       count['T'-'A']-=count['R'-'A'];
       count['H'-'A']-=count['R'-'A'];
       count['E'-'A']-=2*count['R'-'A'];

       ans[7]=count['S'-'A'];

       count['E'-'A']-=2*count['S'-'A'];
       count['V'-'A']-=count['S'-'A'];
       count['N'-'A']-=count['S'-'A'];

       ans[5]=count['F'-'A'];
       count['I'-'A']-=count['F'-'A'];
       count['V'-'A']-=count['F'-'A'];
       count['E'-'A']-=count['F'-'A'];

       ans[1]=count['O'-'A'];
       count['N'-'A']-=count['O'-'A'];
       count['E'-'A']-=count['O'-'A'];

       ans[9]=count['N'-'A']/2;
       
       

       printf("Case #%d: ",j);
 
       for(int i=0;i<10;++i){

           for(int j=0;j<ans[i];++j){

               printf("%d",i);
           }


       }  

       printf("\n"); 
   
    
    }

	return 0;
}