#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream infile("A-small-attempt0.in");
    ofstream outfile("A-small-attempt0.out");
    int T;
    infile >> T;

    int r1,r2;
    int arr1[4][4];
    int arr2[4][4];

    //i is the row

    for(int t=0; t<T; t++)
    {
        infile >> r1;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                infile >> arr1[i][j];

        infile >> r2;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                infile >> arr2[i][j];

        int count=0;
        int index=-1;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                if(arr1[r1-1][i]==arr2[r2-1][j])
                {
                    count++;
                    index = i;
                }
            }
        }

        outfile << "Case #" << t+1 << ": ";
        if(count==0)
            outfile << "Volunteer cheated!" << endl;
        else if(count==1)
            outfile << arr1[r1-1][index] << endl;
        else
            outfile << "Bad magician!" << endl;

    }
    infile.close();
    outfile.close();
    return 0;
}
