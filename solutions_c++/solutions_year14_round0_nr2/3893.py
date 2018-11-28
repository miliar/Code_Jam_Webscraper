#include <fstream>
#include <vector>

using namespace std;

ifstream cin("test.in");
ofstream cout("test.out");

#define M 300200

long double c,f,x;

void read(void){
	cin >> c >> f >> x;
}

long double get(int k){
	long double ans=0;
	for (int i=0; i<k; ++i)
		ans += c/(2+i*f);
	
	ans += x/(2+k*f);
	
	return ans;
}

void kill(void){
	int l=0,r=M,m1,m2;
	
	while (l<r){
		m1=( 2*l + r )/3;
		m2=( l + 2*r )/3;
		
		if (get(m1)<=get(m2))
			r=m2;
		else
			l=m1+1;
	}
	
	cout<<get(l)<<"\n";
	
}


int main(){
	int t;
	cin>>t;
	
	cout.precision(8);
	cout<<fixed;
	
	for (int i=1; i<=t; ++i){
		cout<<"Case #"<<i<<": ";
		read();
		kill();
	}
	return 0;
}
