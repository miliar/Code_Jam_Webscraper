#include<fstream>
using namespace std;
int main()
{
    int t, an1, an2, mat1[5][5], mat2[5][5], num, value;
    ifstream fin;
    fin.open("A-small-attempt2.in");
    ofstream fout;
    fout.open("A-small-attempt2.out");
    fin>>t;
    for(int i=1;i<=t;i++)
    {
            fin>>an1;
            for(int j=1;j<=4;j++)
                    for(int k=1;k<=4;k++)
                            fin>>mat1[j][k];
            fin>>an2;
            for(int j=1;j<=4;j++)
                    for(int k=1;k<=4;k++)
                            fin>>mat2[j][k];
            fout<<"Case #"<<i<<": ";
            num=0;
            value=0;
            for(int j=1;j<=4;j++)
            {
                    for(int k=1;k<=4;k++)
                    {
                            if(mat1[an1][j]==mat2[an2][k])
                            {
                                           num++;
                                           value = mat1[an1][j];
                            }
                    }
            }
            if(num==1)
                      fout<<value<<endl;
            else if(num==0)
                      fout<<"Volunteer cheated!"<<endl;
            else
                      fout<<"Bad magician!"<<endl;
    }
    fin.close();
    fout.close();
    //system("PAUSE");
    return 0;
}
