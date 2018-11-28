#include <iostream>
#include <fstream>
#include <vector>

class Game {
public:
    Game(int, std::vector<int>, int);
    ~Game();
    int cal();

private:
    std::vector<int> Motes;
    int mote;
};

Game::Game(int m, std::vector<int>M, int n) {
    Motes = M;
    Motes.resize(n);
    mote = m;
}

Game::~Game() {
}

int Game::cal(){
    if (mote == 1) {
        return Motes.size();
    }

    int count = 0;
    int i = 0;
    for (; i < Motes.size(); i++) {
        if (Motes[i] < mote) {
            mote += Motes[i];
        }else{
            int count2 = count;
            int tmp = mote;
            while (Motes[i] >= tmp) {
                count2++;
                tmp = 2 * tmp - 1;
            }
            if (count2 - count <= Motes.size() - i) {
                count = count2;
                mote = Motes[i] + tmp;
            }else
                return count + Motes.size() - i;
        }
    }

    return count;
}

int main()
{
    std::ifstream inf("A-large.in");
    std::ofstream of("result.out");
    int T;
    inf >> T;
    int S = T;

    while (T > 0) {
        of << "Case #" << S - T + 1 << ": ";
        int mRead, nRead;
        inf >> mRead >> nRead;
        std::vector<int> MRead(nRead);
        for (int i = 0; i < MRead.size(); i++) {
            inf >> MRead[i];
        }
        for (int i = 0; i < MRead.size() - 1; i++) {
            for(int j = MRead.size() - 1; j > i; j--) {
                if ( MRead[j] < MRead[j - 1]) {
                    int tmp = MRead[j - 1];
                    MRead[j - 1] = MRead[j];
                    MRead[j] = tmp;
                }
            }
        }

        std::vector<int> Count(nRead);
        for (int i = 0; i < nRead; i++) {
            Game g(mRead, MRead, i + 1);
            Count[i] = g.cal() + nRead - i - 1;
        }
        int min = Count[0];
        for (int i = 1; i < nRead; i++) {
            if (min > Count[i])
                min = Count[i];
        }
        of << min << std::endl;
        T--;
    }

    inf.close();
    of.close();

    return 0;
}
