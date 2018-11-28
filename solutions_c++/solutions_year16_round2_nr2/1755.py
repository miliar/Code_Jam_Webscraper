

#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;  // since cin and cout are both in namespace std, this saves some text


string nums[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

template<class Iter, class T>
Iter binary_find(Iter begin, Iter end, T val)
{
    // Finds the lower bound in at most log(last - first) + 1 comparisons
    Iter i = std::lower_bound(begin, end, val);

    if(i != end && !(val < *i))
        return i; // found
    else
        return end; // not found
}


int main()
{
    std::map<char, int> letters;
    for(int i = 0; i < 10; ++i){
        for(int l = 0; l < nums[i].size(); ++l){
            if(letters.find(nums[i][l]) == letters.end())
                letters[nums[i][l]] = 0;
        }
    }

    int t;
    cin >> t;
    cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');//for removing trailing spaces to endof line
    for(int i = 1; i <= t; ++i) {
        vector<int> possib[2];
        possib[0].push_back(0);
        possib[1].push_back(0);
        vector<int> number;
        string scores[2];
        cin >> scores[0];
        cin >> scores[1];
        const int nums[2] = { 0 };
        for(int c = 0; c < scores[0].size(); ++c){
            for(int z = 0; z < 2; ++z){
                if(scores[z][c] == '?'){
                    char other = scores[1 - z][c] == '?' ? '0' : scores[1 - z][c];
                    auto lastsize = possib[z].size();
                    char les = (other == '0') ? '9' : other - 1;
                    char plus = (other == '9') ? '0' : other + 1;
                    for(int i = 0; i < lastsize; ++i){
                        int prev = possib[z][i];
                        possib[z][i] = prev * 10 + (other - '0');
                        possib[z].push_back(prev * 10 + (les - '0'));
                        possib[z].push_back(prev * 10 + (plus - '0'));
                        if(les!='9' && plus!='9')
                          possib[z].push_back(prev * 10 + 9);
                        if(les != '0' && plus != '0')
                          possib[z].push_back(prev * 10 + 0);
                    }
                } else{
                    for(int i = 0; i < possib[z].size(); ++i){
                        char v = scores[z][c];
                        possib[z][i] = possib[z][i] * 10 + (v - '0');
                    }
                }
            }
        }
        int num0 = possib[0][0], num1 = possib[1][0];
        int xold = abs(num0 - num1);
        for(int c = 0; c < possib[0].size(); ++c){
            for(int j = 0; j < possib[1].size(); ++j){
                int xnew = abs(possib[0][c] - possib[1][j]);
                if(xnew < xold || (xnew==xold && (possib[0][c]<num0 || (possib[0][c]==num0 && possib[1][j] < num1) ))){
                    num0 = possib[0][c];
                    num1 = possib[1][j];
                    xold = xnew;
                }
            }
        }

        cout << "Case #" << i << ": ";
        for(int c = scores[0].size()-1; c >= 0; --c)
            cout << (num0 / (int)pow(10,c)) % 10;
        cout << " ";
        for(int c = scores[1].size()-1; c >= 0; --c)
            cout << (num1 / (int)pow(10,c)) % 10;
        cout << endl;
    }

    return 0;
}

