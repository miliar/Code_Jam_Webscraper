#include <bits/stdc++.h>
using namespace std;
int f(int c,int w){
	if(w==1) return c;
	if(c==w) return w;
	if(c<=2*w) return w+1;
	int i=0;
	while(c>2*w){
		i++;
		c-=w;
	}
	return i+f(c,w);

}
int main(){
	freopen("AS.in", "r", stdin);
  	freopen("OS.txt", "w", stdout);
	int t,n,ans,r,c,w;
	cin>>t;
	for(int k=1;k<=t;k++){
		cin>>r>>c>>w;
		ans=f(c,w);
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}