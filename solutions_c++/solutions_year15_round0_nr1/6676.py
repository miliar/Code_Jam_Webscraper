#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    int num_cases;
    fin >> num_cases;
    for (int tc = 1; tc <= num_cases; tc++) {
        int people = 0;
        int need = 0;
        int smax;
        string maxes;
        fin >> smax >> maxes;
        for (int i = 0; i <= smax; i++) {
            int ppl = maxes.at(i) - '0';
            if (ppl != 0) {
                if (i <= people)
                    people += ppl;
                else {
                    need += (i - people);
                    people += (need + ppl);
                }
            }
        }
        fout << "Case #" << tc << ": " << need << '\n';
    }
    fin.close();
    fout.close();
    return 0;
}
