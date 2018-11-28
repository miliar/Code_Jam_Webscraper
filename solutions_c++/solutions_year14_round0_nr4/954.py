#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
using namespace std;

void printArr(set<double>& A, set<double>& B){
    for (const double &i: A) {
        cout<<i<<", ";
    }
    cout<<endl;
    for (const double &i: B) {
        cout<<i<<", ";
    }
    cout<<endl;
}

int DecWar(set<double>& A, set<double>& B) {
    vector<double> a, b;
    for (auto it = A.begin(); it != A.end(); ++it) {
        a.push_back(*it);
    }
    for (auto it = B.begin(); it != B.end(); ++it) {
        b.push_back(*it);
    }
    int small = 0, Awin = 0, k;
    int i, j = 0;
    while ((i = a.size()-1) >= j) {
        if (a[i] > b[b.size() - 1]) {
            Awin++;
            a.pop_back();
            b.pop_back();
        } else {
            k = b.size() - 1;
            small = 0;
            while (a[i] < b[k--]) {
                small++;
            }
            a.erase(a.begin(), a.begin() + small);
            while (small-->0) {
                b.pop_back();
            }
        }
    }
    return Awin; // return A's optimal score in deceived war
}

int War(set<double> A, set<double> B) {
    
    int Bwin = 0, All = (int)A.size();
    set<double>::iterator bt;
//     printArr(A,B);
    for (set<double>::iterator at = A.begin(); at != A.end();) {
//        cout<<"AT: "<<*at<<endl;
//        printArr(A,B);
        bt = B.upper_bound(*at);
        if (bt == B.end()) {
            B.erase(B.begin());
        } else {
            B.erase(bt);
            Bwin++;
        }
        A.erase(at++);
    }
    return All - Bwin; // return A's optimal score
}

int main(int argc, const char * argv[])
{
    int T, N, count = 1, tmp;
    double block;
    set<double> a, b;
    cin>>T;

    while(T-- > 0){
        a.clear();
        b.clear();
        cin>>N;
        tmp = N;
        while(tmp-- > 0) {
            cin>>block;
            a.insert(block);
        }
        tmp = N;
        while(tmp-- > 0) {
            cin>>block;
            b.insert(block);
        }
        
        printf("Case #%d: %d %d\n", count++, DecWar(a, b), War(a, b));
    }
}