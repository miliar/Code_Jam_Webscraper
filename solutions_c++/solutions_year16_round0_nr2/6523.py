#include<iostream>
#include<string>
#include<fstream>
#include<cstdlib>
#include<vector>

using namespace std;

int main()
{
    ifstream infile("B-large.in",ios::in);
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
        int flip = 0;
        string seq;
        infile >> seq;

        for(int j = 0; j < seq.length(); j++)
        {
            if(j == 0)
            {
                if(seq[j] == '-')
                {
                    flip++;
                }
            }

            else
            {
                if((seq[j-1] == '+') && (seq[j] == '-'))
                {
                    flip+=2;
                }
            }


        }


        outfile<<"Case #"<<i+1<<": "<< flip <<endl;
    }


    return 0;
}
