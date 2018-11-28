#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int lawn[100][100];

int main()
{
    int case_namber;
    cin >> case_namber;

    for(int current = 1; current <= case_namber; ++current)
    {
        int rows;
        int cols;

        cin >> rows;
        cin >> cols;

        for(int i = 0; i < rows; ++i)
        {
            for(int j = 0; j < cols; ++j)
            {
                cin >> lawn[i][j];
            }
        }

        bool able = true;

        if(rows != 1 && cols != 1)
        {
            for(int i = 0; i < rows; ++i)
            {
                for(int j = 0; j < cols; ++j)
                {
                    int height = lawn[i][j];
                    bool left = true;
                    bool right = true;
                    bool top = true;
                    bool bottom = true;

                    for(int k = j-1; k >= 0; --k) // left
                    {
                        if(lawn[i][k] > height) {left = false; break;}
                    }
                    for(int k = j+1; k < cols; ++k) // right
                    {
                        if(lawn[i][k] > height) {right = false; break;}
                    }
                    for(int k = i-1; k >= 0; --k) // top
                    {
                        if(lawn[k][j] > height) {top = false; break;}
                    }
                    for(int k = i+1; k < rows; ++k) // bottom
                    {
                        if(lawn[k][j] > height) {bottom = false; break;}
                    }

                    able = false;
                    if(left && right) able = true;
                    if(top && bottom) able = true;

                    if(!able) break;
                }
                if(!able) break;
            }
        }

        cout << "Case #" << current << ": ";
        if(able) cout << "YES";
        else cout << "NO";
        cout << endl;
    }
    return 0;
}
