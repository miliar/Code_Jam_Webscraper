#include<bits/stdc++.h>
#include<time.h>
using namespace std;
#define ll unsigned long long int
double tim;
clock_t s,e;

bool isnonp(ll m){
	ll a=14923738830;
	ll b= __gcd((ll)14923738830,m);
	if(b==1){
		return false;
	}
	return true;
}
main(){
	ll a,b,c,d,t,i,j,x,n,y,f,z,m,k;
      s= clock();
	  cin>>t;
	  cin>>n;
	  cin>>m;
	  vector< ll > v1;
	    c= pow(2,n-2);
      for(i=0; i<c; i++){
          
            f=0;
      	 for(j=2; j<=10; j++){         
            y=1;
            a=1;
            x=i;
              
            while(x){
            	if(x&1){
                  a= a+ pow(j,y);
            	}
            	x=x>>1;
            	y++;
            }
              a= a+ pow(j,n-1);
             // cout<<a<<" ";
             if(!isnonp(a)){

                 f=1;
               }
      	   }
      	   //cout<<"\n";
      	     if(!f){
      	     	  //cout<<a<<" ";
             	v1.push_back(a);
             	 if(v1.size()==m){
             	 	break;
             	 }
      	     } 	   
      }
         cout<<"Case #1:\n";
        for(i=0; i<v1.size(); i++){
           
               cout<<v1[i]<<" ";
           for(j=2; j<=10; j++){
               a=0;
               x=v1[i];
               y=0;
            while(x){
            	if(x%10==1){
                  a= a+ pow(j,y);
            	}
            	x=x/10;
            	y++;
            }
             for(k=2; k<=sqrt(a); k++){
             	if(a%k==0){
             		cout<<k<<" ";
             		break;
             	}
             }
              
             }
            cout<<"\n";   
        }

	  e= clock();

	  tim= (double)(e-s)/CLOCKS_PER_SEC;
	//  cout<<tim<<" time taken by code";

}