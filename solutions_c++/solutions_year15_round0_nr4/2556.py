#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<(n);i++)
#define MP make_pair
#define PB push_back
typedef long long ll;
int main(){
	int t;
	int x,c,r;
	cin>>t;
	for(int times=0;times<t;times++){
		cin>>x>>c>>r;
		bool f;
		int s=c*r;
		if(s%x!=0)f=true;
		else if(x==1||x==2)f=false;
		else if(x==3){
			if(s==6||s==9||s==12)f=false;
			else f=true;
		}else{
			if(s==16||s==12)f=false;
			else f=true;
		}
//		cout<<x<<" "<<c<<" "<<r<<" ";
		printf("Case #%d: ",times+1);
		if(f)printf("RICHARD\n");
		else printf("GABRIEL\n");
	}
}
