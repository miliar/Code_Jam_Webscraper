//#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

int main(){
	ifstream cin("D-small-attempt3.in.txt");
	ofstream cout("outputD.txt");
	int t,x,r,c;
	string str;
	cin >> t;
	for(int i=1;i<=t;i++){
		cin >> x >> r >> c;
		cout << "Case #" << i << ": ";
		if(x==1)
			cout << "GABRIEL\n";
		else if(x==2)
			cout << ((r*c)%2?"RICHARD\n":"GABRIEL\n");
		else if(x>=7 || (r*c)%x || min(r,c)<=x/2 || (r*c)<=x){
			cout<<"RICHARD\n";
		}
		else{
			cout << "GABRIEL\n";
		}
	}
}