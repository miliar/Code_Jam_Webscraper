#include <vector>
#include <iostream>

using namespace std;

typedef long long int LL;




int main()
{	
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ":";
		
		int N;
		cin >> N;

		if(N == 0)
			cout << " INSOMNIA" << endl;
		else
		{
			LL x = N;
			bool read[10];
			for(int i = 0; i < 10; i++)
				read[i] = false;


			LL z = x;
			for( ; z > 0; z /= 10)
				read[z % 10] = true;
			
			
			while(!(read[0] && read[1] && read[2] && read[3] && read[4] && read[5] && read[6] && read[7] && read[8] && read[9]))
			{
				x += N;

				LL z = x;
				for( ; z > 0; z /= 10)
					read[z % 10] = true;			
			}
			
			cout << " " << x << endl;
		}
	}
}
