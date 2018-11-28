#include<iostream>
#include<iomanip>
using namespace std;
void f(){
	long double c,f,x;
	cin>>c>>f>>x;
	long double nasek=2,wyn=x/2,t=0;
	while(t<wyn){
		t+=c/nasek;
		nasek+=f;
		wyn=min(wyn,t+x/nasek);
	}
	cout<<setprecision(8)<<fixed<<wyn<<"\n";
}
main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		cout<<"Case #"<<i+1<<": ";
		f();
	}
}
