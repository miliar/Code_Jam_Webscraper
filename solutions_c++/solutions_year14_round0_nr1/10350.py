#include<iostream>
#include<cstdlib>

using namespace std;
int main()
{
    int c;
    int num;
    int n;
    int r1,r2;
    int a[4][4];
    int b[4][4];
    cin >> n;
    for(int i=0;i<n;i++)
    {
        c = 0;
        cin >> r1;
        r1--;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                cin >> a[j][k];
        cin >> r2;
        r2--;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                cin >> b[j][k];

        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                if(a[r1][j] == b[r2][k])
                {
                    num = a[r1][j];
                    c++;
                }

        if(c==0)
            cout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
        else if(c==1)
            cout << "Case #" << i+1 << ": " << num << endl;
        else
            cout << "Case #" << i+1 << ": " << "Bad magician!" << endl;

    }
    return 0;
}

