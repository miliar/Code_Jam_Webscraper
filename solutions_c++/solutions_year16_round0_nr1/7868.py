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
    int N, temp, curr_N, curr_N_start, i, res;

    //begin
    infile.open("E:/yangliu/Documents/c++/google practice/test.txt", std::ios::in);
    outfile.open("E:/yangliu/Documents/c++/google practice/test_out.txt", std::ios::out);
    if(infile && outfile)
    {
        infile >> T;
        for(case_count = 1; case_count <= T; ++case_count)
        {
            infile >> N;
            std::vector<int> digits(10, -1);
            if(N == 0)
            {
                outfile << "Case #" << case_count << ": INSOMNIA" << std::endl;
            }
            else
            {
                i = 1;
                while(1)
                {
                    curr_N_start = i * N;
                    curr_N = curr_N_start;
                    while(curr_N >= 1)
                    {
                        temp = curr_N - (int)(curr_N / 10) * 10;
                        if(digits[temp] == -1)
                        {
                            digits[temp] = temp;
                        }
                        curr_N = (int)(curr_N / 10);
                        if(check(digits))
                        {
                            break;
                        }
                    }
                    if(check(digits))
                    {
                        res = curr_N_start;
                        outfile << "Case #" << case_count << ": " << res << std::endl;
                        break;
                    }
                    else
                    {
                        ++i;
                    }
                }
            }
        }
    }
    infile.close();
    outfile.close();
    return 0;
}

bool check(const std::vector<int>& digits)
{
    int i;
    bool res = true;
    for(i = 0; i < digits.size(); i++)
    {
        if(digits[i] != i)
        {
            res = false;
            break;
        }
    }
    return res;
}
