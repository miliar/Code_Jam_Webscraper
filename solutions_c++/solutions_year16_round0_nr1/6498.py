#include <iostream>
#include <vector>
#include <fstream>
#include <cstdio>
using namespace std;
int main()
{
	int T;
	int Num;
	vector<bool> num;
	//fstream fs;
	ifstream ifs;
	ifs.open("A-large.in",ios::in);
	ofstream os("haha.txt");
	ifs >> T;
	//scanf_s("%d", &T);
	int count;
	int index = 0;
	while (index < T)
	{
		index++;
		count = 0;
		int temp = 0;
		int tmp;
		num.clear();
		num.resize(10, false);
		ifs >> Num;
		//scanf_s("%d",&Num);
		if (Num == 0)
		{
			os << "Case #" << index << ": INSOMNIA " << endl;
			//printf("Case #%d: INSOMNIA\n", index);
			continue;
		}
		tmp = Num;
		while (count < 10)
		{
			temp = Num;
			while (temp)
			{
				if (num[temp % 10] == false)
				{
					count++;
					num[temp % 10] = true;
				}
				temp /= 10;
			}
			Num += tmp;
		}
		os << "Case #" << index <<": " <<  Num - tmp << endl;
		//printf("Case #%d: %d\n", index,Num - tmp);
	}
	ifs.close();
	os.close();
}
