#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream fi("in");
    ofstream fw("out");

    int T, n;
    fi >> T;
    for(int i=0; i<T ; ++i) {
        fw << "Case #" << (i+1) << ": ";
        fi >> n;
        if (n == 0) {
            fw << "INSOMNIA" << endl;
            continue;
        }

        bool nums[10] = {false};
        int found = 0;
        int nn = n;
        int m=2;
        while(1) {
            int tn = n;
            while(tn) {
                int c = tn % 10;
                if (nums[c] == false) {
                    found++;
                    nums[c] = true;
                }
                tn /= 10;
            }
            if(found == 10) break;
            n = nn*m;
            m+=1;
        }
        fw << n << endl;
        cout<< n << endl;
    }


    fw.close();
    fi.close();
    return 0;
}