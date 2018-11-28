#include <fstream>
using namespace std;

int main()
{
    ifstream Fin;
    ofstream Fout;
    Fin.open("A-small-attempt0.in");
    Fout.open("output.txt");
    int T,i,j,k,a1,a2,sum,x;
    int A[4][4], B[4][4];
    int Temp[4];
    Fin>>T;
    for (i=0; i<T; i++)
    {
        Fin>>a1;
        for (j=0; j<4; j++)
        {
            for (k=0; k<4; k++)
              Fin>>A[j][k];
        }
        Fin>>a2;
        for (j=0; j<4; j++)
        {
            for (k=0; k<4; k++)
             Fin>>B[j][k];
        }
        sum=0;
        for (j=0; j<4; j++)
        {
            x=A[a1-1][j];
            for (k=0; k<4; k++)
            { 
              if (B[a2-1][k]==x)
              { 
                Temp[sum]=x;
                sum=sum+1;
              }
            }
        }
        if (sum==1)
         Fout<<"Case #"<<i+1<<": "<<Temp[0]<<endl;
        else
        {
            if (sum==0)
             Fout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
            else
             Fout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
        }
    }
    Fin.close();
    Fout.close();
    return 0;
}
