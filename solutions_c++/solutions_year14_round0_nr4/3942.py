#include <iostream>
#include <set>

using namespace std;

int playdirty(const set<float> &Naomi, const set<float> &Ken) {
    int done = 0;
    auto N_L = Naomi.begin();
    auto N_R = Naomi.end(); N_R--;
    auto K_L = Ken.begin();
    auto K_R = Ken.end(); K_R--;
    while (1) {
        cerr << "1";
        while (*N_R > *K_R) {
            cerr << "2";
            done++;
            if (N_L == N_R)
                return done;
            N_R--;
            K_R--;
        }
        while (*N_R < *K_R) {
            cerr << "3";
            if (N_L == N_R)
                return done;
            N_L++;
            K_R--;
        }
    }
    return done;
}

int playright(const set<float> &Naomi, const set<float> &Ken) {
    int done = 0;
    auto N_L = Naomi.begin();
    auto N_R = Naomi.end(); N_R--;
    auto K_L = Ken.begin();
    auto K_R = Ken.end(); K_R--;
    while (1) {
        cerr << "4";
        while (*N_R > *K_R) {
            cerr << "5";
            done++;
            if (N_L == N_R)
                return done;
            N_R--;
            K_L++;
        }
        while (*N_R < *K_R) {
            cerr << "6";
            if (N_L == N_R)
                return done;
            N_R--;
            K_R--;
        }
    }
    return done;
}

void work() {
    int cubes;
    set<float> Naomi;
    set<float> Ken;
    cin >> cubes;
    for (int i = 0; i < cubes; i++) {
        float size;
        cin >> size;
        Naomi.insert(size);
    }
    for (int i = 0; i < cubes; i++) {
        float size;
        cin >> size;
        Ken.insert(size);
    }
    cout << playdirty(Naomi, Ken) << " ";
    cout << playright(Naomi, Ken) << endl;
}

int main(void) {
    int cases;
    cin >> cases;
    for (int i = 1; i <= cases; i++) {
        cout << "Case #" << i << ": ";
        work();
    }
    return 0;
}