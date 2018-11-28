#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define D(x) cout << #x << " : " << x << endl;

#define For(i,a) for(int i=0; i<a; i++)
#define Fori(i,a,b) for(int i=a; i<b; i++)
#define Forn(i,a,b,c) for(int i=a; i<b; i+=c)
#define pb push_back
#define mp make_pair


int main(){
  #ifdef SV
    freopen("A-small-attempt0.in","r",stdin);
  #endif
    int T;
    cin>>T;
    int first[4],second[4],f,s,x,n;
    for(int cas=1; cas<=T; cas++){
        cin>>f;
        For(i,4){
            For(j,4){
                cin>>x;
                if(i==f-1) first[j]=x;
            }
        }
        cin>>s;
        For(i,4){
            For(j,4){
                cin>>x;
                if(i==s-1) second[j]=x;
            }
        }
        int count=0;
        For(i,4){
            For(j,4){
               if(first[i]==second[j]){
                   count++;
                   n=first[i];
               } 
            }
        }
        
        if(count==0) cout<<"Case #"<<cas<<": Volunteer cheated!"<<endl;
        else if(count==1) cout<<"Case #"<<cas<<": "<<n<<endl;
        else if(count>1)  cout<<"Case #"<<cas<<": Bad magician!"<<endl;
    }
}




