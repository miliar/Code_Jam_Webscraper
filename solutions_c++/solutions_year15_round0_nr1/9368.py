#include <fstream>
#include <string>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("standing.out");

int v[1001], k, T, S;
string shy;

int main()
{
    fin >> T;
    for (int i = 1; i <= T; i++){
        fin >> S;
        fin >> shy;
        for (int j = 0; j <= S; j++)
            v[j] = shy[j] - '0';
        int sum = 0, cnt = 0;
        for (int j = 0; j <= S; j++){
            if (!j)
                sum += v[0];
            else{
                if (sum < j){
                    cnt += j - sum;
                    sum += j - sum;
                }
                sum += v[j];
            }
        }
        fout << "Case #" << i << ": " << cnt << '\n';
    }
    return 0;
}
