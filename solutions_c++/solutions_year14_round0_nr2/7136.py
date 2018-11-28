#include <fstream>
//#include <iostream>
#include <iomanip>
using namespace std;
ifstream cin("input.in");
ofstream cout("output.out");
int t, leftover;
double f, x, c, curspeed, ans;

int main(){
	cin>>t;
	int kk=0;
	while(t--){
		cin>>c>>f>>x;
		int k=0;
		leftover=0;
		curspeed=2;
		ans=0;
		while((x-c)/(2+k*f)>x/(2+(k+1)*f))
			k++;
		//cout<<k<<endl;
		for(int i=0; i<k; ++i){
			ans+=c/curspeed;
			curspeed+=f;
		}
		ans+=x/curspeed;
		cout<<"Case #"<<++kk<<": "<<fixed<<setprecision(7)<<ans<<endl;
	}
}
/*
4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0

1
500.0 4.0 2000.0
*/