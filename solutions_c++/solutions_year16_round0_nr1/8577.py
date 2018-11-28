#include<iostream>
#include<fstream>
using namespace std;

int check(int *a)
{
    int flag=1;
    for(int i=0;i<10;i++)
    {
        if(a[i]==0)
        {
            flag=0;
            break;
        }
    }
    return flag;
}

int main()
{
    std::ifstream infile("A-large.in");

    ofstream outfile;
    outfile.open("test.txt");

    int T;
    infile>>T;

    for(int i=0;i<T;i++)
    {
        int test[10]={0,0,0,0,0,0,0,0,0,0};
        long int num;
        int j;
        infile>>num;
        if(num==0)
            outfile<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
        else
        {
                for(j=0;!(check(test));j++)
                {
                            int temp=(j+1)*num;

                            while(temp>0)
                            {
                                test[temp%10]=1;
                                temp/=10;
                            }
                }
                outfile<<"Case #"<<(i+1)<<": "<<(j*num)<<endl;
        }
    }
return 0;
}
