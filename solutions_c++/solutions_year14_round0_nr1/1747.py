#include <iostream>
#include <sstream>

using namespace std;

int main() {
    int rows = 4;
    int cases;
    int use1;
    int use2;
    int casenum = 1;
    string aline, bline;
    int in1[16];
    int in2[16];
    int possibilities[8];
    string result;
    cin >> cases;
    while (cases--)
    {
        cin >> use1;
        int i = 0;
        for (i = 0; i < 16; i++)
            cin >> in1[i];
        cin >> use2;
        for (i = 0; i < 16; i++)
            cin >> in2[i];

        use1 = use1-1;
        use2 = use2-1;
        int add = 0;
        for (i = 0; i < 4; i++) 
        {
            add = 4 * use1 + i;
            possibilities[i] = in1[add];
        }

        for (i = 4; i < 8; i++)
        {
            add = 4 * use2 + (i-4);
            possibilities[i] = in2[add];
        }

		//bubblesort
		int j = 0;
		int swap;
		
		for (i = 0; i < 8-1; i++)
			for (j = 0; j < 8-i-1; j++)
			{
				if (possibilities[j] > possibilities[j+1])
				{
					swap = possibilities[j];
					possibilities[j] = possibilities[j+1];
					possibilities[j+1] = swap;
				}
			}
		//Sorted.
		
		int ans = 0;
		int paircount = 0;
		
		for (i = 0; i < 7; i++)
		{
			if (possibilities[i] == possibilities[i+1])
			{
				paircount++;
				ans = possibilities[i];
			}
		}
		if (paircount > 1)
			result = "Bad magician!";
		else if (paircount == 0)
			result = "Volunteer cheated!";
		else
        {
            stringstream s;
            s << ans;
			result = s.str();
        }
		
        cout << "Case #" << casenum++ << ": " << result << endl;
    }
    return 0;
}

