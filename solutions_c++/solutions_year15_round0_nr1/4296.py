#include <fstream>
using namespace std;

int T;
int N;
string s;

int main()
{
    ifstream fin("file.in");
    ofstream fout("file.out");

    fin >> T;

    for(int j = 1; j <= T; j++){
        fin >> N >> s;

        int curr = 0;
        int Add = 0;
        for(int i = 0; i <= N; i++){
            int a = s[i] - '0';
            if(a != 0){
                if(curr < i){
                    Add += i - curr;
                    curr = i;
                }
                curr += a;
            }
        }

        fout << "Case #" << j << ": " << Add << "\n";

    }

}
