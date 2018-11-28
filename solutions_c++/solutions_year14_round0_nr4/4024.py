#include <iostream>
#include <fstream>
#include <sstream>
#include <list>
#include <algorithm>

using namespace std;

list<double> split(const string &s, char delim)
{
    list<double> elems;
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim)) {
        elems.push_back(stod(item));
    }
    return elems;
}

int deceitful(list<double> n, list<double> k)
{
    int count = 0;

    k.sort();
    n.sort();

    while (!n.empty()) {
        auto nit = n.begin();
        auto kit = k.begin();
        for (; nit != n.end(); ++nit, ++kit) {
            if (*nit < *kit) {
                n.pop_front();
                k.pop_back();
                break;
            }
        }

        if (nit == n.end()) {
            return n.size();
        }
    }

    return count;
}

int optimal(list<double> n, list<double> k)
{
    int count = 0;
    k.sort();

    while (!n.empty()) {
        double choosen_naomi = n.front();

        bool scored = false;
        for (auto kit = k.begin(); kit != k.end(); ++kit) {
            if (*kit > choosen_naomi) {
                k.erase(kit);
                n.pop_front();
                scored = true;
                break;
            }
        }

        if (!scored) {
            n.pop_front();
            k.pop_front();
            count++;
        }
    }
    return count;
}

int main()
{
    ifstream input;
    input.open("input.txt");

    ofstream output;
    output.open("output.txt");

    string reader;
    getline(input, reader);

    const int T = stoi(reader);
    for (int i = 0; i < T; i++) {
        getline(input, reader); // N

        getline(input, reader);
        auto naomi = split(reader, ' ');

        getline(input, reader);
        auto ken = split(reader, ' ');

        output << "Case #" << i + 1 << ": " << deceitful(naomi, ken) << " " << optimal(naomi, ken) << "\n";
    }

    input.close();
    output.close();

    return 0;
}
