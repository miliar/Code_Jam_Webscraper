#include <iostream>
#include <iomanip>

using namespace std;
int main(){
	int t;
	double c,f,x,time,r;
	cin>>t;
	for(int i=0; i<t; i++){
		time = 0;
		r = 2;
		cin>> c;
		cin>> f;
		cin>> x;
		while(x >= c){
			time = time + c/r;
			if((x-c)/r < x/(r+f)){
				x = x-c;
			}
			else {
				r = r+f;
			}
		}
		time = time + x/r;
		cout<<"Case #";
		cout<<i+1<<": ";
		cout<< std::fixed<<std::setprecision(7)<<time<<"\n";
	}
}
