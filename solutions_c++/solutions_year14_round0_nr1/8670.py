#include <iostream>
#include <fstream>


using namespace std;

int main()
{
    ofstream fout;
    fout.open("a.txt",ios::out);
    int t;
    int t1=1;
    cin>>t;
    while(t1<=t)
    {
        int r1,row1;
        cin>>r1;
        row1=r1-1;
        int arr1[4][4];
        int check[16];
        for(int k=0;k<16;k++)
        {
            check[k]=k+1;
        }
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>arr1[i][j];
                if(i==row1)
                {
                    int m=arr1[i][j]-1;
                    check[m]=-1;
                }

            }
        }
        int arr2[4][4];
        int r2;
        cin>>r2;
        int row2=r2-1;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>arr2[i][j];
                if(i==row2)
                {
                    int m=arr2[i][j]-1;
                    check[m]=check[m]+1;
                }

            }
        }


        int count=0;
        int out;
           for(int k=0;k<16;k++)
        {


                if(check[k]==0)
                {
                    if(count==0)
                    {
                        out=k+1;
                    }
                    count=count+1;
                }

        }


        if(count==0)
        {
            fout<<"Case #"<<t1<<":"<<" "<<"Volunteer cheated!"<<endl;
        }
        if(count==1)
        {
            fout<<"Case #"<<t1<<":"<<" "<<out<<endl;
        }
        if(count>1)
        {
            fout<<"Case #"<<t1<<":"<<" "<<"Bad magician!"<<endl;
        }


        t1++;
    }
    return 0;
}
