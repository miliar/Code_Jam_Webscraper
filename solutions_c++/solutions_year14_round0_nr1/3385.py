#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int n,T,row,val,arr1[4], arr2[4];
    int c1,c2,c3,c4;

    cin >> T;
    n=1;
    while(n <= T)
    {
        cin >> row;
        for(int i=1; i<=4; i++)
        {
            cin >> c1 >> c2 >> c3 >> c4;

            if(i == row)
            {
                arr1[0] = c1;
                arr1[1] = c2;
                arr1[2] = c3;
                arr1[3] = c4;
            }
        }

        cin >> row;
        for(int i=1; i<=4; i++)
        {
            cin >> c1 >> c2 >> c3 >> c4;

            if(i == row)
            {
                arr2[0] = c1;
                arr2[1] = c2;
                arr2[2] = c3;
                arr2[3] = c4;
            }
        }

        int cnt = 0;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                if(arr1[i] == arr2[j])
                {
                    val = arr1[i];
                    cnt++;
                }
            }
        }

        if(0 == cnt)
            cout << "Case #" << n << ": Volunteer cheated!" << endl;
        else if(1 == cnt)
            cout << "Case #" << n << ": " << val << endl;
        else
            cout << "Case #" << n << ": Bad magician!" << endl;

        n++;
    }
    return 0;
}
