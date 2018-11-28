#include<iostream>
#include<string>
#include<fstream>
#define INT_MAX 0x7fffffff

using namespace std;

int main()
{
	fstream in;
	in.open("C://input_large0.in", ios::in);
	if (in.fail()){
		cerr << "Open graph file inputfile error!" << endl;
		return false;
	}
	ofstream outfile("C://output_large0.txt");
	if (!outfile){
		cout << "Unable to open outfile";
		exit(1); // terminate with error  
	}
	const int BUFFER_LENGTH = 100000;
	char buffer[BUFFER_LENGTH] = { 0 };
	int CaseNum = 0;
	in.getline(buffer, BUFFER_LENGTH);
	CaseNum = atoi(buffer);
	int count = 1;
	while (in.getline(buffer, BUFFER_LENGTH))
	{
		int mapList[10] = { 0 };
		int hasShow = 0;
		int N = atoi(buffer);
		int base = 1;
		if (N == 0)
		{
			outfile << "Case #" << count << ": " << "INSOMNIA" << endl;
			count++;
			cout << N*base << endl;
			continue;
		}
		bool findFlag = false;
		while (N*base<0x7fffffff)
		{
			int tempNum = N*base;
			while (tempNum)
			{
				int temp = tempNum % 10;
				if (mapList[temp] == 0)
				{
					mapList[temp] = 1;
					hasShow++;
					if (hasShow == 10)
					{
						outfile << "Case #" << count << ": " << N*base << endl;
						cout << N*base << endl;
						count++;
						findFlag = true;
						break;
					}
				}
				tempNum = tempNum / 10;
			}
			if (findFlag == true)
				break;
			base++;
		}
		if (findFlag == true)
			continue;
		outfile << "Case #" << count << ": " << "INSOMNIA" << endl;
		count++;
		cout << N*base << endl;
	}
	in.close();
	outfile.close();
	return 0;

}