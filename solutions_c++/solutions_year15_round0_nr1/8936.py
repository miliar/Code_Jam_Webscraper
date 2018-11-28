#include <iostream>
using namespace std;

void start()
{
	int C = 0, smax;
	char line[2000];
	cin >> smax;
	while(cin >> smax >> line) {
		auto p = 0, f = 0, l = 0;
		for(auto && c : line) {
			if(c == 0) break;
			c &= 0x0F;
			if(c && (l > p)) {
				auto cf = l - p;
				f += cf;
				p += cf;
			}
			p += c;
			l++;
		}
		cout << "Case #" << ++C << ": " << f << endl;
	}
}

int main(int argc, char *argv[])
{
	start();
	return 0;
}

