#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		double c,f,x;
		cin>>c>>f>>x;
		double time=0.0;
		double rate=2.0; 
		while(true){
			if(x/rate>((c/rate)+(x/(rate+f)))){
				time+=(c/rate);
				rate+=f;
			}
			else{
				time+=(x/rate);
				break;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		cout<<setprecision(7)<<fixed<<time*1.0<<endl;
	}
}
