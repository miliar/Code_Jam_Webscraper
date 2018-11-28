#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream cin("B-large.in");
	ofstream cout("pancakes_Sevag_large.out");

	int T;
	string str;

	cin>>T;

	for (int t=1; t<=T; t++)
	{
		cin>>str;

		int flips=0;
		bool happy = true;

		int indx = str.size()-1;
		while(indx >= 0)
		{
			if (happy) {
				if (str[indx] == '+') {
					indx--;
				}else {
					flips++;
					indx--;
					happy = !happy;
				}
			}else {
				if (str[indx] == '-') {
					indx--;
				}else {
					flips++;
					indx--;
					happy = !happy;
				}
			}
		}

		cout<<"Case #"<<t<<": "<<flips<<endl;
	}

	return 0;
}