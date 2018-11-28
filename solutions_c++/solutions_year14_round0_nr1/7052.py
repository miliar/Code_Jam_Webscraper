//Google code jam 2014 Magic Trick

#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <sstream>
#include <cmath>
#include <iomanip>
#include <set>

using namespace std;

int TEST_CASES;
set <int> riga;
int main()
{
    cin >> TEST_CASES;
    for (int c = 0; c < TEST_CASES; c++)
    {
		int row, cont = 0, carta;
		cin >> row;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				int temp;
				cin >> temp;
				if (i==row-1)
					riga.insert(temp);
			}
        cin >> row;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				int temp;
				cin >> temp;
				if (i==row-1)
					if (riga.find(temp) != riga.end())
					{
                        cont++;
                        carta = temp;
                    }
			}
        cout << "Case #" << c+1 << ": ";
        if (cont == 0)
            cout << "Volunteer cheated!" << endl;
        else if (cont > 1)
            cout << "Bad magician!" << endl;
        else
            cout << carta << endl;
        riga.clear();
    }
    return 0;
}
