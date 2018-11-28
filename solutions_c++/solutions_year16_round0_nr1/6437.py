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
        int num;
        infile >> num;

        int temp = num;
        int ans = 0;

        vector<int> digit;

        for(int j = 1; j <= 100; j++)
        {
            temp = j*num;
            while(temp > 0)
            {
                int flag = 0;
                int d;
                d = temp%10;
                temp/=10;
                for(int k = 0; k < digit.size(); k++)
                {
                    if(digit[k] == d)
                    {
                        flag =1;
                    }
                }
                if(flag == 0)
                {
                    digit.push_back(d);
                }
            }

            if(digit.size() == 10)
            {
                ans = j*num;
                break;
            }

        }
        if(ans != 0)
        {
            outfile<<"Case #"<<i+1<<": "<< ans <<endl;
        }
        else
        {
            outfile<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        }
    }


    return 0;
}
