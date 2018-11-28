#include <iostream>
#include <fstream>
#include <string>


int main()
{
    std::fstream f("data.txt", std::fstream::in);
    if ( (f.rdstate() & std::ifstream::failbit ) != 0 ) {
        std::cerr << "Error opening file.\n";
        return 1;
    }

    std::fstream out("out.txt", std::fstream::out);

    size_t test_count = 0;
    f >> test_count;

    for (size_t i = 0; i < test_count; i++) {
        unsigned long max_shyness = 0;
        std::string input_state;
        f >> max_shyness;
        f >> input_state;

        unsigned long people_stood_up = 0;
        unsigned long need_people = 0;
        for (size_t current_shyness = 0; current_shyness < (max_shyness + 1); current_shyness++) {
            long people_of_current_shyness = (input_state[current_shyness] - '0');
            if (people_of_current_shyness > 0 && current_shyness > people_stood_up) {
                long delta_people = (current_shyness - people_stood_up);
                people_stood_up += delta_people;
                need_people += delta_people;
            }
            people_stood_up += people_of_current_shyness;
        }
        std::cout << "Case #" << (i+1) << ": " << need_people << "\n";
        out << "Case #" << (i+1) << ": " << need_people << "\n";
    }

    f.close();
    out.close();

    return 0;
}
