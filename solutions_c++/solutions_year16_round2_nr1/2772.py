#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <algorithm>
#include <map>

void digits(std::string S);

int main()
{
    int T;
    std::string S;
    std::cin >> T;

    for(int t = 0; t < T; t ++)
    {
        std::cin >> S;
        std::cout << "Case #" << t + 1 << ": ";
        digits(S);
    }
        return 0;
}

void digits(std::string S)
{
    std::string letters [10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

    std::list<int> result;
    std::list<char> found;
    std::map<char, int> letter_dict;

    //std::cout << "S: " << S << std::endl;
    for(int i = 0; i < S.size(); i++)
    {
        letter_dict[S[i]] ++;
    }

    // Find special letters: Z (0), X(6), G(8)
    result.insert(result.begin(), letter_dict['Z'], 0);
    letter_dict['E'] -= letter_dict['Z'];
    letter_dict['R'] -= letter_dict['Z'];
    letter_dict['O'] -= letter_dict['Z'];
    letter_dict['Z'] -= letter_dict['Z'];

    result.insert(result.begin(), letter_dict['X'], 6);
    letter_dict['I'] -= letter_dict['X'];
    letter_dict['S'] -= letter_dict['X'];
    letter_dict['X'] -= letter_dict['X'];

    result.insert(result.begin(), letter_dict['G'], 8);
    letter_dict['E'] -= letter_dict['G'];
    letter_dict['I'] -= letter_dict['G'];
    letter_dict['H'] -= letter_dict['G'];
    letter_dict['T'] -= letter_dict['G'];
    letter_dict['G'] -= letter_dict['G'];

    result.insert(result.begin(), letter_dict['S'], 7);
    letter_dict['E'] -= 2 * letter_dict['S'];
    letter_dict['N'] -= letter_dict['S'];
    letter_dict['V'] -= letter_dict['S'];
    letter_dict['S'] -= letter_dict['S'];

    result.insert(result.begin(), letter_dict['V'], 5);
    letter_dict['F'] -= letter_dict['V'];
    letter_dict['I'] -= letter_dict['V'];
    letter_dict['E'] -= letter_dict['V'];
    letter_dict['V'] -= letter_dict['V'];

    result.insert(result.begin(), letter_dict['F'], 4);
    letter_dict['O'] -= letter_dict['F'];
    letter_dict['U'] -= letter_dict['F'];
    letter_dict['R'] -= letter_dict['F'];
    letter_dict['F'] -= letter_dict['F'];

    result.insert(result.begin(), letter_dict['W'], 2);
    letter_dict['T'] -= letter_dict['W'];
    letter_dict['O'] -= letter_dict['W'];
    letter_dict['W'] -= letter_dict['W'];

    result.insert(result.begin(), letter_dict['O'], 1);
    letter_dict['N'] -= letter_dict['O'];
    letter_dict['E'] -= letter_dict['O'];
    letter_dict['O'] -= letter_dict['O'];

    result.insert(result.begin(), letter_dict['R'], 3);
    letter_dict['T'] -= letter_dict['R'];
    letter_dict['H'] -= letter_dict['R'];
    letter_dict['E'] -= 2 * letter_dict['R'];
    letter_dict['R'] -= letter_dict['R'];

    result.insert(result.begin(), letter_dict['I'], 9);
    result.sort();

    for(std::list<int>::iterator iter = result.begin();
            iter != result.end(); iter ++)
    {
        std::cout << *iter;
    }
    std::cout << std::endl;
}
