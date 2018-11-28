#include <iostream>
#include <fstream>

int main(int argc, char* argv[])
{
    if (argc != 2)
        return 1;

    std::ifstream input;
    std::ofstream output;

    input.open(argv[1]);

    output.open("test.out");

    if (!input.is_open() || !output.is_open())
        return 1;

    unsigned nb_test = 0;
    input >> nb_test;

    for (unsigned i = 0; i < nb_test; ++i)
    {
        unsigned max_shyness = 0;
        input >> max_shyness;

        unsigned count_friend = 0;

        std::string audience;
        input >> audience;

        unsigned count_person = 0;

        for (unsigned j = 0; j <= max_shyness; ++j)
        {
            unsigned tmp = audience[j] - '0';

            if (j > count_person && tmp != 0)
            {
                count_friend += (j - count_person);
                count_person += (j - count_person);
            }

            count_person += tmp;
        }

        output << "Case #" << i + 1 << ": " << count_friend << std::endl;
    }

    input.close();
    output.close();

    return 0;
}
