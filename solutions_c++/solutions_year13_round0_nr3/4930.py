#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

bool isPalin(string str){
	for (int i=0; i<str.size(); i++)
		if (str[i]!=str[str.size()-i-1])
			return false;
	return true;
}


int main ()
{
	ifstream cin("C-small-attempt0.in");
	ofstream cout("sevag_fairsquare_small.out");

	int T, A, B;

	cin>>T;
	for (int t=1; t<=T; t++)
	{
		cin>>A>>B;

		int count=0;

		for (int num=A; num<=B; num++)
		{
			int root = sqrt((double)num);
			if (root*root == num){
				char buff[10];
				itoa(root,buff,10);
				string str1(buff);

				if (isPalin(str1)){
					itoa(num,buff,10);
					string str2(buff);
					if (isPalin(str2))
						count++;
				}
			}
		}
		cout<<"Case #"<<t<<": "<<count<<endl;

	}

	return 0;
}