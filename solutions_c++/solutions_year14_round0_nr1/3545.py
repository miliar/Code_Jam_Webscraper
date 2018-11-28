#include <fstream>

using namespace std;

ifstream in("data.in");
ofstream out("data.out");

const int NMAX = 16;

bool Selected[NMAX+1];

int main()
{
    int i, j, answer, r, value, T;
    in >> T;

    for(int t = 1; t <= T; t++){
        answer = 0;
        for(i = 1; i <= NMAX; i++)
            Selected[i] = 0;

        in >> r;

        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++){
                in >> value;
                if(i == r){
                    Selected[value] = 1;
                }
            }

        in >> r;

        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++){
                in >> value;
                if(i == r && Selected[value] == 1){
                     answer = answer * NMAX + value;
                }
            }

        if(answer == 0){
            out << "Case #" << t << ": Volunteer cheated!\n";
        }
        else if(answer > NMAX){
            out << "Case #" << t << ": Bad magician!\n";
        }
        else {
            out << "Case #" << t << ": " << answer << '\n';
        }
    }
    return 0;
}
