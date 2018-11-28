#include <iostream>

using namespace std;
string s0[5] = {"ZERO", "TWO", "FOUR", "SIX", "EIGHT"};
char c0[5] = {'Z', 'W', 'U', 'X', 'G'};
int v0[5] = {0, 2, 4, 6, 8};

string s1[4] = {"ONE", "THREE", "FIVE", "SEVEN"};
char c1[4] = {'O', 'R', 'F', 'S'};
int v1[4] = {1, 3, 5, 7};

int res[10];
int main()
{
    int t;
    string s;
    cin >> t;
    for(int v = 0; v < t; v++){
        cin >> s;
        int count = 0;
        for(int i = 0; i < 10; i++)
            res[i] = 0;
        for(int i = 0; i < 5; i++){
            char ck = c0[i];
            string sk = s0[i];
            int vk = v0[i];
            std::size_t found = s.find_first_of(ck);
            while(found!=std::string::npos){
                res[vk]++;
                for(int j = 0; j < sk.length(); j++){
                    s.at(s.find_first_of(sk.at(j))) = ',';
                    count++;
                }
                found = s.find_first_of(ck);
            }
        }

        for(int i = 0; i < 4; i++){
            char ck = c1[i];
            string sk = s1[i];
            int vk = v1[i];
            std::size_t found = s.find_first_of(ck);
            while(found!=std::string::npos){
                res[vk]++;
                for(int j = 0; j < sk.length(); j++){
                    s.at(s.find_first_of(sk.at(j))) = ',';
                    count++;
                }
                found = s.find_first_of(ck);
            }
        }
        cout << "Case #" << v + 1 << ": ";
        res[9] = (s.length() - count)/4;
        for(int i = 0; i < 10; i++)
            for(int j = 0; j < res[i]; j++)
                cout << i;
        cout << endl;
    }
    return 0;
}
