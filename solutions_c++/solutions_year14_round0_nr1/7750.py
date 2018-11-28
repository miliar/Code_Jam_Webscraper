#include<iostream>
#include<fstream>
#define SIZE 4

using namespace std;

int main()
{
    ifstream infile;
    infile.open("Input.txt");
    ofstream outfile;
    outfile.open("Output.txt");
    int cases;
    infile >> cases;
    for (int i=0;i<cases;i++)
    {
        outfile << "Case #" << i+1 << ": ";
        int count=0, out=0, arr1[SIZE][SIZE], arr2[SIZE][SIZE], rownum1, rownum2, temp1[SIZE], temp2[SIZE];
        infile >> rownum1;
        for (int j=0;j<SIZE;j++)
        {
            for (int k=0;k<SIZE;k++)
            {
                infile >> arr1[j][k];
            }
        }
        infile >> rownum2;
        for (int j=0;j<SIZE;j++)
        {
            for (int k=0;k<SIZE;k++)
            {
                infile >> arr2[j][k];
            }
        }
        for (int k=0;k<SIZE;k++)
        {
            temp1[k]=arr1[rownum1-1][k];
            temp2[k]=arr2[rownum2-1][k];
        }
        for (int k=0;k<SIZE;k++)
        {
            for (int j=0;j<SIZE;j++)
            {
                if (temp1[k]==temp2[j]){
                out=temp1[k];
                count++;
                }
                else
                if (out <= 0)
                out=-1;
            }
        }
        if (count==1 && out!=-1)
        outfile << out << endl;
        else if (out==-1)
        outfile << "Volunteer cheated!" << endl;
        else if (count > 1)
        outfile << "Bad magician!" << endl;
        }
    infile.close();
    outfile.close();
    return 0;
}
