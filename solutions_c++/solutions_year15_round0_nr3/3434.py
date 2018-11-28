
#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

map<char, map<char, char> > table;

void initTable() {
    table['1']['1'] = '1';
    table['1']['i'] = 'i';
    table['1']['j'] = 'j';
    table['1']['k'] = 'k';

    table['i']['1'] = 'i';
    table['i']['i'] = '2';
    table['i']['j'] = 'k';
    table['i']['k'] = 'm';

    table['j']['1'] = 'j';
    table['j']['i'] = 'n';
    table['j']['j'] = '2';
    table['j']['k'] = 'i';

    table['k']['1'] = 'k';
    table['k']['i'] = 'j';
    table['k']['j'] = 'l';
    table['k']['k'] = '2';
    
    // negatives

    table['2']['1'] = '2';
    table['2']['i'] = 'l';
    table['2']['j'] = 'm';
    table['2']['k'] = 'n';

    table['l']['1'] = 'l';
    table['l']['i'] = '1';
    table['l']['j'] = 'n';
    table['l']['k'] = 'j';

    table['m']['1'] = 'm';
    table['m']['i'] = 'k';
    table['m']['j'] = '1';
    table['m']['k'] = 'l';

    table['n']['1'] = 'n';
    table['n']['i'] = 'm';
    table['n']['j'] = 'i';
    table['n']['k'] = '1';

    // negatives 2

    table['1']['2'] = '2';
    table['1']['l'] = 'l';
    table['1']['m'] = 'm';
    table['1']['n'] = 'n';

    table['i']['2'] = 'l';
    table['i']['l'] = '1';
    table['i']['m'] = 'n';
    table['i']['n'] = 'j';

    table['j']['2'] = 'm';
    table['j']['l'] = 'k';
    table['j']['m'] = '1';
    table['j']['n'] = 'l';

    table['k']['2'] = 'n';
    table['k']['l'] = 'm';
    table['k']['m'] = 'i';
    table['k']['n'] = '1';


}


char reduce(string word) {
    char c = '1';
    for (char i : word) {
        c = table[c][i];
    }
    return c;
}

bool dijkstra(string word) {
    if (word.size() < 3)
        return false;

    char ci = '1';
    char cj;
    for (int i = 0; i < word.size() - 2; i++) {
        ci = table[ci][word[i]];
        //if (reduce(word.substr(0, i)) == 'i') 
        if (ci == 'i')
        {
            cj = '1';
            for (int j = 1; j < word.size() - i; j++)
            {
                cj = table[cj][word[i + j]];
                //if (reduce(word.substr(i, j)) == 'j')
                if (cj == 'j')
                {
                    if (reduce(word.substr(i + j + 1, string::npos)) == 'k') {
                        // printf("i: %d, j: %d, 1:%s, 2:%s, 3:%s\n", i, j, 
                        //        word.substr(0, i).c_str(),
                        //        word.substr(i, j).c_str(),
                        //        word.substr(i + j, string::npos).c_str());
                               
                        return true;
                    }
                }
            }

        }
    }
    return false;
}

vector<int> getIs(string& word) {
    vector<int> result;
    char c = '1';
    for (int i = 0; i < word.size() ; i++) {
        c = table[c][word[i]];
        if (c == 'i') {
            result.push_back(i);
        }
    }
    return result;
}


vector<int> getKs(string& word) {
    vector<int> result;
    char c = '1';
    for (int i = word.size() - 1; i >= 0; i--) {
        c = table[word[i]][c];
        if (c == 'k') {
            result.push_back(i);
        }
    }
    return result;
}


bool dijkstra2(string &word) {

    vector<int> is = getIs(word);
    vector<int> ks = getKs(word);

    char c;
    int l;

    for (int i : is) {
        c = '1';
        l = i + 1;
        
        for (int ki = ks.size() - 1; ki >= 0; --ki) {
        //for (int k : ks) {
            //if (i + 1 < k) { 
                
                while (l < ks[ki]) {
                    c = table[c][word[l]];
                    l++;
                }
                if (c == 'j')
                {
                    return true;
                }
                //}
        }
    }
    return false;
}


int main(int argc, char** argv) {

    initTable();

    //printf("i * i = %c\n", reduce(string("ii")));

    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int L, X;
        cin >> L;
        cin >> X;

        string in;
        cin >> in;
        string word;
        for (int j = 0; j < X; j++) {
            word += in;
        }
       

        
        if (dijkstra2(word)) {
            printf("Case #%d: YES\n", i + 1);
        }
        else {
            printf("Case #%d: NO\n", i + 1);
        }

        
    }

}
