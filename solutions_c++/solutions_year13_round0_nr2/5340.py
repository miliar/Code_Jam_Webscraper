#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int T,M,N,i=0,arr[10][10],flag1,flag2;
    ifstream infile("B-small-attempt0.in");
    ofstream outfile("output.txt");
    infile>>T;
    for(i=0;i<T;)
    {
        infile>>N>>M;
        for(int j=0;j<N;j++)
        {
            for(int k=0;k<M;k++)
            {
                infile>>arr[j][k];
            }
        }

        for(int j=0;j<N;j++)
        {
            for(int k=0;k<M;k++)
            {
                if(arr[j][k]==1)
                {
                    flag1=1;
                    flag2=1;
                    for(int r=0;r<M;r++)
                    {
                        if(arr[j][r]==2)
                        {

                            flag1=0;
                            break;

                        }
                    }
                    for(int s=0;s<N;s++)
                    {
                        if(arr[s][k]==2)
                        {
                             flag2=0;
                             break;
                        }
                    }
                    if(flag1==0&&flag2==0)
                    {
                        outfile<<"Case #"<<i+1<<": NO";
                        outfile<<endl;
                        goto label;

                    }
                }
            }
        }
        outfile<<"Case #"<<i+1<<": YES";
        outfile<<endl;
        label:i++;
    }

}
