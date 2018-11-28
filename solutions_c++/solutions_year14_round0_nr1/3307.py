#include<iostream>
#include<fstream>
#include<cmath>

using namespace std;

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small-attempt0.out");
    int T;
    
    fin >> T;
    for (int t=0;t<T;t++ )
    {
        int A1,A2;
        int R1[4][4];
        int R2[4][4];
                
        fin >>A1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                fin >> R1[i][j];
            }
        fin >>A2;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                fin >> R2[i][j];
            }
        int Count = 0;
        int Match = 0;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                if( R1[A1-1][i] == R2[A2-1][j] )
                {
                    Count = Count+1;
                    Match = R1[A1-1][i]; 
                }
            }
        if (Count == 0)
            fout << "Case #" << t+1 << ": " << "Volunteer cheated!" << endl;
        if (Count == 1)
            fout << "Case #" << t+1 << ": " << Match << endl;
        if (Count > 1)
            fout << "Case #" << t+1 << ": " << "Bad magician!" << endl;
    }     
    fin.close();
    fout.close();
    
    return 0;
}
