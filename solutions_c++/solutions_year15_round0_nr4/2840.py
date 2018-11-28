#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("ab.in","r",stdin);
freopen("bc.out","w",stdout);
   int t,p;
  
   cin>>t;
    p=t;
   while(t--){
   int x,r,c;
   cin>>x>>r>>c;
   if(x==1) cout<<"Case #"<<p - t<<": GABRIEL"<<endl;
   
   if(x==2){
   	if( (r*c)%2 == 0) cout<<"Case #"<<p-t<<": GABRIEL"<<endl;
   	else cout<<"Case #"<<p-t<<": RICHARD"<<endl;
   }
   
  if(x==3){
   	if((r==2&& c==3)||(r==4&& c==3)||(r==3&& c==3)||(r==3&& c==2)||(r==3&& c==4))
	    cout<<"Case #"<<p-t<<": GABRIEL"<<endl;
   	else cout<<"Case #"<<p-t<<": RICHARD"<<endl;
   }
   
   if(x==4){
   	if((r==4&& c==4)||(r==4&& c==3)||(r==3&& c==4)) 
	   cout<<"Case #"<<p-t<<": GABRIEL"<<endl;
   	else cout<<"Case #"<<p-t<<": RICHARD"<<endl;
   }

   
   }
}



