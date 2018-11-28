#include <iostream>
#include <iomanip>      // std::setprecision
using namespace std;


int main()
{
	int t, n, k;
	double c, f, x, ans, pk, sk;
	
	cin >> n;
	for (t=0; t<n; t++) {
		cin >> c >> f >> x;
		pk=0;
		sk=x/2;
		k=0;
		do {
			k++;
			ans=sk;
//			cout << ans << endl;
			pk=pk+c/(f*(k-1)+2);
			sk=pk+x/(f*k+2);
		} while (ans>sk);
//		cout << sk << endl;
		
		std::cout << std::fixed;
		cout << std::setprecision(7) << "Case #" << t+1 << ": " << ans <<  endl;
	}	
	return 0;
}
