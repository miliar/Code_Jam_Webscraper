#include <fstream>
#include <iostream>

int main ()
{
    std::ifstream fin("magician.in");
    std::ofstream fout("magician.out");
    
    int t, x;
    fin>>t;
    for(int i=0;i<t;i++)
    {
        int l1;
        int row1[4];
        fin>>l1;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                fin>>x; 
                if(j+1==l1)
                {
                    row1[k]=x;
                } 
            }
        }

        int l2;
        int row2[4];
        fin>>l2;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                fin>>x; 
                if(j+1==l2)
                {
                    row2[k]=x;
                } 
            }
        }
        int count=0;

        int that;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                if(row1[j]==row2[k])
                {
                    count++;
                    that = row1[j];
                }
            }
        }
        fout<<"Case #"<<i+1<<": ";
        if(count==1)
        {
            fout<<that;
        }
        else if(count ==0)
        {
            fout<<"Volunteer cheated!";
        }
        else //more
        {
            fout<<"Bad magician!";
        }
        fout<<std::endl;
    }
    return 0;
}
