#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int nStrategy(vector<double> nVect, int nStart, int nEnd,
              vector<double> kVect, int kStart, int kEnd) {
    if(nStart > nEnd) {
        return 0;
    }
    for(int i=0; i<=nEnd-nStart; ++i) {
        if(nVect[nStart+i]<kVect[kStart+i]) {
            return nStrategy(nVect, nStart+1, nEnd,
                             kVect, kStart, kEnd-1);
        }
    }
    return nEnd-nStart+1;
}

int kStrategy(vector<double> nVect, vector<double> kVect) {
    int kScore = 0;
    int nIndex = 0;
    for(int i=0; i<kVect.size(); ++i) {
        if(kVect[i]>nVect[nIndex]) {
            ++kScore;
            ++nIndex;
        }
    }
    return nVect.size()-kScore;
}

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("d-large.out", "w", stdout);
    int cnt;
    cin>>cnt;
    for(int t=1; t<=cnt; t++) {
        int num;
        cin>>num;
        vector<double> nVect(num, 0.0);
        vector<double> kVect(num, 0.0);
        for(int i=0; i<num; ++i) {
            cin>>nVect[i];
        }
        for(int i=0; i<num; ++i) {
            cin>>kVect[i];
        }
        sort(nVect.begin(), nVect.end());
        sort(kVect.begin(), kVect.end());

        int nScore = nStrategy(nVect, 0, num-1, kVect, 0, num-1);
        int kScore = kStrategy(nVect, kVect);
        cout<<"Case #"<<t<<": "<<nScore<<" "<<kScore<<endl;
    }
}
