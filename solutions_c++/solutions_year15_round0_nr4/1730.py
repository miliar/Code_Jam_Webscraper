#include <iostream>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    freopen("D:\\GoogleCodeJam\\in.txt","r",stdin);
    freopen("D:\\GoogleCodeJam\\out.txt","w",stdout);

    int TestNum = 0;
    cin >> TestNum;
    for (int testCase = 0;testCase < TestNum;testCase++)
	{
        int X, R, C;

        cin >> X >> R >> C;
        bool canFill = false;

        int col = R > C? R : C;
        int row = R < C? R : C;

        if (X == 1 && col > 0 && row > 0)
            canFill = true;

        if (X == 2 && col >= 2 && row >= 1 && col*row >=2 && col*row % 2==0)
            canFill = true;

        if (X == 3 && col >= 3 && row >= 2 && col*row >=3 && col*row % 3==0)
            canFill = true;

        if (X == 4 && col >= 4 && row >= 3 && col*row >=4 && col*row % 4==0)
            canFill = true;

        if (X == 5 && col >= 5 && row >= 4 && col*row >=5 && col*row % 5==0)
            canFill = true;

        if (X == 6 && col >= 6 && row >= 4 && col*row >=6 && col*row % 6==0)
            canFill = true;

        if (X >= 7) canFill = false;

        if (testCase != 0) cout << endl;
        cout << "Case #" << (testCase + 1) << ": " << ( canFill ? "GABRIEL" : "RICHARD");
	}
    return 0;
}
