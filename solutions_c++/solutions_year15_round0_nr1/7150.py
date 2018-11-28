#include <iostream>
#include <string>
using namespace std;

std::string removeSpaces(std::string s) {
	std::string t;
	for (int i = 0; i < s.length(); i++) { 
		if (!isdigit(s[i])) continue;
		t += s[i];
	}
	return t;
}

int extraPersonsForOvation(std::string shy, int smax)
{
	//cout << shy << " : " << smax << endl;	
	std::string shyness = removeSpaces(shy);
	int total = 0, extra = 0;
	for (int i = 0; i <= smax; i++)
	{		
		int shy_cnt = shyness[i] - '0';		
		if (i != 0 || shy_cnt == 0) {
			if (total < i) {
				extra += (i - total);
				total += (i - total);
			}
		}
		total += shy_cnt;
	}
	return extra;
}

int main()
{
	int caseno = 1;
	int total, smax;
	cin >> total;	
	string shyness;
	
	while(caseno <= total) {
		shyness = "";
		cin >> smax;
		std::getline(std::cin, shyness);
		int count = extraPersonsForOvation(shyness, smax);
		cout << "Case #" << caseno << ": " << count << endl;
		caseno++;
	}
	return 0;
}