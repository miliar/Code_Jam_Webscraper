#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int T;
int N;

int add(long long A,long long mote,long long& rtA) {
    int cnt = 0;
    rtA = A;
    if(rtA <=1) return -1;
    while(rtA <= mote) {
        rtA += (rtA - 1);
        cnt++;
    }
    
    return cnt;
}
/*
int sorbcnt(long long& tmpA,vector<long long>& mote,int cur) {
    int cnt = 0;
    while(cur < mote.size()) {
        if(tmpA > mote[cur]) {
            tmpA += mote[cur];
            cnt++;
            cur++;
            //cout << "TMPA " << tmpA << endl;
        } else 
            return cnt;
    }
    return cnt;
}*/

int solve(vector<long long>& mote,int cur,long long cA) {
    //cout << "cur " << cur << "cA " << cA << endl;
    if(cur >= mote.size()) return 0;
    while(cur < mote.size()) {
        if(cA > mote[cur]) {
            cA += mote[cur];
            cur++;
        } else 
            break;
    }
    if(cur >= mote.size()) return 0;
    else {
        
        int ans2 = 1 + solve(mote,cur+1,cA);
        if(cA <= 1) return ans2;
        
        int ans1 = 0;
        while(cA <= mote[cur]) {
            cA += (cA - 1);
            ans1++;
        }
        ans1 += solve(mote,cur,cA);
        return (ans1 < ans2 ? ans1 : ans2);
    }
}

int main(int argc, char* argv[]) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    
    fin >> T;
    for(int tt = 1; tt <= T; tt++) {
        long long A;
        fin >> A >> N;
        vector<long long> ms;
        long long tmp;
        for(int i = 0; i < N; i++) {
            fin >> tmp;
            ms.push_back(tmp);
        }
        sort(ms.begin(),ms.end());
        /*
        cout << "A " << A << endl;
        for(int i = 0; i < ms.size(); i++)
            cout << ms[i] << " ";
        cout << endl;
        cout << "Case #" << tt << ": " << solve(ms,0,A) << endl;
        */
        fout << "Case #" << tt << ": " << solve(ms,0,A) << endl;
    }
    
    
    return 0;
}
