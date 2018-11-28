#include<conio.h>
#include<iostream>
#include<fstream>
using namespace std;

ifstream in("text.txt");
ofstream out("result.txt");

class Magic{
	
	int row1, row2;
	int arr1[4][4];
	int arr2[4][4];
  public:
	  void getData()
	  {
		  in >> row1;
		  --row1;
		  for (int i = 0; i < 4; i++)
		  {
			  for (int j = 0; j < 4; j++)
			  {
				  in >> arr1[i][j];
			  }
		  }
		  in >> row2;
		  --row2;
		  for (int i = 0; i < 4; i++)
		  {
			  for (int j = 0; j < 4; j++)
			  {
				  in >> arr2[i][j];
			  }
		  }
	  }
	  void check(int &caseNo);
	//  void show(int &caseNo,string msg);
};

int main()
{
	static int T = 100;
	Magic caseArr[100];
	int noc;
	in >> noc;
	int i;
	for (i = 0; i < noc; i++)
	{
		caseArr[i].getData();
	}
	for (i = 0; i < noc; i++)
	{
		caseArr[i].check(i);
	}
/*	for (i = 0; i < noc; i++)
	{
		out << endl << "Case #" << i + 1 << ":\t";
			caseArr[i].show();
	}
*/
//	_getch();
	return 0;
}

void Magic::check(int &caseNo)
{	
	int flag = 0;
	int choice=17;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (arr1[row1][i] == arr2[row2][j])
			{
				choice = arr2[row2][j];
				++flag ;
			}
		}
	}
	
	if (flag == 0)
	{
		out << "Case #" << caseNo + 1 << ": Volunteer cheated!" << endl;
	}
	else if (flag == 1)
	{
		out << "Case #" << caseNo + 1 << ": " << choice << endl;
	}

	else
		out << "Case #" << caseNo + 1 << ": Bad magician!" << endl;
}
//void Magic::show(int &caseNo, string msg)
