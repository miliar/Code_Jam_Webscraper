#include<bits/stdc++.h>
using namespace std;

int main(){
   cout.sync_with_stdio(0);
   int T;
   cin>>T;
   
   for(int t=1;t<=T;t++){
      int n;
      string S;
      cin>>n>>S;
      
      int odp=0,akt=0;
      
      for(int i=0;i<=n;i++){
	 if(i>akt){
	    odp+=i-akt;
	    akt=i;
	 }
	 akt+=S[i]-'0';
      }
      cout<<"Case #"<<t<<": "<<odp<<"\n";
   }
   return 0;
}