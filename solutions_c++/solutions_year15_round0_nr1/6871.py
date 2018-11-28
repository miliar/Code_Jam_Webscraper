#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
	int Testno, Smax;
	string shynesstring;
	cin >> Testno;

	ofstream output;
	output.open("output.txt");

	for(int i =0; i < Testno; i++)
	{
		cin >> Smax;
		cin >> shynesstring;
		int audineeded =0;
		int temp =0;
		int currentshyness = 0;
		
		if(Smax == 0)
		{
			cout << "Case #" <<i+1<<":"<<" "<<"0"<<endl;
			output <<"Case #" <<i+1<<":"<<" "<<"0"<<endl;
		}
		else
		{
			for(int i=0; i<Smax+1;i++)
			{
				currentshyness = shynesstring[i] - 48;
				if(currentshyness>0 && i > temp)
				{
					audineeded +=(i-temp);
					temp += (i-temp);
				}
				temp += currentshyness;
			}
			//audineeded = Smax - temp;
			cout << "Case #" <<i+1<<":"<<" "<<audineeded<<endl;
			output << "Case #" <<i+1<<":"<<" "<<audineeded<<endl;
		}
		
	}
	output.close();
	return 0;
}