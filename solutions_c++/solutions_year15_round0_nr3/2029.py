//
//  main.cpp
//  Dijkstra
//
//  Created by Bai, Shi on 4/11/15.
//  Copyright (c) 2015 Bai, Shi. All rights reserved.
//


#include <stdio.h>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

struct Quaternion
{
public:
    Quaternion()
        : sign(1)
        , letter('1')
    {}

    Quaternion(int _sign, char _letter)
        : sign(_sign)
        , letter(_letter)
    {}

    Quaternion(char _letter)
        : sign(1)
        , letter(_letter)
    {}

    int sign;
    char letter;
};

Quaternion multiply(Quaternion a, Quaternion b)
{
    Quaternion res;
    res.sign = a.sign * b.sign;
    if (a.letter == '1' || b.letter == '1')
    {
        res.letter = (a.letter == '1') ? b.letter : a.letter;
        return res;
    }
    if (a.letter == b.letter)
    {
        res.letter = '1';
        res.sign *= -1;
        return res;
    }
    
    if (a.letter > b.letter)
    {
        Quaternion res = multiply(b, a);
        res.sign *= -1;
        return res;
    }
    if (a.letter == 'i')
    {
        if (b.letter == 'j')
        {
            res.letter = 'k';
        }
        else
        {
            res.letter = 'j';
            res.sign *= -1;
        }
    }
    else
    {
        res.letter = 'i';
    }
    return res;
}

int main()
{
    int num_cases = 0;
    string in_file_name;
    string out_file_name;
    cout << "Please enter input file name:";
    cin >> in_file_name;
    cout << "Please enter ouput file name:";
    cin >> out_file_name;
    std::fstream infile(in_file_name.c_str(), ios::in);
    std::fstream outfile(out_file_name.c_str(), ios::out);
    std::string line;
    std::getline(infile, line);
    std::istringstream iss(line);
    iss >> num_cases;

    for (int case_id = 1; case_id <= num_cases; case_id++)
    {
        std::getline(infile, line);
        std::istringstream iss_LX(line);
        int L = 0, X = 0;
        iss_LX >> L;
        iss_LX >> X;

        cout << "Current test case L & X: " << line << endl;

        string str;
        std::getline(infile, line);
        cout << "Current test case string: " << line << endl;
        std::istringstream iss_str(line);
        iss_str >> str;


        Quaternion whole_str;
        Quaternion single_str;
        for (int t = 0; t < L; t++)
        {
            Quaternion curr_qua(str[t]);
            single_str = multiply(single_str, curr_qua);
        }
        for (int t = 0; t < X; t++)
        {
            whole_str = multiply(whole_str, single_str);
        }

        bool found_solution = false;
        Quaternion i_qua;
        int whole_len = L * X;
        for (int t_i = 0; t_i < whole_len; t_i++)
        {
            i_qua = multiply(i_qua, str[t_i % L]);
            if (i_qua.letter != 'i' || i_qua.sign != 1)
            {
                continue;
            }
            Quaternion removed_i = multiply(Quaternion(-1, 'i'), whole_str);
            Quaternion j_qua;
            for (int t_j = t_i + 1; t_j < whole_len; t_j++)
            {
                j_qua = multiply(j_qua, str[t_j % L]);
                if (j_qua.letter != 'j' || j_qua.sign != 1)
                {
                    continue;
                }
                Quaternion removed_j = multiply(Quaternion(-1, 'j'), removed_i);
                if (removed_j.letter == 'k' && removed_j.sign == 1)
                {
                    found_solution = true;
                    break;
                }
            }
            if (found_solution)
            {
                break;
            }
        }


        printf("Case #%d: %c%c\n", case_id, whole_str.sign == 1 ? ' ' : '-', whole_str.letter);
        printf("Case #%d: %s\n", case_id, found_solution ? "YES" : "NO");
        outfile << "Case #" << case_id << ": " << (found_solution ? "YES" : "NO") << endl;
    }
    outfile.close();
    return 0;
}
