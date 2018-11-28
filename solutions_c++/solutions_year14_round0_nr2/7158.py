#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
	ofstream fout;
	ifstream fin;
	fout.open("B-large.out");
	fin.open("B-large.in");
	int t;
	fin >> t;
	double c, f, x;
	double speed = 0;
	double min = 1E+37;
	double ans[t];
	double time = 0;
	double l = 0;
	int count = 0;
	bool increase = true;
	double place = 0;
	double x1;
	//double cookie = 0;
	
	for(int i = 0; i < t; i++)
	{
		fin >> c >> f >> x;
		l = x - c;
		speed += 2;
		while(increase)
		{
			time += (c/speed);
			//cookie += c;
			x1 = l/speed + time;
			//cout << "Case " <<  i+1  << ": << " << x1 << endl;
			if(x1 < min)
			{
				min = x1;
			}
			if(count >= 1 && place < x1)
			{
				increase = false;
			}
			place = x1;
			//cookie -= c;
			speed += f;
			count++;
		}
		ans[i] = min;
		speed = 0;
		time = 0;
		min = 1E+37;
		count = 0;
		increase = true;
	}
	
	for(int i = 0; i < t; i++)
	{
		fout << setprecision(15) << "Case #" << i + 1 << ": " << ans[i] << endl;
		//cout << setprecision(15) << "Case #" << i + 1 << ": " << ans[i] << endl;
	}
		
	fin.close();
	fout.close();
	return 0;
}