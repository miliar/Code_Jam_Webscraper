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
        int c0 = 0;
        int c1 = 0;
        int c2 = 0;
        int c3 = 0;
        int c4 = 0;
        int c5 = 0;
        int c6 = 0;
        int c7 = 0;
        int c8 = 0;
        int c9 = 0;

        string num;
        infile >> num;
        for(int j = 0; j < num.length();j++)
        {
            if(num[j] == 'Z')
            {
                c0++;
            }
            if(num[j] == 'W')
            {
                c2++;
            }
            if(num[j] == 'U')
            {
                c4++;
            }
            if(num[j] == 'X')
            {
                c6++;
            }
            if(num[j] == 'G')
            {
                c8++;
            }
        }
        for(int j = 0; j < num.length();j++)
        {
            if(num[j] == 'O')
            {
                c1++;
            }
            if(num[j] == 'H')
            {
                c3++;
            }
            if(num[j] == 'F')
            {
                c5++;
            }
            if(num[j] == 'S')
            {
                c7++;
            }
            if(num[j] == 'N')
            {
                c9++;
            }

        }
        c1 = c1-c0-c2-c4;
        c3 = c3-c8;
        c5 = c5-c4;
        c7 = c7 - c6;
        c9 = (c9 - c1 - c7)/2;

        vector<int> c;
        c.push_back(c0);
        c.push_back(c1);
        c.push_back(c2);
        c.push_back(c3);
        c.push_back(c4);
        c.push_back(c5);
        c.push_back(c6);
        c.push_back(c7);
        c.push_back(c8);
        c.push_back(c9);

        outfile<<"Case #"<<i+1<<": ";

        for(int j = 0; j < 10; j++)
        {
            int countnum = c[j];
            for(int k = 0; k < countnum; k++)
            {
                outfile << j;
            }
        }

        outfile << endl;

    }


    return 0;
}
