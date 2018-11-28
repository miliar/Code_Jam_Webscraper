#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <set>
using namespace std;

int main(){
	int t =0;
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );	
	cin >> t;
	

	for(int i =0; i< t; i++)
	{
		int digitsSeen = 1023;
		long long int multiple = 0;
		long long int multipleTemp = multiple;
		int w = 1;
	
		string result = "INSOMNIA";
		cin >> multiple;

		while(digitsSeen > 0)
		{
			if(multiple == 0) break;
			multipleTemp = multiple * w;
			int k = multipleTemp % 10;
			long long int x = multipleTemp;
			int digits = 0;

			while( x > 0 )
			{
				++digits;
				x /= 10;
			}
			while(digits > 0)
			{
				int k = multipleTemp % 10;
				multipleTemp = multipleTemp - k;
				multipleTemp = multipleTemp/10;
				

				int l = 1;
				for(int n = 0; n < k; n++)
				{
					l = l << 1;
				}
                digitsSeen = digitsSeen & (~l);
				digits--;
			}	
			ostringstream  convert;
			convert << (multiple * w);
			result = convert.str();
			w++;
		}
		
		cout << "Case #" << i+1 <<": " << result << "\n";		
	}

}
