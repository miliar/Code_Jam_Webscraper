#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int t;
    ifstream fe("A-small-attempt1.in");
    ofstream fs("A-small-attempt0.out");
    fe>>t;
    for (int q=1; q<=t; q++)
    {
        int f1;
        fe>>f1;
        int mat[4][4];
        for (int a=0; a<4; a++)
        {
            for (int w=0; w<4; w++)
            {
                fe>>mat[a][w];
            }
        }
        int f2;
        fe>>f2;
        int mat2[4][4];
        for (int a=0; a<4; a++)
        {
            for (int w=0; w<4; w++)
            {
                fe>>mat2[a][w];
            }
        }
        int c=0,aux;
        for (int z=0; z<4; z++)
        {
            for (int w=0; w<4; w++)
            {
                if (mat[f1-1][z]==mat2[f2-1][w])
                {
                    aux=mat[f1-1][z];
                    c++;
                }
            }
        }
        fs<<"Case #"<<q<<": ";
        if (c==1)
        {
            fs<<aux<<endl;
        }
        else if (c>1)
        {
            fs<<"Bad magician!"<<endl;
        }
        else if (c==0)
        {
            fs<<"Volunteer cheated!"<<endl;
        }
    }
    return 0;
}
