#include <iostream>
#include <fstream>

using namespace std;

void validate(int,int a[4],int b[4]);

int main()
{
    int T,ans1,ans2,arr1[4][4],arr2[4][4],check[4],check2[4];
    fstream file;
    file.open("input.txt",ios::in);
    if(!file)
    {
        cout<<"\nError opening the file";
    }
    else
    {
        file>>T;
        for(int i=1;i<=T;i++)
        {
            file>>ans1;
            for(int j=0;j<4;j++)
            {
                for(int k=0;k<4;k++)
                {
                    file>>arr1[j][k];
                }
            }
            file>>ans2;
            for(int l=0;l<4;l++)
            {
                for(int m=0;m<4;m++)
                {
                    file>>arr2[l][m];
                }
            }
            for(int n=0;n<4;n++)
            {
                check[n]=arr1[ans1-1][n];
                check2[n]=arr2[ans2-1][n];
            }
            validate(i,check,check2);
        }
        file.close();
    }
}

void validate(int tcase,int a[4],int b[4])
{
    int matches=0,card;
    fstream file2;
    file2.open("output.txt",ios::out|ios::app);
    if(!file2)
    {
        return;
    }
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(a[j]==b[i])
            {
                matches++;
                card=b[i];
            }
        }
    }
    if(matches==0)
    {
        file2<<"Case #"<<tcase<<": Volunteer cheated!"<<endl;
    }
    else if(matches==1)
    {
        file2<<"Case #"<<tcase<<": "<<card<<endl;
    }
    else
    {
        file2<<"Case #"<<tcase<<": Bad magician!"<<endl;
    }
    file2.close();
}
