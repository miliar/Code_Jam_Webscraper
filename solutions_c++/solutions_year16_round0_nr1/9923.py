#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main() {
    ifstream in("C:\\Users\\Cyril\\ClionProjects\\CodeJam\\file.in");
    ofstream out("C:\\Users\\Cyril\\ClionProjects\\CodeJam\\test1.out");

    int n;
    in >> n;

    for (int i = 0; i < n; ++i) {
        int k;
        in >> k;

        vector<bool> list(10, false);

        if (k == 0) out <<"Case #"<<i+1<<": "<< "INSOMNIA" << endl;
        else {
            bool c = true;
            int count = 0;
            while(c){
                count++;
                int current = count * k;
                while(current != 0){
                    list[current%10] = true;
                    current /= 10;
                }

                c = false;
                for (int j = 0; j < 10; ++j) {
                    if (!list[j])
                        c = true;
                }
            }
            out << "Case #"<<i+1<<": "<<count*k << endl;
        }

    }
}
