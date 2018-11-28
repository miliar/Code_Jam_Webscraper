//Lasha Bukhnikashvili
#include<iostream>
#include<stdio.h>
#include<math.h>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<string>
#define Pi 3.14159265358
#define mod9 %1000000009
#define INF 1000000000
#define mod7 %1000000007
#define LL  long long
#define time clock()/(double)CLOCKS_PER_SEC
using namespace std;
  int it,x,r,c,T;
  char ch;
int main(){
 #ifndef ONLINE_JUDGE
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
 #endif
    cin>>T;
it=0;
    while (T--){
            it++;
    cout<<"Case #"<<it<<": ";
         cin>>x>>r>>c;
         if (x==1){cout<<"GABRIEL\n"; continue;};
         if (r*c%x!=0) {cout<<"RICHARD\n"; continue;};
         if (x==2) {cout<<"GABRIEL\n"; continue;};
         if (x==3) {if (r==1 || c==1) {cout<<"RICHARD\n"; continue;} else {cout<<"GABRIEL\n"; continue;}; };
         if (x==4) {if (r<=2 || c<=2) {cout<<"RICHARD\n"; continue;} else {cout<<"GABRIEL\n"; continue;}; };
         //cout<<"GABRIEL\n";
}
 return 0;
}
