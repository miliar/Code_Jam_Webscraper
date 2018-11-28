#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("A-large.in");
    ofstream out("gcj.a.txt");

    int t;
    in >> t;

    int smax;
    string input;
    for (int i = 0; i < t; i++) {
        in >> smax >> input;

        int already_ovating = input[0] - '0';
        int friends = 0;
        for (int shyness = 1; shyness < input.size(); shyness++) {
            int current_ovation = input[shyness] - '0';

            if (already_ovating < shyness) {
                friends++;
                already_ovating++;
            }

            already_ovating += current_ovation;
        }

        out << "Case #" << i + 1 << ": " << friends << "\n";
    }
}

