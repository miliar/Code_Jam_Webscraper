#include<iostream>
#include<string>
#include<fstream>
#include<cstdlib>
#include<vector>

using namespace std;

int main()
{
    ifstream infile("A-large.in",ios::in);
    ofstream outfile("out.txt",ios::out);
    if(!infile)
    {
        cerr<<"File Problem!!"<<endl;
        exit(1);
    }

    int N;

    infile >> N;

    for(int i = 0; i < N; i++)
    {
        string seq;
        infile >> seq;

        for(int j = 1; j < seq.length(); j++)
        {
            if(seq[j] >= seq[0])
            {
                char temp = seq[j];
                for(int k = j; k > 0; k--)
                {
                    seq[k] = seq[k-1];
                }
                seq[0] = temp;
            }
        }


        outfile<<"Case #"<<i+1<<": "<< seq <<endl;
    }


    return 0;
}
