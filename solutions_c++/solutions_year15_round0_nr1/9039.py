#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
	int c,T, shyMax, cur, cnt;
	string in;
	cin >> T;
	c = 1;
	while (T--){
		cnt = cur = 0;
		cin >> shyMax;
		cin >> in;
		for (int i = 0; i < in.size(); i++){
			if (in[i] == '0')
				continue;
			else if (cur >= i)
				cur += in[i]-'0';
			else {
				cnt+= i-cur;
				cur+= in[i]-'0' + i-cur;
			}
		}
		cout << "Case #" <<c++ << ": " << cnt <<endl;
	}	
	return 0;
}