#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>

using namespace std;

fstream file;
int l,b;
int mat[100][100],tmat[100][100];
void read (int mat[100][100])
{
    for(int i=0;i<l;i++)
        for(int j=0;j<b;j++)
            file>>mat[i][j];

            file.get();
}

int max_r (int row)
{
    int max=0;
    for(int i=0;i<b;i++)
    {
        if(max<=mat[row][i])
        max=mat[row][i];
    }
    return max;
}
int max_c (int col)
{
    int max=0;
    for(int i=0;i<l;i++)
    {
        if(max<mat[i][col])
        max=mat[i][col];
    }
    return max;
}

void check_ver()
{

    int max;
    if(tmat[0][0]>=mat[0][0])
    {
        max=max_r(0);
            for(int i=0;i<b;i++)
                if(max<=tmat[0][i])
                tmat[0][i]=max;

        max=max_c(0);
            for(int i=0;i<l;i++)
                if(max<=tmat[i][0])
                tmat[i][0]=max;

    }

    if(tmat[0][b-1]>=mat[0][b-1])
    {
        max=max_c(b-1);
            for(int i=0;i<l;i++)
                {
                    if(max<=tmat[i][b-1])
                    tmat[i][b-1]=max;
                }
    }



    if(tmat[l-1][0]>=mat[l-1][0])
    {
        max=max_r(l-1);
            for(int i=0;i<b;i++)
                {
                    if(max<=tmat[l-1][i])
                    tmat[l-1][i]=max;
                }

    }

}

void check_ed()
{
    int max;
    for(int z=1;z<b-1;z++)
    {
        if(tmat[0][z]>=mat[0][z])
        {
           max=max_c(z);
            for(int i=0;i<l;i++)
                {
                    if(max<=tmat[i][z])
                    tmat[i][z]=max;
                }
        }
    }

     for(int z=1;z<l-1;z++)
    {
        if(tmat[z][0]>=mat[z][0])
        {
           max=max_r(z);
            for(int i=0;i<b;i++)
                {
                    if(max<=tmat[z][i])
                    tmat[z][i]=max;
                }
        }
    }
}

bool check ()
{
    for(int i=0;i<l;i++)
    {
        for(int j=0;j<b;j++)
        {
            if(tmat[i][j]!=mat[i][j])return false;
        }
    }
    return true;
}

int main()
{
    ofstream answer;
    file.open("B-large.in");
    answer.open("answer.txt");

    int n=0,t1,t2;
    while(int temp=file.get())
    {
        if(temp==10)break;
        temp-=48;
        n=(n*10)+temp;
    }
    //cout<<n<<endl;

    for(int line=1;line<=n;line++)
    {
        file>>l;
        file>>b;
        //cout<<l<<" "<<b<<endl;

        read(mat);

        for(int i=0;i<l;i++)
        {
            int max=100;
            for(int j=0;j<b;j++)
            {
               tmat[i][j]=max;
            }
        }

        check_ver();
        check_ed();

        if(check())
        {
            //cout<<"Case #"<<line<<": YES"<<endl;
            answer<<"Case #"<<line<<": YES"<<endl;
        }
        else
        {
            //cout<<"Case #"<<line<<": NO"<<endl;
            answer<<"Case #"<<line<<": NO"<<endl;
        }
    }
}
