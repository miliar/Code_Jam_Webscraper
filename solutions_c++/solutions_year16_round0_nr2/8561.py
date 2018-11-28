#include <bits/stdc++.h>

using namespace std;

#define all(n) (n).begin(),(n).end()
#define rall(n) (n).rbegin(),(n).rend()
#define mp make_pair
#define pb push_back
#define sz size()
#define F first
#define S second
#define FO(i,x) for(int i=0;i<x;i++)

#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
//  int dx[]={-2,-2,-1,-1,1,1,2,2}; int dy[]={-1,1,-2,2,-2,2,-1,1}; // Knight Dir
//  int dx[]={-1,-1,-1,0,1,1,1,0}; int dy[]={-1,0,1,1,1,0,-1,-1};  // 8 Dir
//  int dx[]={0,1,-1,0}; int dy[]={1,0,0,-1}; // 4 Dir


int main(){
     READ("B-large.in");
  	 WRITE("B-large.out");
     
     
	 int t;
     string s;
     cin>>t;
     FO(k,t){
     	cin>>s;
     	char cur=s[0];
     	int res=0;
     	FO(i,s.sz){
     		if(s[i]!=cur){
     			cur=s[i];
     			res++;
     		}
     	}
     	if(cur=='-') res++;
     	cout<<"Case #"<<k+1<<": "<<res<<endl;
     }
     	
     
	 return 0;
}
