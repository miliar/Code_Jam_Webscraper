#include<iostream>
#include<fstream>
#define SIZE 4
using namespace std;

int main ()
{
    int array1[SIZE][SIZE], array2[SIZE][SIZE], cases, row1, row2;
    ifstream infile;
    ofstream outfile;
    outfile.open("output.txt");
    infile.open("Input.txt");
    if(infile.is_open())
    {
    infile >> cases;

        for(int x=0; x<cases; x++)
        {
        outfile << "Case #" << x+1 << ": ";
        infile >> row1;
        for(int i=0; i<SIZE; i++)
        for(int j=0; j<SIZE; j++)
        infile >> array1[i][j];
        
        infile >> row2;
        for(int i=0; i<SIZE; i++)
        for(int j=0; j<SIZE; j++)
        infile >> array2[i][j];

        row1--;
        row2--;
        int count=0, num;
        for(int col=0; col<SIZE; col++)
        for(int j=0; j<SIZE; j++)
        if(array1[row1][col]==array2[row2][j])
        {
                                   num = array1[row1][col];
                                   count++;
        }//end if
            
        if(count==0)
             outfile << "Volunteer cheated!" << endl;
        else if(count==1)
             outfile << num << endl;
        else
             outfile << "Bad magician!" << endl;
        }//end for loop for cases
        
    infile.close();
    }//end if loop for infile.is_open
    else
    outfile << "File cannot be opened!" << endl;
    
    return 0;
}
