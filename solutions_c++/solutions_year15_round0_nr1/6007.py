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

int main(){ 
      READ("A-large.in");
      WRITE("A-large.out");
     int t;
     cin>>t;
     int n;
     string s;
     for(int k=1;k<=t;k++){
     	   cin>>n>>s;
     	   int res=0;
     	   int prev=0;
     	   FO(i,n+1)
			if(s[i]!='0'){
     	   	   if(i<=prev){
     	   	   	   prev+=(s[i]-'0');  
     	   	   }else{
     	   	   	   res=res+i-prev;
				   prev=prev + (i-prev) + (s[i]-'0'); 	     
     	   	   }     
     	    }
     	    cout<<"Case #"<<k<<": "<<res<<endl;
     }
		
    return 0;
}
