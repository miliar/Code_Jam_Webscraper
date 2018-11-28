#include <bits/stdc++.h>

using namespace std;

#define all(n) (n).begin(),(n).end()
#define rall(n) (n).rbegin(),(n).rend()

#define mp make_pair
#define pb push_back
#define sz size()
#define FO(i,x) for(int i=0;i<x;i++)
#define F first
#define S second
#define ll long long
#define ld long double


#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
//  int dx[]={-2,-2,-1,-1,1,1,2,2}; int dy[]={-1,1,-2,2,-2,2,-1,1}; // Knight Dir
//  int dx[]={-1,-1,-1,0,1,1,1,0}; int dy[]={-1,0,1,1,1,0,-1,-1};  // 8 Dir
//  int dx[]={0,1,-1,0};  int dy[]={1,0,0,-1};
int t,x,r,c;
string fun(){
	  
	  if(r>c) swap(r,c);
	  
	   if(x==1) return "GABRIEL";
	   
	   if(x==2){
	   	     if(r%2==0 || c%2==0) return "GABRIEL";
	   	     else return "RICHARD";
	   }
	   
	   if(x==3){
	     if(r==2 && c==3) return "GABRIEL";
	     if(r==3 && c==3) return "GABRIEL";
	     if(r==3 && c==4) return "GABRIEL";
	     
	     return "RICHARD";
	   }
	   if(r==4 && c==4) return "GABRIEL";
	   if(r==3 && c==4) return "GABRIEL";
	   return "RICHARD";
}	
int main(){ 
     
      READ("D-small-attempt4.in");
      WRITE("D-small-attempt4.out");

	cin>>t;
	for(int k=1;k<=t;k++){
		 cin>>x>>r>>c;
		 cout<<"Case #"<<k<<": "<<fun()<<endl; 
	}	
    return 0;
}
