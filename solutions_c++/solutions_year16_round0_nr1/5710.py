#include <iostream>
#include <set>
#include <string>
#include <fstream>

using namespace std;

void add_digits(std::string s, set<char> *digitos){
    for(unsigned int i = 0; i < s.length(); ++i){
        digitos->insert(s.at(i));
    }
}

void add_digits(int s, set<char> *digitos){
    add_digits(std::to_string(s), digitos);
}

int main()
{
    ifstream input_file;
    input_file.open("A-large.in", ifstream::in);
    ofstream output_file;
    output_file.open("A-large-output.txt", ofstream::out);
    string temp;
    getline(input_file, temp);

    int caso = 1;
    while(getline(input_file, temp)){
        if(temp.compare("0") == 0){
            output_file << "Case #" << caso << ": " << "INSOMNIA" << endl;
            ++caso;
            continue;
        }

        set<char> digitos;
        add_digits(temp, &digitos);

        int i = 2;
        long n_orig = std::stoi(temp, nullptr, 10);
        long n;
        while(digitos.size() < 10){
            n = i * n_orig;
            ++i;
            add_digits(n, &digitos);
        }
        output_file << "Case #" << caso << ": " << n << endl;
        ++caso;
    }

    input_file.close();
    output_file.close();
    return 0;
}
