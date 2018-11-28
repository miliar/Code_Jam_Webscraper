
#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <map>
using namespace std;
typedef long long ll;

#define MAX 10001

map<string, string> multiplication;
map<string, string> division;

string word;
string i_value;

int i_ind[MAX];
int k_ind[MAX];

string update_value (string last, int i, int dir) {
    string cur_i = last;
    if (last[0] == '-')
        cur_i = cur_i[1];
    
    if (cur_i == "1") cur_i = word[i];
    else if (dir == 1)
        cur_i = multiplication[cur_i + word[i]];
    else if (dir == -1)
        cur_i = multiplication[word[i] + cur_i];
    
    if (cur_i[0] == '-' &&  last[0] == '-')
        cur_i = cur_i[1];
    else if (last[0] == '-')
        cur_i = '-' + cur_i;
    
    return cur_i;
    
}

int main() {

    ofstream fout ("ans.txt");
    ifstream fin ("input.txt");
    
    multiplication["ii"] = "-1";
    multiplication["ij"] = "k";
    multiplication["ik"] = "-j";
    multiplication["ji"] = "-k";
    multiplication["jj"] = "-1";
    multiplication["jk"] = "i";
    multiplication["ki"] = "j";
    multiplication["kj"] = "-i";
    multiplication["kk"] = "-1";
    
    // i * j = k
    // i * j * k = -1
    
    int T;
    fin >> T;
       // TEST CASES
    for (int t = 0; t < T; t++) {
        fout << "Case #" << t+1 << ": ";
        
        int N, repeat;
        fin >> N >> repeat >> word;
        
        string w = word;
        for (int i = 0; i < repeat-1; i++)
            word += w;
        
        string check_against = "i";
        
        i_value = word[0];
        if (i_value == "i")
            check_against = "k";
        for (int i = 1; i < N*repeat; i++) {
            i_value = update_value(i_value, i, 1);
            if (i_value == check_against) {
                if (check_against == "i")
                    check_against = "k";
                else if (check_against == "k")
                    check_against = "-1";
                else if (i == N*repeat-1)
                    check_against = "YES";
            }
        }
        
        if (check_against == "YES")
            fout << "YES\n";
        else
            fout << "NO\n";
    }
    
    return 0;
}

