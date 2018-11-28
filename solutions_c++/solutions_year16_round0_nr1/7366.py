#include<iostream>
#include<conio.h>
#include<algorithm>
#include<fstream>
using namespace std;

int t,n,mask[10];

int main(void) {

	ifstream cin("input.in");
	ofstream cout("output.out");
	
	cin>>t;
	
	int c=0;
	
	for (; t; --t) {

		cin>>n;
	//	n=t;
		int nr=0;
		int sol=0;

		for (int i=1; i<=100; ++i) {
		   int aux=i*n;
		   ++sol;
			while (aux>=10) {
				if (mask[aux%10]!=t) { mask[aux%10]=t; ++nr; }
				aux/=10;
			}
			
			if (mask[aux%10]!=t) { mask[aux%10]=t; ++nr; }
			
			if (nr==10) break;
		}
		
		++c;
		cout<<"Case #"<<c<<": ";
		
		if (nr<10) cout<<"INSOMNIA\n";
		else cout<<sol*n<<"\n";
		
	}
	
	return 0;
}
