#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
int main(){
  ll n,t;
  cin>>t;
   int w=1;
  while(t--){
    int x,cx;
    cin>>n;
    bool V[10];
    for(int i=0 ; i<10 ; i++){
      V[i]=false;
    }
    bool sw=false;
    if(n==0) cout<<"Case #"<<w<<": INSOMNIA"<<endl;
    else{
      int i=1;
      while(!sw){
	// for(int i=1 ; !sw ; i++){
	x= n*i;
	cx=x;
	while(x>0){
	  int d= x%10;
	  x/=10;
	  // cout<<"esta es x :v : "<<x<<endl;
	  V[d]=true;
	}
	int c=0;
	//verificar si existe un 0 en el vector
	for(int j=0 ; j<10 ; j++){
	  if(V[j]==true) c++;
	  // cout<<"este es c "<<c<<endl;
	}
	if(c==10) sw=true;
	i++;
      }
      cout<<"Case #"<<w<<": "<<cx<<endl;
    }
    w++;
  }    
  
  return 0;
}
