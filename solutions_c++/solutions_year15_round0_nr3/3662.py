#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;
struct Current {
    char letter;
    int sign; // 0 = pos, 1 = neg
};
static Current currentl;

void process(char nextl)
{
    switch (currentl.letter) {
    case '1':
        currentl.letter = nextl;
        break;
    case 'i':
        if (nextl == 'i') {
            currentl.letter = '1';
            currentl.sign = 1 - currentl.sign;
        }
        else if (nextl == 'j')
            currentl.letter = 'k';
        else {
            currentl.letter = 'j';
            currentl.sign = 1 - currentl.sign;
        }
        break;
    case 'j':
        if (nextl == 'i') {
            currentl.letter = 'k';
            currentl.sign = 1 - currentl.sign;
        }
        else if (nextl == 'j') {
            currentl.letter = '1';
            currentl.sign = 1 - currentl.sign;
        }
        else
            currentl.letter = 'i';
        break;
    case 'k':
        if (nextl == 'i')
            currentl.letter = 'j';
        else if (nextl == 'j') {
            currentl.letter = 'i';
            currentl.sign = 1 - currentl.sign;
        }
        else {
            currentl.letter = '1';
            currentl.sign = 1 - currentl.sign;
        }
        break;
    }
}

int main(int argc, char* argv[])
{
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    int num_cases;
    fin >> num_cases;
    for (int tc = 1; tc <= num_cases; tc++) {
        bool ans = false;
        int chars;
        int times;
        string bblock;
        string word;
        fin >> chars >> times >> bblock;
        if (chars == 1 || (chars * times <= 2))
            ans = false;
        else {
            vector<int> is;
            for (int i = 1; i <= times; i++)
                word.append(bblock);
            currentl.letter = word.at(0);
            currentl.sign = 0;
            if (currentl.letter == 'i' && currentl.sign == 0)
                is.push_back(0);
            for (unsigned int i = 1; i < word.size() - 2; i++) {
                process(word.at(i));
                if (currentl.letter == 'i' && currentl.sign == 0)
                    is.push_back(i);
            }
            if (is.empty())
                ans = false;
            else {
                for (unsigned int i = 0; i < is.size(); i++) {
                    vector<int> js;
                    currentl.letter = word.at(is[i] + 1);
                    currentl.sign = 0;
                    if (currentl.letter == 'j' && currentl.sign == 0)
                        js.push_back(is[i] + 1);
                    for (unsigned int j = is[i] + 2; j < word.size() - 1; j++) {
                        process(word.at(j));
                        if (currentl.letter == 'j' && currentl.sign == 0)
                        js.push_back(j);
                    }
                    if (!js.empty()) {
                        for (unsigned int j = 0; j < js.size(); j++) {
                            string last = word.substr(js[j] + 1);
                            currentl.letter = last.at(0);
                            currentl.sign = 0;
                            for (unsigned int k = 1; k < last.size(); k++) {
                                process(last.at(k));
                            }
                            if (currentl.letter == 'k' && currentl.sign == 0) {
                                ans = true;
                                break;
                            }
                        }
                    }
                    if (ans == true)
                        break;
                }
            }
        }
        fout << "Case #" << tc + 75 << ": " << (ans ? "YES\n" : "NO\n");
    }
    fin.close();
    fout.close();
    return 0;
}
