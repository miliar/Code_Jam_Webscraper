#include <iostream>
#include<fstream>

using namespace std;
int a[11];
void init(){
	int i;
	for (i=0; i< 10; i++){
		a[i]=0;
	}
}
bool check(){
	int i;
	for (i=0; i<10; i++){
		if(a[i]==0) return false;
	}
	return true;
}
void doit(long long n ){

	while(n!=0){
		a[n%10]++;
		n=n/10;
	}
}
bool solve(long long &n){
	init();
	int dem =0;
	long long temp =n;
	while(true){
		if (check() || dem>100000) break;
		doit(n);
		if (check() || dem>100000) break;
		dem ++;
		n=n+temp;
	}
	if (check()) return true;
	else  return false;
}

int main(){
	long long  t,i,n;
	ifstream in ("input3.in");
	ofstream out ("output.out");	
	in>>t;
	for (i=1; i<=t; i++){
		in>>n;
		if(solve(n)) out<<"Case #"<<i<<": "<<n<<endl;
		else out<<"Case #"<<i<<": INSOMNIA\n";
	}
	return 0;
}
