#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const int MAX = 100 + 10;

int a[MAX][MAX];
int r[MAX];
int c[MAX];

int main()
{
	int n;
	cin >> n;
    int n0 = n;
    while(n-->0)
    {
        bool b = true;
        int x, y;
        cin >> y >> x;
        for(int j = 0; j < y; j++)
            for(int i = 0; i < x; i++)
                cin >> a[i][j];

        for(int i = 0; i < x; i++)
            c[i] = -1;

        for(int j = 0; j < y; j++)
            r[j] = -1;

        for(int i = 0; i < x; i++)
            for(int j = 0; j < y; j++)
            {
                r[j] = max(r[j], a[i][j]);
                c[i] = max(c[i], a[i][j]);
            }
        for(int i = 0; i < x; i++)
            for(int j = 0; j < y; j++)
                if((a[i][j] < r[j]) && (a[i][j] < c[i]))
                    b = false;

        if(b)
            cout << "Case #" << n0 - n << ": YES" << endl;
        else
            cout << "Case #" << n0 - n << ": NO" << endl;
    }
	return 0;
}
