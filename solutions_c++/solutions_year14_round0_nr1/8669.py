#include <iostream>
#include <fstream>
using namespace std;
int main()
{
      ofstream myfile;
      ifstream infile;
      infile.open("input.in");
     myfile.open ("out.out");
     int n;
     int array1[4][4],array2[4][4];
     int ans1,ans2;
    infile>>n;
    for(int t=0;t<n;t++)
    {
    int count=0;
    int temp=0;
     infile>>ans1;
    for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
        infile>>array1[i][j];

        infile>>ans2;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        infile>>array2[i][j];

        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
            if(array1[ans1-1][i]==array2[ans2-1][j])
            {
                count++;
                temp=i;
            }

        }

        if (count==0)
        myfile<< "Case #" << t+1<< ": " << "Volunteer cheated!"<< endl;
        else if (count==1)
        myfile<< "Case #" << t+1<< ": " << array1[ans1-1][temp]<< endl;
        else
         myfile<< "Case #" << t+1<< ": " << "Bad magician!"<< endl;



}
}
