#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

std::vector<int> split(const std::string &s, char delim)
{
    std::vector<int> elems;
    std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        elems.push_back(atoi(item.c_str()));
    }
    return elems;
}

int main()
{
    ifstream input;
    input.open("input.txt");

    ofstream output;
    output.open("output.txt");

    string reader;
    getline(input, reader);

    const int T = atoi(reader.c_str());
    for (int i = 0; i < T; i++) {
        vector <int> vec[2];

        for (int r = 0; r < 2; r++) {
            getline(input, reader);
            int answer = atoi(reader.c_str());

            string lines[4];
            for (int j = 0; j < 4; j++) {
                getline(input, lines[j]);
            }

            vec[r] = split(lines[answer - 1], ' ');
            sort(vec[r].begin(), vec[r].end());
        }

        vector<int> intersection;
        set_intersection(vec[0].begin(), vec[0].end(),
                         vec[1].begin(), vec[1].end(),
                         back_inserter(intersection));

        output << "Case #" << i + 1 << ": ";
        switch (intersection.size()) {
            case 0:
                output << "Volunteer cheated!\n";
                break;

            case 1:
                output << intersection.front() << "\n";
                break;

            default:
                output << "Bad magician!\n";
                break;
        }
    }

    input.close();
    output.close();

    return 0;
}

