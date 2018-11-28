#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

bool checks(long long num, bool* grid)
{
	ostringstream ss;
	ss << num;
	string toch = ss.str();
	for (int i = 0; i < toch.length(); i++)
	{
		grid[toch[i] - '0']=true;
	}
	bool is = true;
	for (int i = 0; i < 10; i++)
	{
		if (!grid[i])is = false;
	}

	return is;
}

int main(){

	int T, mex = 0; cin >> T;
	long long num;
	ofstream out;
	out.open("outputA.txt");
	for (int i = 1; i <= T; i++)
	{
		int counter = 2, temp;
		bool * grid = new bool[10]{ 0 };
		cin >> num;
		temp = num;
		while (!checks(temp, grid) && counter < 75&&num!=0) { temp = num*counter; counter++; }



		if(num==0) out << "Case #" << i << ": INSOMNIA\n";
		else out << "Case #" << i << ": " << temp << "\n";
		mex = max(counter, mex);
	}


	out.close();

	return 0;
}