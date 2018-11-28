#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>

enum Values : int
{
    V_1 = 1,
    V_i = 2,
    V_j = 3,
    V_k = 4,
};

// http://stackoverflow.com/a/4609795
template <typename T> int sgn(T val)
{
    return (T(0) < val) - (val < T(0));
}

const std::map<std::pair<int, int>, int> multiplication_table =
{
    { { V_1, V_1 }, V_1 }, { { V_1, V_i },  V_i }, { { V_1, V_j },  V_j }, { { V_1, V_k },  V_k },
    { { V_i, V_1 }, V_i }, { { V_i, V_i }, -V_1 }, { { V_i, V_j },  V_k }, { { V_i, V_k }, -V_j },
    { { V_j, V_1 }, V_j }, { { V_j, V_i }, -V_k }, { { V_j, V_j }, -V_1 }, { { V_j, V_k },  V_i },
    { { V_k, V_1 }, V_k }, { { V_k, V_i },  V_j }, { { V_k, V_j }, -V_i }, { { V_k, V_k }, -V_1 },
};

int multiply(int val1, int val2)
{
    return sgn(val1 * val2) * multiplication_table.at(std::make_pair(std::abs(val1), std::abs(val2)));
}



std::string solve(const std::string& input, size_t repetitions)
{
    std::vector<int> in;

    for (auto c : input)
    {
        int val;
        if ('1' == c)
        {
            val = V_1;
        }
        else if ('i' == c)
        {
            val = V_i;
        }
        else if ('j' == c)
        {
            val = V_j;
        }
        else if ('k' == c)
        {
            val = V_k;
        }
        in.push_back(val);
    }

    if (in.size() * repetitions < 3)
    {
        return "NO";
    }

    std::vector<int> cur_values{ V_1 };

    size_t end_idx_i = 1;
    size_t end_idx_j = 1;

    for (size_t idx = 0; idx < in.size() * repetitions; ++idx)
    {
        int val = in[idx % in.size()];

        for (auto& cur : cur_values)
        {
            cur = multiply(cur, val);
        }
        
        for (size_t i = end_idx_j; i-- > 0;)
        {
            if (i >= end_idx_i)
            {
                // j
                if (V_j == cur_values[i])
                {
                    cur_values.push_back(V_1);
                }
            }
            else
            {
                // i
                if (V_i == cur_values[i])
                {
                    cur_values.insert(cur_values.begin() + end_idx_j, V_1);
                    ++end_idx_j;
                }
            }
        }

        // Simplify
        // Sort
        // j
        std::sort(cur_values.begin() + end_idx_i, cur_values.begin() + end_idx_j);
        // k
        std::sort(cur_values.begin() + end_idx_j, cur_values.end());

        // Remove duplicates
        // k
        cur_values.erase(std::unique(cur_values.begin() + end_idx_j, cur_values.end()), cur_values.end());
        // j
        size_t len = cur_values.size();
        cur_values.erase(std::unique(cur_values.begin() + end_idx_i, cur_values.begin() + end_idx_j), cur_values.begin() + end_idx_j);
        end_idx_j -= len - cur_values.size();
    }

    for (size_t i = end_idx_j; i < cur_values.size(); ++i)
    {
        if (V_k == cur_values[i])
        {
            return "YES";
        }
    }

    /*int first_value = V_1;
    for (size_t idx_i = 0; idx_i < total.size() - 2; ++idx_i)
    {
        first_value = multiply(first_value, total[idx_i]);

        if (V_i != first_value)
        {
            continue;
        }

        int second_value = V_1;
        for (size_t idx_j = idx_i + 1; idx_j < total.size() - 1; ++idx_j)
        {
            second_value = multiply(second_value, total[idx_j]);

            if (V_j != second_value)
            {
                continue;
            }

            int third_value = V_1;
            for (size_t idx_k = idx_j + 1; idx_k < total.size(); ++idx_k)
            {
                third_value = multiply(third_value, total[idx_k]);
            }
            if (V_k == third_value)
            {
                return "YES";
            }
        }
    }*/

    return "NO";
}


int main(int argc, char** argv)
{
    if (2 > argc)
    {
        std::cerr << argv[0] << " inputfile [outputfile]" << std::endl;
        return 1;
    }
    std::string infile{argv[1]};
    std::string outfile{infile};
    if (2 < argc)
    {
        outfile = argv[2];
    }
    else
    {
        outfile += ".out";
    }

    std::ifstream in(infile);
    std::ofstream out(outfile);
    if (!in.good())
    {
        std::cerr << "Bad input file" << std::endl;
        return 2;
    }

    if (!out.good())
    {
        std::cerr << "Bad output file" << std::endl;
        return 3;
    }

    int cases;
    in >> cases;

    for (int caseno = 1; caseno <= cases; ++caseno)
    {
        size_t length, repetitions;
        std::string input;
        in >> length >> repetitions >> input;
        assert(length == input.size());
        
        out << "Case #" << caseno << ": " << solve(input, repetitions) << std::endl;
    }
    out.flush();
}
