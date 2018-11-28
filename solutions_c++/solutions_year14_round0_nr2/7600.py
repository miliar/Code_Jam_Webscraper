#include <bits/stdc++.h>
#include<vector>
#include<fstream>
using namespace std;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("output2.in","w",stdout);
	long double t,c,f,x,check1,check2;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>c>>f>>x;
		check1=x/2;
		check2=c/2;
		double d=f;
		while(true){
			if(check1<(check2+double(x/(f+2))))break;
			else{
				check1=check2+double(x/(f+2));
				check2=check2+double(c/(f+2));
				f+=d;	
			}
		}
		cout<<"Case #"<<i+1<<": "<<setprecision(7)<<fixed<<check1<<endl;
	}
	
	
	
	
	
	
	return 0;
}
