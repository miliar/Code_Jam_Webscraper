#include<iostream>
#include<fstream>
#include<map>

using namespace std;

int magicTrick(int choices[], int arr1[4][4], int arr2[4][4])
{
    map<int,bool> rows;
    int i,cnt = -1;
    for(i = 0; i < 4; i++)
    {
        rows[arr1[choices[0]-1][i]] = true;
    }
    for(i = 0; i < 4; i++)
    {
        if (rows.find(arr2[choices[1]-1][i]) != rows.end())
        {
            if (cnt == -1)
            {
                cnt = i;
            }
            else
            {
                return -1;
            }
        }
    }
    if (cnt == -1)
    {
        return -2;
    }
    return cnt;
}

int main(int argc, char* argv[])
{
    ifstream test;
    ofstream res;
    int cases, choices[2], arr1[4][4], arr2[4][4], out;
    int i, j ,c;
    if (argc != 2)
    {
        cout << "<obj file> <testFile>";
        return 0;
    }
    test.open(argv[1]);
    res.open("magicTrickRes");
    test >> cases;
    for (c = 1; c <= cases; c++)
    {
        test >> choices[0];
        for ( j = 0; j < 4; j++)
        {
            for (i = 0; i < 4; i++)
            {
                test >> arr1[j][i];
            }
        }
        test >> choices[1];
        for ( j = 0; j < 4; j++)
        {
            for (i = 0; i < 4; i++)
            {
                test >> arr2[j][i];
            }
        }
        out = magicTrick(choices, arr1, arr2);
        if (out == -1)
        {
            res << "Case #" << c << ": Bad magician!\n";
        }
        else if (out == -2)
        {
            res << "Case #" << c << ": Volunteer cheated!\n";
        }
        else
        {
            res << "Case #" << c << ": " << arr2[choices[1]-1][out] << "\n";
        }
    }
    return 0;
} 
        
    
    
        
