#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int selectMinAbove(vector<double> k, double n)
{
    int pos = -1;
    double min = 1024;
    for(int i = 0; i < k.size(); i++) {
        if(k[i] < min && k[i] > n) {
            pos = i;
            min = k[i];
        }
    }
    if(min == 1024) return -1;
    return pos;
}

int warScore(vector<double> n, vector<double> k)
{
    int wins = 0;
    while(n.size()) {
        int pos = selectMinAbove(k, n[0]);
        if (pos == -1) {
            wins++;
            pos = 0;
        }
        n.erase(n.begin());
        k.erase(k.begin()+pos);
    }
        return wins;
}

int dwarScore(vector<double> n, vector<double> k)
{

    int wins = 0;
    while (n.size()) {
        if( n[n.size() - 1] > k[k.size() - 1]) {
            n.pop_back();
            k.pop_back();
            wins++;
        } else {
            if( n[0] > k[k.size() - 1] ) wins++;
            n.erase(n.begin());
            k.pop_back();
        }
    }
    return wins;
}

int main()
{
    int cases;
    cin >> cases;

    for(int ii = 1; ii <= cases; ii++) {
        int blocks;
        vector<double> n;
        vector<double> k;
        cin >> blocks;
        for(int i = 0; i < blocks; i++) {
            double d;
            cin >> d;
            n.push_back(d);
        }
        for(int i = 0; i < blocks; i++) {
            double d;
            cin >> d;
            k.push_back(d);
        }
        std::sort(n.begin(), n.end());
        std::sort(k.begin(), k.end());

        cout << "Case #" << ii << ": " << dwarScore(n, k) << " " << warScore(n, k) << endl;
    }

}
