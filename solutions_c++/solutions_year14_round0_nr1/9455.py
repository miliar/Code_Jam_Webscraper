#include<iostream>

using namespace std;

int main()
{
    int num = 0;
    int a;
    int b;
    int arr1[4][4];
    int arr2[4][4];
    int result;

    cin >> num;

    for (int i = 0; i < num; i++)
    {
        result = 0;
        cin >> a;
        a--;
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                cin >> arr1[j][k];
            }
        }
        cin >> b;
        b--;
        for (int j = 0; j < 4; j++)
        {   
            for (int k = 0; k < 4; k++)
            {   
                cin >> arr2[j][k];
            }
        }
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                if (arr1[a][j] == arr2[b][k])
                {
                    if (result == 0)
                    {
                        result = arr1[a][j];
                    }
                    else if (result != -1)
                    {
                        cout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
                        result = -1;
                    }
                }
            }
        }
        if (result == 0 )
        {
            cout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
        }
        else if (result != -1)
        {
            cout << "Case #" << i+1 << ": " << result << endl;
        }
    }
    return 0;
}
