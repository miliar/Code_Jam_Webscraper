#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int judge;
    int judgearray[4];
    int T;
    int row1;
    int row2;
    int temp;
    int i,j,k;
    int A[4][4];
    int B[4][4];
    ifstream file1;
    file1.open("A-small-attempt3.in");
    file1>>T;
    ofstream file2;
    file2.open("out.out");
    for(i=0;i<T;i++)
    {
        judge=0;
        file1>>row1;
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
            {
                file1>>temp;
                A[j][k]=temp;
            }
        file1>>row2;
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
            {
                file1>>temp;
                B[j][k]=temp;
            }
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
            {
                if(A[row1-1][j]==B[row2-1][k])
                {
                    judgearray[judge]=A[row1-1][j];
                    judge++;
                }
            }
        if(judge==0)
            file2<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        if(judge==1)
            file2<<"Case #"<<i+1<<": "<<judgearray[0]<<endl;
        if(judge>1)
            file2<<"Case #"<<i+1<<": Bad magician!"<<endl;
    }
    file1.close();
    file2.close();
    return 0;
}
