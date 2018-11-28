#include<iostream>
#include<string>
#include<fstream>
using namespace std;


int minFriend(string str)
{
	if (str.size() == 0 || str.size()==1)
		return 0;
	int tempsum = str[0] - '0', needF = 0;
	for (int i = 1; i < str.size(); i++)
	{
		
		if (tempsum<i)
		{
			needF += (i - tempsum);
			tempsum += (i - tempsum+(str[i]-'0'));
		}
		else{
			tempsum += (str[i] - '0');
		}
	}
	return needF;
}

int main()
{
//
//	int a = minFriend("0000201");
//	cout << a << endl;


	int totalline,i=0;

	
	ifstream infile("A-large.in");
	if (!infile)
	{	
		cerr << "error open file" << endl;
		exit(0);
	}
	infile >> totalline;
	int *p = new int[totalline];
	ofstream outfile("A-large-result.in");
	while (i < totalline)
	{
		int size = 0; string instr;
		infile >> size >> instr;
		cout << size << " " << instr<<endl;
		int temp = minFriend(instr);
		p[i++] = temp;
		
	}
	for (int j = 1; j <= totalline; j++)
	{
		outfile << "Case #" << j << ": " << p[j-1] << endl;
	}
	delete[]p;
	infile.close();
	outfile.close();
	system("pause");
	return 0;
}