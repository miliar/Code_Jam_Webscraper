#include <iostream>

using namespace std;

int main()
{

    short case1[4][4];
    short case2[4][4];
    short t;
    short row1;
    short row2;
    short result[100];
    short flag=0;
    short iter=0;
    short value=0;

    cin >> t;
    for(short i=0;i<t;i++)
    {
        cin >> row1;
        for(short j=0;j<4;j++)
        {
                for(short k=0;k<4;k++)
                {
                    cin >> case1[j][k];
                }
        }


        cin >> row2;
        for(short j=0;j<4;j++)
        {
                for(short k=0;k<4;k++)
                {
                    cin >> case2[j][k];
                }
        }

        flag=0;
        for(short l=0;l<4;l++)
        {
            for(short m=0;m<4;m++)
            {
                if(case1[row1-1][l]==case2[row2-1][m])
                {
                    flag++;
                    value=case1[row1-1][l];
                }
            }
        }
        if(flag==1)
        {
                result[iter]=value;
        }
        else if(flag>1)
        {
            result[iter]=0;
        }
        else if(flag==0)
        {
            result[iter]=-1;
        }
        iter++;
    }

    for(short n=0;n<t;n++)
    {
        cout << "Case #" << n+1 << ": ";
        if(result[n]==0)
        {
            cout << "Bad magician!" << endl;
            continue;
        }
        else if(result[n]==-1)
        {
            cout << "Volunteer cheated!" << endl;
        }
        else
        {
            cout << result[n] << endl;
        }

    }
    return 0;
}
