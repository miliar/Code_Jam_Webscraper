#include<iostream>
#include<cstdio>
#include<iomanip>

using namespace std;

int main(){
	int t,cases=1;
	long double c,f,x,time,rate;
	cout<<fixed<<setprecision(7);
	scanf( "%d" , &t );
	while( t-- ){
		cin>>c>>f>>x;
		time = 0.0; rate = 2.0;
		float p,q;
		p = x/rate;
		q = ( c/rate ) + ( x/(rate+f) );
		while( p > q ){
			time += (c/rate);
			rate += f;
			p = x/rate;
			q = ( c/rate ) + ( x/(rate+f) );
		}
		time += p;
		cout<<"Case #"<<cases++<<": "<<time<<endl;
	}
	return 0;
}

