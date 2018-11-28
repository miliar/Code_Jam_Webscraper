#include<iostream>
#include<fstream>
int mtx[10][10];
int N,M;
using namespace std;
bool ch_col(int,int);
bool ch_rw(int,int);

bool ch_rw(int v,int r)
{
    bool f;
    for(int i=0;i<M;i++)
    {
        if(mtx[r][i]>v)
        {
          return false;
        }

    }
    return true;
}
bool ch_col(int v,int c)
{
    bool f;
    for(int i=0;i<N;i++)
    {
        if(mtx[i][c]>v)
        {
          return false;
        }

    }
    return true;
}
int main()
{
    int t;
    ifstream ifs;
    ifs.open("B-small-attempt2.in");
    ofstream ofs;
    ofs.open("output_1.txt");
    //int cs=0;
    int flag,inc;
    ifs>>t;
    int cs=0;
    while(cs<t)
    {
        cs++;
        ifs>>N;
        ifs>>M;
        for(int i=0;i<N;i++)
        {
                for(int j=0;j<M;j++)
                {
                   ifs>>mtx[i][j];
                   // cout<<mtx[i][j]<<" ";

                }
               // cout<<endl;

        }
        /////////////
        int p=mtx[0][0];
        bool f=true;
        for(int i=0;i<N&&f;i++)
        {
                p=mtx[i][0];

                for(int j=1;j<M;j++)
                if(p<mtx[i][j])
                p=mtx[i][j];

                for(int j=0;j<M;j++)
                {

                    if(p>mtx[i][j])
                    {
                        f=ch_col(mtx[i][j],j);
                        if(f==false)
                        {
                            break;
                        }
                    }
                }


        }
        if(f)
        ofs<<"Case #"<<cs<<": YES"<<endl;
        else
        ofs<<"Case #"<<cs<<": NO"<<endl;

    }

}
