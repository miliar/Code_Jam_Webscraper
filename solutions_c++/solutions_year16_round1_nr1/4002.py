#include<iostream>
#include<fstream>
#include<algorithm>


int main()
{
	int i, j, N, n, T;
	char ch[1005],cc;
	std::string str = "";
	char c;
	std::ofstream out("1.out");
	std::ifstream inp("1.in");
	inp >> T;
	inp.getline(ch, 200);
	for (int ii = 1; ii<=T; ++ii) {
		inp.getline(ch, 1005);
		str = ch[0];
		cc = ch[0];
		for (i = 1; ch[i] != '\0'; ++i) {
			if (cc > ch[i]) {
				str = str + ch[i];
			}
			else {
				cc = ch[i];
				str = ch[i] + str;
			}
		}
		out << "Case #" << ii << ": " << str.c_str() << "\n";
	}
	out.close();
	inp.close();
	return 0;
}
