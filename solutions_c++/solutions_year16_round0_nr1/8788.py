#include<iostream>

using namespace std;

bool check( int x, int a[] ) {
	while ( x>0 ){
		a[x%10] = 1;
		x/=10;
	}
	for ( int i = 0; i < 10; i++ ) {
		if ( a[i] == 0 )
			return false;
	}
	return true;
}
int main()
{
	int t, o = 0;
	cin >> t;
	while ( t-- ) {
		++o;
		int n;
		cin >> n;
		cout <<"Case #"<<o<<": ";
		if ( !n ) {
			cout<<"INSOMNIA"<<endl;
		}else{
			int a[10]={0}, x = 0;
			do{
				x += n;
			}while(!check(x,a));
			cout<<x<<endl;
		}
	}
}
