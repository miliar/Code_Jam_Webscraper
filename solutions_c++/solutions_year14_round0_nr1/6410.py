#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream infile;
    ofstream outfile;
    infile.open("A-small-attempt1.in");
    outfile.open("A-small-attempt1.out");
    int t , n , i , j  , z, k[2][16] , a1 , a2 , f , pos;
    while(infile >> t)
    {
        for(i = 0 ; i < t ; i++)
        {
            f = 0;pos = 0;
            infile >> a1;
            for(j = 0 ; j < 16 ; j++)
                infile >> k[0][j];
            infile >> a2;
            for(j = 0 ; j < 16 ; j++)
                infile >> k[1][j];
            for(j = (a1 - 1) * 4 ; j < a1 * 4 ; j++)
            {
                for(z = (a2 - 1) * 4 ; z < a2 * 4 ; z++)
                {
                    if (k[0][j] == k[1][z])
                    {
                        f++;
                        pos = k[0][j];
                    }
                }
            }
            if(f == 1)
                outfile << "Case #" << i+1 << ": " << pos << endl;
            else if(f > 1)
                outfile << "Case #" << i+1 << ": Bad magician!" << endl;
            else
                outfile << "Case #" << i+1 << ": Volunteer cheated!" << endl;
        }
    }
    infile.close();
    outfile.close();
    return 0;
}
