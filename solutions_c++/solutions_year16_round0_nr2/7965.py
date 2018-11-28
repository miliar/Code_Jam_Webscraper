#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

bool check(const std::vector<int>& digits);

int main()
{
    int T, case_count;
    std::fstream infile, outfile;

    //problem variables
    std::string cake;

    //begin
    infile.open("E:/yangliu/Documents/c++/google practice/test.txt", std::ios::in);
    outfile.open("E:/yangliu/Documents/c++/google practice/test_out.txt", std::ios::out);
    if(infile && outfile)
    {
        infile >> T;
        for(case_count = 1; case_count <= T; ++case_count)
        {
            infile >> cake;
            int i;
            std::string cake_reduce;
            for(i = 0; i < cake.size(); i++)
            {
                if(cake[i] == cake[i + 1])
                {
                    continue;
                }
                else if(cake[i] != cake[i + 1])
                {
                    cake_reduce.push_back(cake[i]);
                }
            }
            std::vector<int> res(cake_reduce.size());
            if(cake_reduce[0] == '+')
            {
                res[0] = 0;
            }
            else if(cake_reduce[0] == '-')
            {
                res[0] = 1;
            }
            for(i = 1; i < res.size(); i++)
            {
                if(cake_reduce[i] == '+')
                {
                    res[i] = res[i - 1];
                }
                else if(cake_reduce[i] == '-')
                {
                    res[i] = res[i - 1] + 2;
                }
            }
            outfile << "Case #" << case_count << ": " << res.back() << std::endl;
        }
    }
    infile.close();
    outfile.close();
    return 0;
}
