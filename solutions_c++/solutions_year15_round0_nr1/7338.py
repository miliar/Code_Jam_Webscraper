#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

int main(int argc, char const *argv[])
{
    string line;
    int T;
    cin >> T;
    cin.get();
    for(int test=0; test<T; test++){
        getline(cin, line);

        int s_max;
        string temp;
        vector<int> shy_level;
        stringstream ss(line);

        ss >> s_max >> temp;
        for(int i=0; i<temp.size(); i++){
            shy_level.push_back(temp[i] - '0');
        }

        int num_additional_friend = 0;
        int num_standing = shy_level[0];
        for(int i=1; i<shy_level.size(); i++){
            if(shy_level[i] != 0){
                if(num_standing < i){
                    num_additional_friend += (i - num_standing);

                    num_standing +=  (i - num_standing);
                }

                num_standing += shy_level[i];
            }
        }

        cout << "Case #" << test+1 << ": " << num_additional_friend << endl;
    }

    return 0;
}