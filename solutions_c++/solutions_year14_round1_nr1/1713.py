#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

ifstream in("in.txt"); ofstream out("out.txt");

int nOut, bLen, trials, pow2m;
vector<int> outlets;
vector<int> devices;

int pow2(int k)
{
	int i = 1;
	while (k > 0) { i *= 2; --k; }
	return i;
}

int main()
{
	in >> trials;
	for (int thisTime = 1; thisTime <= trials; ++thisTime)
	{
		outlets.clear(); devices.clear();
		in >> nOut >> bLen; pow2m = pow2(bLen);
		for (int i = 0; i < nOut; ++i)
		{
			string s; in >> s;
			int num = 0, po2 = 1;
			for (int j = bLen-1; j >= 0; --j)
			{
				num += (s.substr(j, 1)=="1")*po2;
				po2 *= 2;
			}
			outlets.push_back(num);
		}
		sort(outlets.begin(), outlets.end());

		for (int i = 0; i < nOut; ++i)
		{
			string s; in >> s;
			int num = 0, po2 = 1;
			for (int j = bLen-1; j >= 0; --j)
			{
				num += (s.substr(j, 1)=="1")*po2;
				po2 *= 2;
			}
			devices.push_back(num);
		}
		sort(devices.begin(), devices.end());

		unsigned int minM = -1;
		for (int trial = 0; trial < pow2m; ++trial)
		{
			//cout << trial << endl;
			vector<int> newOut = outlets;
			for (int i = 0; i < newOut.size(); ++i) newOut[i] = newOut[i]^trial;
			sort(newOut.begin(), newOut.end());
			bool fail = false;
			for (int j = 0; j < newOut.size(); ++j)
				if (newOut[j] != devices[j]) fail = true;
			if (!fail)
			{
				//cout << trial << endl;
				int nM = 0; int moveNum = trial;
				while (moveNum > 0)
				{
					nM += moveNum%2;
					if (nM > minM) moveNum = 0;
					moveNum /= 2;
				}
				if (nM < minM) minM = nM;
			}
		}

		out << "Case #" << thisTime << ": ";
		if (minM == UINT_MAX) out << "NOT POSSIBLE\n";
		else out << minM << endl;
		/*for (int i = 0; i < working.size(); ++i)
			out << working[i] << " ";
		out << endl;
		for (int i = 0; i < outlets.size(); ++i)
			out << outlets[i] << " ";
		out << endl;
		for (int i = 0; i < devices.size(); ++i)
			out << devices[i] << " ";
		out << endl << endl;*/
	}
	//cin >> trials;
	return 0;
}