/*Case #1: 7
Case #2: Bad magician!
Case #3: Volunteer cheated!*/
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ofstream fout("c:\\me.txt");
    int num,i,j,k;
    cin>>num;
    int square[num][2][4][4];
    int line[num][2];
    int temp[num][2][4];
    int counter;
    int outbuff;
    for(i=0;i<num;i++)
    {
        counter=0;
        cin>>line[i][0];
        for(j=0;j<4;j++)
        for(k=0;k<4;k++)
        {

           cin>>square[i][0][j][k];
           if(j==line[i][0]-1)
           temp[i][0][k]=square[i][0][j][k];
        }

        cin>>line[i][1];
        for(j=0;j<4;j++)
        for(k=0;k<4;k++)
        {

           cin>>square[i][1][j][k];
           if(j==line[i][1]-1)
           temp[i][1][k]=square[i][1][j][k];
        }
        for(j=0;j<4;j++)
        for(k=0;k<4;k++)
        {
            if(temp[i][0][j]==temp[i][1][k])
            {
                counter++;
                outbuff=temp[i][0][j];
            }
        }
    if(counter==1)
    fout<<"Case #"<<i+1<<": "<<outbuff<<endl;
    else if(counter==0)
    fout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
    else
    fout<<"Case #"<<i+1<<": Bad magician!"<<endl;
    }

return 0;

}




