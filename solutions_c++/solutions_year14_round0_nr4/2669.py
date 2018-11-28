#include <cstdio>
#include <fstream>
#include <algorithm>
#include <iterator>
#include <list>
using namespace std;

int war(list<long double> a, list<long double> b) {
    int n = 0;
    bool found;
    for(const long double &d: a) {
        found = false;
        for (auto it=b.begin(); it!=b.end(); ++it) {
            if(*it > d) {
                b.erase(it);
                found = true;
                break;
            }
        }
        if(!found) {
            b.pop_front();
            n++;
        }

    }
    return n;
}

int dwar(list<long double> a, list<long double> b) {
    a.reverse();
    b.reverse();
    int n = 0;
    for(const long double &d: b) {
        if(d < a.front()) {
            a.pop_front();
            n++;
        }
        else {
            a.pop_back();
        }


    }
    return n;
}

int counter = 0;
ifstream inFile("C:/tmp/file.in");
ofstream outFile("C:/tmp/file.out");
void make() {

    int n;
    long double m;
    list<long double> l1, l2;

    inFile >> n;
    inFile.ignore();

    for(int i = 0; i < n; i++) {
        inFile >> m;
        l1.push_back(m);
    }
    inFile.ignore();

    for(int i = 0; i < n; i++) {
        inFile >> m;
        l2.push_back(m);
    }
    inFile.ignore();

    l1.sort();
    l2.sort();
    int res_war = war(l1,l2);
    int res_dwar = dwar(l1,l2);
    outFile  << "Case #" << ++counter << ": " << res_dwar << " " << res_war << endl;

}

int main() {

    int t; inFile >> t;
    inFile.ignore();
    while(t--) {
        make();
    }
    return 0;
}
