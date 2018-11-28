#include <iostream>
#include <fstream>
using namespace std;
class Magic
{
private:
	char *filename;
public:
	Magic(char* Name)
	{

		filename = new char[100];
#pragma warning(disable: 4996) 
		strcpy(filename, Name);
#pragma warning(default: 4996)
		ifstream fin;
		ofstream Magic("Magic.txt");
		fin.open(filename);
		while (fin.fail())
		{
			cout << "File doesnt exist write the correct file name" << endl;
			cin >> *filename;
			fin.open(filename);
		}
		int temp, FileCheck = 1;
		int Cases = 0, Credit = 0, items = 0;
		fin >> temp;
		Cases = temp;
		while (FileCheck <= Cases)
		{
			const int size = 4;
			int ro1;
			int ro2;
			int Arr[size][size];
			int Arr1[size][size];
			fin >> ro1;
			for (int i = 0; i < size; i++)
			{
				for (int j = 0; j < size; j++)
				{
					fin >> Arr[i][j];
					cout << Arr[i][j];
					cout << " ";
				}
				cout << endl;
			}
			fin >> ro2;
			for (int i = 0; i < size; i++)
			{
				for (int j = 0; j < size; j++)
				{
					fin >> Arr1[i][j];
					cout << Arr1[i][j];
					cout << " ";
				}
				cout << endl;
			}
			int answer;
			int counter = 0;
			for (int i = 0; i < size; i++)
			{
				for (int j = 0; j < size; j++)
				{
					if (Arr[ro1 - 1][i] == Arr1[ro2 - 1][j])
					{
						counter++;
						if (counter == 1)
						{
							answer = Arr[ro1 - 1][i];
						}
					}
				}
			}
			if (counter == 1)
			{
				Magic << "Case #";
				Magic << FileCheck;
				Magic << ": ";
				Magic << answer;
				Magic << '\n';
			}
			if (counter > 1)
			{
				Magic << "Case #";
				Magic << FileCheck;
				Magic << ": ";
				Magic << "Bad magician!";
				Magic << '\n';
			}
			if (counter == 0)
			{
				Magic << "Case #";
				Magic << FileCheck;
				Magic << ": ";
				Magic << "Volunteer cheated!";
				Magic << '\n';
			}
			FileCheck++;
		}
	}
};
void main()
{
	//I have created a class in which if you pass the name of a file of the given format it will give you the required
	// questions output
	Magic check("A-small-attempt0.in");

}