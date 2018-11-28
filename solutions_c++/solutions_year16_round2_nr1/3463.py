

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

std::map<char, int> letters;

bool getnumber(int i, vector<int>& number)
{
  if(i == 10){
    for(auto it = letters.begin(); it != letters.end(); ++it){
      if(it->second != 0)
        return false;
    }
    return true;
  }
  bool found = true;
  for(int l = 0; l < nums[i].size(); ++l){
    char c = nums[i][l];
    if(letters[c] == 0)
      found = false;
    letters[c] -= 1;
  }
  if(!found){
    for(int l = 0; l < nums[i].size(); ++l){
      char c = nums[i][l];
      letters[c] += 1;
    }
  } else{
    number.push_back(i);
    --i;
  }
  if(getnumber(i + 1, number))
    return true;

  if(found){
    ++i;
    for(int l = 0; l < nums[i].size(); ++l){
      char c = nums[i][l];
      letters[c] += 1;
    }
    number.pop_back();
  }
  return getnumber(i+1,number);

}

int main()
{
    
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
        vector<int> number;
        string str;
        cin >> str;
        for(auto it = letters.begin(); it != letters.end(); ++it){
            it->second = 0;
        }
        std::sort(str.begin(), str.end());
        for(int i = 0; i < str.size(); ++i)
            letters[str[i]] += 1;

        getnumber(0, number);
        /*
        for(int i = 0; i < 10; ++i){
            bool found = true;
            for(int l = 0; l < nums[i].size(); ++l){
                char c = nums[i][l];
                if(letters[c] == 0)
                    found = false;
                letters[c] -= 1;
            }
            if(!found){
                for(int l = 0; l < nums[i].size() ; ++l){
                    char c = nums[i][l];
                    letters[c] += 1;
                }
            } else{
                number.push_back(i);
                --i;
            }
        }
        */
        cout << "Case #" << i << ": ";
        for(int i = 0; i < number.size(); ++i){
            cout << number[i];
        }
        cout << endl;
    }

    return 0;
}

