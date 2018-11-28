#include <fstream>
#include <algorithm>

using namespace std;

ifstream in("data.in");
ofstream out("data.out");

const int NMAX = 1001;

double Naomi[NMAX], Ken[NMAX];
int N;

int simulateDeceitfulWar(){
    int bN = N - 1, sN = 0, bK = N - 1;
    int k;

    for(k = 0; bK >= 0; bK--){
        if(Naomi[bN] > Ken[bK]){
            k ++;
            bN--;
        }
        else {
            sN++;
        }
    }

    return k;
}

int simulateWar(){
    int bN = N - 1,bK = N - 1,sK = 0;
    int k;

    for(k = 0; bN >= 0; bN--){
        if(Naomi[bN] > Ken[bK]){
            k ++;
            sK++;
        }
        else {
            bK--;
        }
    }

    return k;
}

int main()
{
    int T, i;
    in >> T;

    for(int t = 1; t <= T; t++){
        in >> N;

        for(i = 0; i < N; i++)
            in >>Naomi[i];

        sort(Naomi, Naomi + N);

        for(i = 0; i < N; i++)
            in >> Ken[i];

        sort(Ken, Ken + N);

        out << "Case #" << t <<": " << simulateDeceitfulWar() << " " << simulateWar() << '\n';
    }
    return 0;
}
