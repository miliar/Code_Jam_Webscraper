#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <math.h>
using namespace std;

int main (int argc, char * const argv[])
{
	freopen("input1.txt", "rt", stdin);
	freopen("output1.txt", "wt", stdout);
	
	int T;
	cin >> T;
	
    int row1[4], row2[4];
    for(int t = 0; t < T; t++)
    {
        int A1;
        cin >> A1;
        
        int start = (A1-1) * 4, temp;
        for (int i = 0; i < 16; i++)
        {
            if (i >= start && i < start + 4)
                cin >> row1[i-start];
            else
                cin >> temp;
        }
        
        int A2;
        cin >> A2;
        
        start = (A2-1) * 4;
        for (int i = 0; i < 16; i++)
        {
            if (i >= start && i < start + 4)
                cin >> row2[i-start];
            else
                cin >> temp;
        }
        
        int count = 0, v;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                if (row1[i] == row2[j])
                {
                    count++;
                    v = row1[i];
                }
            }
        }
        
        cout << "Case #" << t+1 << ": ";
        if (count == 1)
            cout << v;
        else if (count > 1)
            cout << "Bad magician!";
        else
            cout << "Volunteer cheated!";
        cout << endl;
        
	}
	
	return 0;
}

