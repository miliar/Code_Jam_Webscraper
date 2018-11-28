#include <iostream>

using namespace std;

bool *pancackes;
int gN;

void print_pancakes() {
    for(int i=0; i<gN;  i++) {
        if(pancackes[i])
            cout << '+';
        else
            cout << '-';
    }
    cout << endl;
}

void count_flips(int N, int &counter) {
    if(N<0) return;
    //Skip last +++
    int last_negatives = 0, last_positives = 0;
    int k = N;
    while(k>=0 && pancackes[k] == false) {
        last_negatives++;
        k--;
    }

    while(k>=0 && pancackes[k] == true) {
        last_positives++;
        k--;
    }
    if (last_negatives + last_positives != N+1) {
        count_flips(k,counter);
    }
    //Actual Counting
    int positives = 0, negatives = 0;
    int i = 0;
    while(i<=N && pancackes[i]) {
        positives++;
        i++;
    }
    while(i<=N && !pancackes[i]) {
        negatives++;
        i++;
    }
    if (positives == N+1) {
        counter += 0;
        return;
    }
    if (negatives == N+1) {
        counter += 1;
        for(int j=0;j<=N; j++) {
            pancackes[j] = true;
        }
        //cout << "[" << N+1 << "]: ";
        //print_pancakes();
        return;
    }
    if( positives + negatives == N+1) {
        counter += 2;
        for(int j=0;j<=N; j++) {
            pancackes[j] = true;
        }
        //cout << "[" << N+1 << "]: ";
        //print_pancakes();
        return;
    }

}

int main(int argc, char const* argv[])
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string s;
        cin >> s;
        gN = s.length();
        pancackes = new bool[gN];
        for(int i=0; i<gN; i++) {
            switch (s[i]) {
                case '+':
                         pancackes[i] = true;
                         break;
                case '-':
                         pancackes[i] = false;
                         break;
                default:
                         cout << "Something Wrong!";
                         break;
            }
        }

        int counter = 0;
        count_flips(gN-1, counter);

        cout << "Case #" << t << ": " << counter << endl;


        delete[] pancackes;
        pancackes = NULL;
    }
    return 0;
}
