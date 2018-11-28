#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<cstdlib>
using namespace std;
int main(){
 double c,f,x,t,y,totaltime,rate,i;
int ca = 0;
cin>>t;
while(t--){
	cin>>c>>f>>i;
	ca++;
	rate = 2.0;
	totaltime =0.0;
	//cout<<c<<f<<x;
	while(true){
		x = (i/rate);
		y = (c/rate)+(i/(rate+f));
		if(x>y){
			totaltime+=(c/rate);
			rate+=f;
		}else{
			totaltime+=(i/rate);
			break;
		}
	}
	//cout<<totaltime<<endl;
	printf("Case #%d: %.7f\n",ca,totaltime);
	
}

return 0;
}

