#include <iostream>
#include <set>

int main()
{
	using namespace std;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++){
		unsigned long int a;
		unsigned long long int c;
		int o;
		cin >> o;
		c = o;
 		a = o;
		set<int> digits;		
		while(digits.size() < 10 && o != 0){
			do{
				int d = a % 10;
				digits.insert(d);
				a = a / 10;
			} while (a >= 1);
			c += o;
			a = c; 
		}
		c -= o;
		if (o == 0) {
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
			continue;
		}
		cout << "Case #" << i + 1 << ": " << c << endl;
	}	
}
