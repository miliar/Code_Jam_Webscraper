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

int vis;
void update(int n){
//	cout<<n<<" ";
	while(n>0){
		vis|=1<<(n%10);
		n/=10;
	} 
//	cout<<vis<<endl;
}
int main(){
     READ("A-large.in");
  	WRITE("A-large.out");
     long long t,n;
     cin>>t;
     for(int a=1;a<=t;a++){
     	cin>>n;
     	if(n==0){
     		cout<<"Case #"<<a<<": "<<"INSOMNIA"<<endl;
     		continue;
     	}
     	vis=0;
     	int i=0;
     	do{
     		i++;
     		update(n*i);
     	}while(vis!=1023);
     	cout<<"Case #"<<a<<": "<<n*i<<endl;
     }
     
	 return 0;
}
