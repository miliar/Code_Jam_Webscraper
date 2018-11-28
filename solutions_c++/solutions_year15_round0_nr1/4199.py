#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

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
        // Limit: shy_max <= 1000
        size_t shy_max;
        in >> shy_max;

        std::vector<size_t> count_per_shyness;
        std::string shyness_counts;
        in >> shyness_counts;
        assert(shyness_counts.size() == shy_max + 1);

        for (auto c : shyness_counts)
        {
            count_per_shyness.push_back(c - '0');
        }

        size_t missing = 0;
        size_t current_count = 0;

        for (size_t i = 0; i <= shy_max; ++i)
        {
            if (current_count < i)
            {
                missing += i - current_count;
                current_count = i;
            }
            current_count += count_per_shyness[i];
        }

        out << "Case #" << caseno << ": " << missing << '\n';
    }
    out.flush();
}
