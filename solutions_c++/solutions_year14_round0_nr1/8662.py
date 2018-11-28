#include <iostream> 
#include <fstream> 
#include <iomanip> 
#include <algorithm> 
  
using namespace std; 
  
void readVec(ifstream & ifs, int * const v)
{
    ifs>>v[0]>>v[1]>>v[2]>>v[3];
}

void readMatrix(ifstream & ifs, int mat[][4])
{
    readVec(ifs, mat[0]);
    readVec(ifs, mat[1]);
    readVec(ifs, mat[2]);
    readVec(ifs, mat[3]);
}

int main()
{
    ifstream fin("input.txt");
	ofstream ofs("output.txt");
    int m1[4][4];
    int m2[4][4];
    int r1;
    int r2;
    int n;
    fin>>n;
    for(int i=0; i<n; i++)
    {
        fin>>r1;
        readMatrix(fin, m1);
        fin>>r2;
        readMatrix(fin, m2);
		
		r1--;
		r2--;
        int dup = 0;
        int num = -1;
        for(int j=0; j<4; j++)
            for(int k=0; k<4; k++)
                if(m1[r1][j] == m2[r2][k])
                {
                    num = m1[r1][j];
                    dup++;
                }
                
        ofs<<"Case #"<<i+1<<": ";    
        if(dup == 0)
            ofs<<"Volunteer cheated!";
        else if(dup == 1)
            ofs<<num;
        else
            ofs<<"Bad magician!";
            
        ofs<<endl;
    }
   return 0;
}