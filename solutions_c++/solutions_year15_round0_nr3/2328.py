#include <iostream>
#include <fstream>

using namespace std;

int table[4][4]={{1,2,3,4},{2,-1,4,-3}, {3,-4,-1,2},{4,3,-2,-1}};
char str[20000];

ifstream fin("input.txt");
ofstream fout("output.txt");

int multiply(int first,int second)
{
    int sign=1;

    if(first<0)
    {
        sign=-1;
        first=-first;
    }

    if(second<0)
    {
        sign=sign*-1;
        second=-second;
    }

    return table[first-1][second-1]*sign;
}

int map_value(char ch)
{
    if(ch=='i')
        return 2;
    else if(ch=='j')
        return 3;
    else if(ch=='k')
        return 4;
}

int update_looking(int l)
{
    if(l==2)
        return 3;
    else if(l==3)
        return 4;
    else if(l==4)
        return 2;
}

int main()
{
    int test;

    fin>>test;

    for(int m=1;m<=test;m++)
    {
        int l,x;

        fin>>l>>x;
        fin>>str;

        int flag=0,looking=2,val=1;

        for(int i=1;i<=x;i++)
        {
            for(int j=0;j<l;j++)
            {
                int z=map_value(str[j]);

                val=multiply(val,z);

                if(val==looking)
                {
                    flag=1;

                    if(looking==2 || looking==3)
                    {
                        looking=update_looking(looking);
                        val=1;
                    }
                }
                else
                    flag=0;
            }
        }

        if(flag==1)
            fout<<"Case #"<<m<<": YES"<<endl;
        else
            fout<<"Case #"<<m<<": NO"<<endl;

    }

    return 0;
}
