#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,i=0;
	unsigned long long int N,N1,N2;
	cin>>t;
	int k=1,z=0;
	while(k<=t)
	{
		unsigned int r=0;
		z=0;
		cin>>N;
		i=1;
		bool number[] = {false,false,false,false,false,false,false,false,false,false};
		while(!number[0] || !number[1] || !number[2] || !number[3] || !number[4] || !number[5] || !number[6] || !number[7] ||!number[8] || !number[9])
		{
			if(N==0)
			{
				z=1;
				break;
			}
			N1 = i * N;
			N2 = N1;
			//cout<<"N for i="<<i<<" "<<N1<<"\n";
			//cout<<"Values of r\n";
			while(N1>0)
			{
				r = N1%10;
				number[r] = true;
				//cout<<r<<"\n";
				N1=N1/10;
			}
			i++;
		}
		if(z==1)
			cout<<"Case #"<<k<<": INSOMNIA\n";
		else
			cout<<"Case #"<<k<<": "<<N2<<"\n";
		k++;
	}
	return 0;
}