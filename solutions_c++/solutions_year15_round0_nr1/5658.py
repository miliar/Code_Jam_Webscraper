#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;


int main(){

	ifstream ifz("a.txt");
	ofstream ofz("b.txt");


	if (ifz.is_open() && ofz.is_open())
	{

		int icase;
		string s;

		getline(ifz, s);
		stringstream(s) >> icase;

		for (int i = 1; i <= icase; i++)
		{

			int imax, cur = 0, need = 0;
			int *aud;
			stringstream ss;

			getline(ifz, s);
			ss.str(s);

			ss >> imax;
			imax++;

			aud = new int[imax];
			char c;

			for (int j = 0; j < imax; j++)
			{
				ss >> c;
				string s2;
				s2 = c;
				stringstream(s2) >> aud[j];
				if (cur < j && aud[j] > 0)
				{
					int n;
					n = j - cur;
					need += n;
					cur += n;
				}

				cur += aud[j];

				if (cur > imax)
				{
					break;
				}
			}

			ofz << "Case #" << i << ": " << need << endl;

		}

	}
	int z;
	cin >> z;
}