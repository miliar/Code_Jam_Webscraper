#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");



class senator{
    public:
    senator(int N, string Ch):
    number(N),
    letter(Ch){;}
    bool operator < (const senator& other){
        return number < other.number;
    }
    bool operator > (const senator& other){
        return number > other.number;
    }
    int number;
    string letter;
};

void print(const vector<senator>& vec){
    for (int i = 0; i < vec.size(); ++i){
        cout << vec[i].letter<<": "<<vec[i].number << endl;
    }
}

string solve(vector<senator>& data){
    sort(data.begin(), data.end(),
    [](senator a, senator b){return a > b;}
    );
    string res;
    while (data[0] > data[1]){
        res += data[0].letter + " ";
        --data[0].number;
    }
    senator a = data[0];
    senator b = data[1];
    for (int i = 2; i < data.size(); ++i){
        for (int j = 0; j < data[i].number; ++j){
            res += data[i].letter + " ";
        }
    }
    for (int i = 0; i < a.number; ++i){
        res += a.letter + b.letter + " ";
    }

    //i should get 2k 2n

    //print(data);
    //cout<<"--------------"<<endl;

    return res;

}

int main()
{
    int T;
    in >> T;
    for (int iT = 1; iT <= T; ++iT){
        int N, tmp;
        vector<senator> data;
        in >> N;
        for (int iN = 0; iN < N; ++iN){
            in >> tmp;
            string party;
            party += 'A' + iN;
            data.push_back(senator(tmp,party));
        }
        out << "Case #"<<iT<<": "<<solve(data) << endl;
    }
    return 0;
}
