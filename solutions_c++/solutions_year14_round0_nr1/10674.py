#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int t_case, c_case;
    int c1,c2;
    int arr1[4][4], arr2[4][4];
    int temp1[4];
    int match=0;

    ifstream in("A-small-attempt2.in");
    //ifstream in("in.txt");
    ofstream out("out.out");

    in>>t_case;

    for(int c_case=0;c_case<t_case;c_case++)
    {
        for(int j=0;j<4;j++)
        {
            temp1[j]=0;
        }
        in>>c1;
        for(int row=0; row<4;row++)
        {
            for(int col=0;col<4;col++)
            {
                in>>arr1[row][col];
            }
        }

        in>>c2;

        for(int row=0; row<4;row++)
        {
            for(int col=0;col<4;col++)
            {
                in>>arr2[row][col];
            }
        }


        match=0;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(arr1[c1-1][i]==arr2[c2-1][j])
                {
                    temp1[match]=arr1[c1-1][i];
                    match++;
                }
            }
        }
        if(match==1)
        {
            out<<"Case #"<< c_case+1<<": "<<temp1[0];
        }
        else if(match==0)
        {
            out<<"Case #"<< c_case+1<<": "<<"Volunteer cheated!";
        }
        else if(match>1)
        {
            out<<"Case #"<< c_case+1<<": "<<"Bad magician!";
        }
        //if(c_case<99)
            out<<endl;
    }

	return 0;
}
