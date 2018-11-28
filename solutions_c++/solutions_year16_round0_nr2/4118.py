#include <iostream>
#include <fstream>

using namespace std;

int times(int n) {
	int result = 1;
	for (int i = 0; i < n; ++i)
	{
		result *= 2;
	}
	return result;
}

int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T = 0;
	in >> T;
	for(int i = 0; i < T; i++) {
		string pan = "";
		in >> pan;
		int n = pan.length();
		int result = 0;
		if (n != 0)	
		{
			char cur = pan[0];
			for (int j = 1; j < n; ++j)
			{
				if (cur != pan[j])
				{
					result++;
					// cout<<cur<<" "<<pan[j]<<endl;
					cur = pan[j];
				}
			}
			if (cur == '-')
			{
				result++;
			}
		}
		out << "Case #"<<i+1<<": "<<result<<endl;
	}
}