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
#include <iomanip> 
using namespace std;


double solve()
{
     double dc, df, dx;
     cin >> dc >> df >> dx;
     
     double dCurTime = 0;
     int nFarmSize = 0;
     
     if (dx<=dc)
     {
        return dx/2.0;
     }
     
     double dTimeV = dc/df;
     
     while (true)
     {
            dCurTime += dc/(2.0+df*nFarmSize);
            double dLeftTime = (dx-dc)/(2.0+df*nFarmSize);
            if (dLeftTime <= dTimeV)
            {
                return dCurTime+dLeftTime;
            }
            nFarmSize++;
     }	
}

int main()
{
	freopen("in.txt", "r", stdin);
    cout<<setiosflags(ios::fixed)<< setiosflags(ios_base::showpoint)<< setprecision(10);
	freopen("out.txt", "w", stdout);

	int TestCase;
	cin >> TestCase;
	for (int CaseID = 1; CaseID <= TestCase; CaseID ++)
	{
		cout << "Case #" << CaseID << ": ";
		cout << solve() << endl; 
	}
	return 0;
}

