#include <iostream>
#include <fstream>

using namespace std;

ifstream f ("A-large.in");
ofstream g ("A-large.out");

int t, n, senators[30], tn, idx;

struct party {
    int senators;
    int letter;
};

party getMaxSenatorsInParty() {
    party maxi;
    maxi.letter = 0;
    maxi.senators = 0;

    for(int i =0; i<n; i++) {
        if (senators[i] > maxi.senators) {
            maxi.letter = i;
            maxi.senators = senators[i];
        }
    }

    senators[maxi.letter]--;
    tn -= 1;
    return maxi;
}

void print(party part) {
    g<<char(part.letter + 65);
}

void solve() { // now we can evacuate 2 senators once
    while(tn > 0) {
        party temp = getMaxSenatorsInParty();
        print(temp);
        temp = getMaxSenatorsInParty();
        print(temp);
        g<<" ";
    }
}

void presolve() {
    if (tn % 2 == 1) { //one senator needs to be evacuated
        party temp = getMaxSenatorsInParty();
        print(temp);
        g<<" ";

        solve();
    } else {
        solve();
    }
}

int main()
{
    f>>t;

    while(f>>n) {
        idx++;
        g<<"Case #"<<idx<<": ";

        tn = 0;
        for (int i=0; i<n; i++) {
            f>>senators[i];
            tn += senators[i];
        }
        presolve();
        g<<'\n';
    }

    f.close();
    g.close();
    return 0;
}
