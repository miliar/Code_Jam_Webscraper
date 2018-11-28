#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int minkorszam = 10000;

void szetoszt(vector<int> v, int korszam);
void csokkent(vector<int> v, int korszam);
bool kesz(vector<int> v);

void szetoszt(vector<int> v, int korszam) {
    if (korszam > minkorszam) return;
    int maxhely = 0;
    for (int i=1;i<v.size();++i) if (v[maxhely] < v[i]) maxhely = i;
    int volt = v[maxhely];
    if (volt <= 3) return;

    v[maxhely] /= 2;
    v.push_back(volt - v[maxhely]);

    csokkent(v, korszam+1);
    szetoszt(v, korszam+1);

    if (volt == 9) {
        v[maxhely] = 6;
        v[v.size()-1] = 3;

        csokkent(v, korszam+1);
        szetoszt(v, korszam+1);
    }
}

void csokkent(vector<int> v, int korszam) {
    if (korszam > minkorszam) return;
    for (int i=0;i<v.size();++i) if (v[i] > 0) --v[i];

    if (kesz(v)) {
        if (minkorszam > korszam)
            minkorszam = korszam;
    }
    else {
        csokkent(v, korszam+1);
    }
}

bool kesz(vector<int> v) {
    bool l = true;
    for (int i=0;i<v.size() && l;++i) l = v[i] == 0;
    return l;
}

int main()
{
    ifstream f("B-small-attempt2.in");
    ofstream g("outputpan3.txt");
    int T;
    f >> T;
    for (int i=0;i<T;++i) {
        minkorszam = 10000;
        int P;
        f >> P;
        vector<int> v;
        for (int j=0;j<P;++j) {
            int tmp;
            f >> tmp;
            v.push_back(tmp);
        }
        szetoszt(v, 1);
        csokkent(v, 1);
        g << "Case #" << i+1 << ": " << minkorszam << endl;
    }


    return 0;
}
