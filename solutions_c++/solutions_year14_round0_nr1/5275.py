#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
using namespace std;


void solve()
{
     int nRow1, nRow2;
     vector<int> nArr;
     cin >> nRow1;
     int nTemp;
     for (int i = 0; i < 4; i++)
     {
         for (int j = 0; j < 4; j++)
         {
             cin >> nTemp;
             if (i+1 == nRow1)
             {
                     nArr.push_back(nTemp); 
             }
         }
     }
     vector<int> nArr2;
     cin >> nRow2;
     for (int i = 0; i < 4; i++)
     {
         for (int j = 0; j < 4; j++)
         {
             cin >> nTemp;
             if (i+1 == nRow2)
             {
                     for (int k = 0; k < nArr.size(); k++)
                     {
                         if (nArr[k] == nTemp)
                         {
                                   nArr2.push_back(nTemp);
                                   break;  
                         }
                     }
             }
         }
     }

		if (nArr2.size() == 0)
		{
                 cout << "Volunteer cheated!" << endl;          
        }

        else if (nArr2.size() == 1)
		{
                 cout << nArr2[0] << endl;          
        }  
        else
        {
                 cout << "Bad magician!" << endl;  
        }   
	
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int TestCase;
	cin >> TestCase;
	for (int CaseID = 1; CaseID <= TestCase; CaseID ++)
	{
		cout << "Case #" << CaseID << ": ";
		solve();
	}
	return 0;
}

