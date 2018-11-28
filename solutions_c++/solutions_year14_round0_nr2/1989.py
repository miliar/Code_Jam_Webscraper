#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; tt++){
		long double result = 0;
		long double c, f, x;
		cin >> c >> f >> x;
		long double cookieNum = 0;
		long double basicNum = 2;
		long double nowresult = 0;
		while (true){
			if (result == 0){
				result = x / basicNum;
			}
			else{
				nowresult = result - x / basicNum + c / basicNum;
				basicNum += f;
				nowresult += x / basicNum;
				if (nowresult > result){
					break;
				}
				else{
					result = nowresult;
				}
			}
		}

		cout << "Case #" << tt << ": " << fixed << setprecision(7) << result << endl;
	}
	return 0;
}