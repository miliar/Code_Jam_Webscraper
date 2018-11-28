#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

long long mod = 1000002013;

int T;
long long N,M;

/*
class Trip {
public:
    long long start;
    long long end;
    long long p;
    Trip(long long s,long long e,long long p) {
        start = s;
        end = e;
        this.p = p;
    }
};

class StartCmp {
    bool operator() (const Trip& t1,const Trip& t2) const {
        if(t1.start < t2.start) return true;
        else if(t1.start == t2.start) {
            if(t1.end >= t2.end) return true;
            else return false;
        } else {
            return false;
        }
    }
};

class EndCmp {
    bool operator() (const Trip& t1,const Trip& t2) const {
        if(t1.end < t2.end) return false;
        else return true;
    }    
};*/

class Time {
public:
    long long time;
    int flag; // 0 start 1 end
    long long p;
    Time(long long t,long long p,int f) {
        Time::time = t;
        Time::p = p;
        Time::flag = f;
    }
    bool operator<(const Time& other) const {
        return (time < other.time) || ((time == other.time)&&(flag < other.flag));
    }
};

long long total(long long i) {
    long long p1 = 2 * N + 1 - i;
    long long p2 = i;
    if(p1 % 2 == 0) p1 /= 2;
    else p2 /= 2;
    return ((p1 % mod) * (p2 % mod)) % mod;
}


int main(int argc, char* argv[]) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    
    fin >> T;
    vector<Time> tlist;
    for(int tc = 1; tc <= T; tc++) {
        fin >> N >> M;
        
        tlist.clear();

        long long s,e,p;
        long long sum = 0;
        for(int i = 0; i < M; i++) {
            fin >> s >> e >> p;
            tlist.push_back(Time(s,p,0));
            tlist.push_back(Time(e,p,1));
            sum = (sum + (total(e - s) * (p % mod)) % mod) % mod;
        }
        
        //cout << "SUM " << sum << endl;
        //cout << "SORT" << endl;
        sort(tlist.begin(),tlist.end());
        //cout << "LEN" << tlist.size() << endl;
        int ep = 0;
        long long real = 0;
        while(ep < tlist.size()) {
            //cout << tlist[ep].time << " " << tlist[ep].flag << endl;
            if(tlist[ep].flag == 1) {
                int sp = ep - 1;
                while(tlist[ep].p > 0 && sp >= 0) {
                    if(tlist[sp].flag == 0 && tlist[sp].p > 0) {
                        long long pn = min(tlist[sp].p,tlist[ep].p);
                        tlist[sp].p -= pn;
                        tlist[ep].p -= pn;
                        pn %= mod;
                        real = (real + (total(tlist[ep].time - tlist[sp].time) * pn) % mod) % mod;
                    } else {
                        sp--;
                    }
                }
            }
            ep++;
        }
        long long ans = (sum - real) % mod;
        if(ans < 0) ans = (ans + mod) % mod;
        
        fout << "Case #" << tc << ": " << ans << endl;
        //cout << "Case #" << tc << ": " << ans << endl;
    }
    
    
    return 0;
}
