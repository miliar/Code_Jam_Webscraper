#include <iostream>
#include <vector>
using namespace std;


vector<double> inputNaomi;
vector<double> inputKen;
vector<double> kens;
vector<double> naomis;

double kenschoice(double naomi)
{
    if (kens.size() == 0) return 0;
    vector<double>::iterator ret = kens.end();
    vector<double>::iterator iter = kens.begin();

    for ( ; iter!=kens.end(); ++iter) {
        if (*iter > naomi) {
            if (ret == kens.end() || *iter < *ret) {
                ret = iter;
            }
        }
    }
    if (ret != kens.end()) {
        // can win
        //cout << "win" << endl;
        double retv = *ret;
        kens.erase(ret);
        return retv;
    }
    // lose
    for (iter=kens.begin(); iter!=kens.end(); ++iter) {
        if (ret == kens.end() || *iter < *ret) {
            ret = iter;
        }
    }
    //cout << "lose" << endl;
    double retv = *ret;
    kens.erase(ret);
    return retv;
}

int war()
{
    kens = inputKen;
    int score = 0;
    for (int i=0; i<inputNaomi.size(); ++i) {
        double naomi = inputNaomi[i];
        if (kenschoice(naomi) < naomi) {
            score++;
        }
    }
    return score;
}

vector<double>::iterator minV(vector<double> &v)
{
    if (v.size() == 0) return v.end();
    vector<double>::iterator ret = v.end();
    vector<double>::iterator iter = v.begin();

    for ( ; iter!=v.end(); ++iter) {
        if (ret == v.end() || *iter < *ret) {
            ret = iter;
        }
    }
    return ret;
}

vector<double>::iterator maxV(vector<double> &v)
{
    if (v.size() == 0) return v.end();
    vector<double>::iterator ret = v.end();
    vector<double>::iterator iter = v.begin();

    for ( ; iter!=v.end(); ++iter) {
        if (ret == v.end() || *iter > *ret) {
            ret = iter;
        }
    }
    return ret;
}

int dwar()
{
    int score = 0;
    kens = inputKen;
    naomis = inputNaomi;
    while (kens.size() > 0) {
        if (*minV(naomis) > *minV(kens)) {
            score++;
            naomis.erase(minV(naomis));
            kens.erase(minV(kens));
        } else {
            //cheat();
            naomis.erase(minV(naomis));
            kens.erase(maxV(kens));
        }
    }
    return score;
}

int main()
{
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t) {
        int n;
        cin >> n;
        inputKen.clear();
        inputNaomi.clear();
        for (int i=0; i<n; ++i) {
            double w;
            cin >> w;
            inputNaomi.push_back(w);
        }
        for (int i=0; i<n; ++i) {
            double w;
            cin >> w;
            inputKen.push_back(w);
        }
        cout << "Case #" << t << ": " << dwar() << " " << war() << endl;
    }
    return 0;
}
