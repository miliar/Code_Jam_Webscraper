
#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
using namespace std;
int main()
{
	freopen("D:\\C++ Projects\\Cookies\\B-large.in","r",stdin); // For reading input
    freopen("D:\\C++ Projects\\Cookies\\Output2.txt","w",stdout); // for writing output
	double L, T;cin>>T;
	for (L=1;L<=T;L++)
	{
		double C , F , X , t=0 ,i=0 ;
		cin >> C >> F >> X ;
		if ((X)/(2+i*F) <= ((C/(2+i*F)) + (X/(2+(i+1)*F))))
			t = (X)/(2+i*F);
		else 
		{
			while ( (X)/(2+i*F) > ((C/(2+i*F)) + (X/(2+(i+1)*F))))
			{
			t = t + (C/(2+i*F));
			i++;
			}
			t = t + (X)/(2+i*F);
		}
		std::cout << "Case #" << L << ": " << std::fixed << std::setprecision(7) << t <<'\n';
	 

	}
return 0;
}
