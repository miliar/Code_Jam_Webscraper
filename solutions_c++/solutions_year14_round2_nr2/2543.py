#include <iostream>
using namespace std;

unsigned long A,B,K;

int main()
{
	int T;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		int res=0;
		cin >> A >> B >> K;
		for(int i=0;i<A;i++)
			for(int j=0;j<B;j++)
				if((i&j)<K)
					res++;
		
		cout << "Case #" << t << ": " << res << endl;
	}
	
	return 0;
}

