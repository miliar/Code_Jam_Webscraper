#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int firstMethod(const vector<int> &mus) {
    int ret = 0;
    for (int idx = 0; idx < mus.size() - 1; ++idx) {
        if (mus[idx + 1] < mus[idx]) {
            ret += mus[idx] - mus[idx + 1];
        }
    }
    return ret;
}

int secondMethod(const vector<int> &mus) {
    int rate = 0;
    for (int idx = 0; idx < mus.size() - 1; ++idx) {
        rate = max(rate, mus[idx] - mus[idx + 1]);
    }
    int ret = 0;
    for (int idx = 0; idx < mus.size() - 1; ++idx) {
        ret += min(mus[idx], rate);
    }
    return ret;
}

int main(int argc, const char **argv) {
    ios::sync_with_stdio(false);
    string file_path = "/Users/lxy/Downloads/";
    string file_name(argv[1]);
    file_path += file_name;
    fstream file;
    file.open(file_path.c_str());
    int T;
    file>>T;
    int num = 1;
    while (num <= T) {
        int N;
        file>>N;
        vector<int> mus(N, 0);
        for (int idx = 0; idx < N; ++idx) {
            file>>mus[idx];
        }
        
        int ret1 = firstMethod(mus), ret2 = secondMethod(mus);
        cout<<"Case #"<<num++<<": "<<ret1<<" "<<ret2<<endl;
    }
    file.close();
    return 0;
}
