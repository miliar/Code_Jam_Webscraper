#include <iostream>
#include <string>
#include <sstream>

unsigned long long divisor(unsigned long long x){
	for (int i = 2; i < x / 2; i++)
		if (x%i == 0)
			return i;
	return 1;
}

using namespace std;
int main()
{
	int t,n,length,answers=0;
	cin >> t;
	cin >> length;
	cin >> n;
	std::stringstream s;
	stringstream s1;
	for (int i = 32768; i <= 65535; i++){
		if (answers == n)
			break; 
		for (int j = sizeof(i) * 8 - 1; j >= 0; --j)
		{
			s << (unsigned long long)((i >> j) & 1);
		}
		bool answer = true;
		for (int j = 2; j <= 10; j++){
			if (stoull(s.str(), nullptr, 10) / 10 == 0 || stoull(s.str(), nullptr, 10)%10==0){
				answer = false;
				break;
			}
			else if (divisor(stoull(s.str(), nullptr, j)) == 1){
				answer = false;
				break;
			}
			s1 << divisor(stoull(s.str(), nullptr, j))<<' ';
		}
		if (answer){
			cout << stoull(s.str(), nullptr, 10) << ' ' << s1.str() << endl;
			answers++;
		}
		s.clear();
		s.str(string());
		s1.clear();
		s1.str(string());
	}
	//	system("pause");
	return 0;
}