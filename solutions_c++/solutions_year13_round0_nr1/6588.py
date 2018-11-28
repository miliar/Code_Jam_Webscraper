#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::string;


char find_in_a_row(string s)
{
    char winner = 'N';

    for(size_t i = 0; i < 16; i += 4) {
        char first = s[i];
        bool flag = 1;

        if(first == 'T')
            first = s[i+1];

        for(size_t j = 1; j < 4; ++j) {
            char next = s[i+j];

            if(next != first && next != 'T') {
                flag = 0;
            }
        }
        if(flag && first != '.') {
            winner = first;
        }
    }

    return winner;
}

char find_in_a_column(string s)
{
    char winner = 'N';

    for(size_t i = 0; i < 4; ++i) {
        char first = s[i];
        bool flag = 1;

        if(first == 'T')
            first = s[i+4];

        for(size_t j = 4; j < 16; j += 4) {
            char next = s[i+j];

            if(next != first && next != 'T') {
                flag = 0;
                break;
            }
        }
        if(flag && first != '.') {
            winner = first;
            break;
        }
    }

    return winner;
}

char find_in_a_diagonals(string s)
{
    char winner = 'N';
    char first = s[0];
    size_t k = 0;

    if(first == 'T')
        first = s[5];
    for(size_t i = 5; i < 16; i += 5) {
        char next = s[i];

        if(next == first || next == 'T')
            ++k;
    }
    if(k == 3 && first != '.')
        winner = first;

    first = s[3];
    if(first == 'T')
        first = s[6];
    k = 0;
    for(size_t i = 6; i < 13; i += 3) {
        char next = s[i];

        if(next == first || next == 'T')
            ++k;
    }
    if(k == 3 && first != '.')
        winner = first;

    return winner;
}


int main()
{
    size_t n;

    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    cin >> n;

    for(size_t i = 0; i < n; ++i) {

        string s;
        bool end = 1;

        std::getline(cin, s);
        for(size_t j = 0; j < 4; ++j) {
            string row;

            std::getline(cin, row);
            if(end) {
                for(size_t k = 0; k < row.length(); ++k) {
                    if(row[k] == '.') {
                        end = 0;
                        break;
                    }
                }
            }
            s += row;
        }

        cout << "Case #" << i+1 << ": ";

        char winner = 'N';
        winner = find_in_a_row(s);
        if(winner != 'N') {
            cout << winner << " won" << std::endl;
            continue;
        }
        winner = find_in_a_column(s);
        if(winner != 'N') {
            cout << winner << " won" << std::endl;
            continue;
        }
        winner = find_in_a_diagonals(s);
        if(winner != 'N') {
            cout << winner << " won" << std::endl;
            continue;
        }

        if(end)
            cout << "Draw" << std::endl;
        else
            cout << "Game has not completed" << std::endl;
    }

    return 0;
}
