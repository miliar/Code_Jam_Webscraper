#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    fstream f1, f2;
    f1.open("A-small.in", ios::in);
    f2.open("output.txt", ios::out | ios::binary);
    int num;
    f1>>num;
    int mat1[4][4];
    int mat2[4][4];
    int r1, r2;
    int match, flag = 0;
    for (int x=0; x<num; x++)
    {
        flag = 0;
        f2<<"Case #"<<(x+1)<<": ";
        f1>>r1;
        cout<<r1<<endl;
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                f1>>mat1[i][j];
                cout<<mat1[i][j]<<" ";
            }
            cout<<endl;
        }
        f1>>r2;
        cout<<r2<<endl;
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                f1>>mat2[i][j];
                cout<<mat2[i][j]<<" ";
            }
            cout<<endl;
        }
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                if (mat2[r2-1][j] == mat1[r1-1][i])
                {
                    flag++;
                    match = mat1[r1-1][i];
                }
            }
        }
        if (flag==0)
            f2<<"Volunteer cheated!"<<endl;
        else if (flag==1)
            f2<<match<<endl;
        else if(flag>1)
            f2<<"Bad magician!"<<endl;
    }
    f1.close();
    f2.close();
    return 0;
}
