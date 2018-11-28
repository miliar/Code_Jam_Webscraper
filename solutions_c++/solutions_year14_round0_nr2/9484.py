#include <iostream>
#include <cstdio>

using namespace std;
 double c,f,x,tt;
 double cal( double r, double t){
//cout<<tt<<endl;
	if(t+x/r>tt)return tt;
	tt=t+x/r;
	return cal(r+f,t+c/r);
}

int main(){
freopen("in.txt","r",stdin);
freopen("out.out","w",stdout);
int t;cin>>t;
for(int i=0;i<t;i++){
	cin>>c>>f>>x;
	tt=x/2;
	printf("Case #%d: %f\n",i+1,cal(2,0));
	
}
return 0;
}