#include <iostream>
using namespace std;
int main()
{
	unsigned int T,k;
	unsigned long long N,interval,val,dupVal;
  	unsigned int digits=0;	
	cin >> T;
	for(unsigned int t=1;t<=T;t++)
	{
	 	digits=0;	
		interval=1;

		cin>>N;

		if(N*interval == 0) {
			cout<<"Case #"<<t<<": INSOMNIA\n"<<endl;
			continue;
		}

		while(1)
		{
			val = interval * N;
			dupVal = val;
			while(dupVal)
			{
				k = dupVal%10;
				digits = digits | (1<<k);
				dupVal = dupVal/10;				
			}			
			//cout<<"I"<<val<<" "<<digits<<endl;
			if(digits  == 1023)
			{
				cout<<"Case #"<<t<<": "<<val<<"\n"<<endl;
				break;
			}	
			interval++;
		}
	}

	return 0;

}
