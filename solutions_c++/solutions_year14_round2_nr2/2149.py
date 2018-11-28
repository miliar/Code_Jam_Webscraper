#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;
int main() 
{	int t;
int A,B,K;
int c,i,j,b;
	cin>>t;
	b=0;
	while(t--){
		b++;
		int c1=0;
		cin>>A>>B>>K;
		for(i=0;i<A;i++){
			for(j=0;j<B;j++){
				if((i&j)<K)
				c1++;
			}
			}
			cout<<"Case #"<<b<<": "<<c1<<"\n";
	}

	return 0;
}