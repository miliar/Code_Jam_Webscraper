#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

#define salida fout
#define entrada fin

int main ()
{
	ifstream fin ("a1.in");
	ofstream fout ("a.out");
	int casos,contador=1;
	entrada>>casos;
	while(casos--){
		long long int t,r,sum,n;
		entrada>>r>>t;
		sum=2*r+4*1-3;
		n=1;
		//cout<<"circulo "<<n<<" sum "<<sum<<endl;
		while(sum<=t){
			n++;
			sum+=2*r+4*n-3;
			//cout<<"circulo "<<n<<" sum "<<sum<<endl;
		}
	
		salida<<"Case #"<<contador<<": "<<n-1<<endl;
		contador++;
	}





	return 0;
}

