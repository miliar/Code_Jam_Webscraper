#include <iostream>
#include <sstream>
#include <deque>
#include <fstream>
#include <vector>
#include <set>

class Digit {
    private:
        char num;
        int positive;
    public:
        Digit(char num, bool positive) {
            if (num != '1' && num != 'i' && num != 'j' && num != 'k') {
                num = 1;
                positive = true;
            }
            this->num = num;
            this->positive = positive?1:-1;
        }
        Digit operator*(const Digit& that) {
            if (num == 'i' && that.num == 'j')
                return Digit('k', positive * that.positive > 0);
            if (num == 'j' && that.num == 'k')
                return Digit('i', positive * that.positive > 0);
            if (num == 'k' && that.num == 'i')
                return Digit('j', positive * that.positive > 0);
            if (num == 'j' && that.num == 'i')
                return Digit('k', -1 * positive * that.positive > 0);
            if (num == 'k' && that.num == 'j')
                return Digit('i', -1 * positive * that.positive > 0);
            if (num == 'i' && that.num == 'k')
                return Digit('j', -1 * positive * that.positive > 0);
            Digit digit('1', true);
            if (num == that.num && num != '1')
                digit = Digit('1', -1 * positive * that.positive > 0);
            else if (num == that.num)
                digit = Digit('1', positive * that.positive > 0);
            else if (num == '1')
                digit = Digit(that.num, positive * that.positive > 0);
            else if (that.num == '1')
                digit = Digit(num, positive * that.positive > 0);

            return digit;
        }
        bool operator==(const Digit& that) {
            return num == that.num && positive == that.positive;
        }
        Digit operator*=(const Digit& that) {
            if (num == 'i' && that.num == 'j') {
                num = 'k';
                positive = positive * that.positive;
                return *this;
            }
            if (num == 'j' && that.num == 'k') {
                num = 'i';
                positive = positive * that.positive;
                return *this;
            }
            if (num == 'k' && that.num == 'i') {
                num = 'j';
                positive = positive * that.positive;
                return *this;
            }
            if (num == 'j' && that.num == 'i') {
                num = 'k';
                positive = -1 * positive * that.positive;
                return *this;
            }
            if (num == 'k' && that.num == 'j') {
                num = 'i';
                positive = -1 * positive * that.positive;
                return *this;
            }
            if (num == 'i' && that.num == 'k') {
                num = 'j';
                positive =  -1 * positive * that.positive;
                return *this;
            }

            // check other cases
            if (num == that.num && num != '1') {
                num = '1';
                positive = -1 * positive * that.positive;
                return *this;
            }
            else if (num == that.num) {
                num = '1';
                positive = positive * that.positive;
                return *this;
            }
            else if (num == '1') {
                num = that.num;
                positive = positive * that.positive;
                return *this;
            }
            else if (that.num == '1') {
                positive = positive * that.positive;
                return *this;
            }

            return *this;
        }
};


bool find (const std::string& input, unsigned biter, unsigned eiter) {
    Digit product('1', true);
    Digit i('i', true);
    Digit j('j', true);
    Digit k('k', true);
    Digit m1('1', false);
    bool iFound = false;
    bool jFound = false;
    while (biter <= eiter) {
        product *= Digit(input[biter], true);
        if (product == i)
            iFound = true;
        else if (product == k && iFound)
            jFound = true;
        else if (product == m1 && jFound && biter == eiter)
            return true;
        ++biter;
    }

    return false;
}

class Vector {
    private:
        unsigned repetition;
        std::string root;
    public:
        bool split() {
            std::string full;
            for (int i = 0; i < repetition; ++i) {
                full += root;
            }

            // now find out if we found first i
            Digit i('i', true);
            Digit j('j', true);
            Digit k('k', true);
            /*std::deque<Digit> dq;
            dq.push_back(i);
            dq.push_back(j);
            dq.push_back(k);*/
            bool ijkFound = find(full, 0, full.size() - 1);
            return ijkFound;
        }

        Vector(std::string& root, unsigned repetition) {
            this->root = root;
            this->repetition = repetition;
        }

};

int main() {
    std::ifstream ifile("/Users/skarunakaran/cj/TC.txt");
    if (ifile.is_open()) {
        bool first = true;
        unsigned numTests = 0;
        std::string line;
        std::getline(ifile, line);
        if (! ifile.eof()) {
            numTests = std::stoi(line);
            for (int i = 0; i < numTests; ++i) {
                unsigned num, repeat;
                std::string root;
                if (! ifile.eof()) {
                    std::getline(ifile, line);
                    std::stringstream frst(line);
                    frst >> num >> repeat;
                    std::getline(ifile, line);
                    std::stringstream scnd(line);
                    scnd >> root;
                    Vector vec(root, repeat);
                    bool isFound = vec.split();
                    std::cout << "Case #" << (i + 1) << ": " << ((isFound)?"YES":"NO") << std::endl;
                }
            }
        }
    }
    return 0;
}
