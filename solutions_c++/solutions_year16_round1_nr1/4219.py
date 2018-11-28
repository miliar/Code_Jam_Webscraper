#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>


int main()
{
    int T, case_count;
    std::fstream infile, outfile;

    //problem variables
    std::string S;
    std::string::iterator it;

    //begin
    infile.open("E:/yangliu/Documents/c++/google practice/test.txt", std::ios::in);
    outfile.open("E:/yangliu/Documents/c++/google practice/test_out.txt", std::ios::out);
    if(infile && outfile)
    {
        infile >> T;
        for(case_count = 1; case_count <= T; ++case_count)
        {
            infile >> S;
            std::string last_word;
            if(S.size() == 1)
            {
                last_word = S;
            }
            else
            {
                last_word.push_back(S[0]);
                for(it = S.begin() + 1; it != S.end(); ++it)
                {
                    if(*it >= last_word[0])
                    {
                        last_word = *it + last_word;
                        //last_word.insert(0, *it);
                    }
                    else if(*it < last_word[0])
                    {
                        last_word.push_back(*it);
                    }
                }
            }
            outfile << "Case #" << case_count << ": " << last_word << std::endl;
        }
    }
    infile.close();
    outfile.close();
    return 0;
}
