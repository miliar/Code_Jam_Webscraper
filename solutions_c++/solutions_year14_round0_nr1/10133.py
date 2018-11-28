#include<iostream>
#include<fstream>
#include<cstdlib>
using namespace std;

int main()
{
    int t;
    ifstream in ("A-small-attempt0.in");
    ofstream out ("output.txt");
    in>>t;


    for(int i=1;i<=t;i++)
{
    int row1,row2,counter=0,re;
    int a1[4][4];
    int a2[4][4];
    in>>row1;
    for(int j=0;j<4;j++)
    {
        for (int k=0;k<4;k++)
        {
            int temp;
            in>>temp;
            a1[j][k]=temp;
        }
    }
    in>>row2;
    for(int j=0;j<4;j++)
    {
        for (int k=0;k<4;k++)
        {
            int temp;
            in>>temp;
            a2[j][k]=temp;
        }
    }
    //bdaeet elmo8arani
     for (int q=0;q<4;q++)
    {

        for(int c=0;c<4;c++)

            if(a1[row1-1][q]==a2[row2-1][c])
               {
                   counter ++;
                  if(counter==0)
                    continue;
                else if(counter > 1){
                    break;
                }
                  else
                    re=a1[row1-1][q];
               }
    }


        if (counter ==0)
        out<<"Case  #"<<i<<": Volunteer cheated!"<<endl;//7ali eaqam 2
        else
        if(counter==1)
        out<<"Case  #"<<i<<": "<<re<<endl;
        else
        out<<"Case  #"<<i<<": Bad magician!"<<endl;//7ali 3





}

return 0;
}
