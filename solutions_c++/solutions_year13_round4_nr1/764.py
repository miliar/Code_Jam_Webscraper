#include <iostream>
#include <fstream>
#include <vector>
#include <deque>
#include <algorithm>

#define MOD 1000002013

using namespace std;

long long N,M;

struct Record {
    int pos;
    long long mult;
    Record(int s1, long long m1): pos(s1), mult(m1) {}
};

long long fair(int s, int e)
{
    long long A = (2 * N - e + s + 1);
    int B = e-s;
    if (B % 2 == 0)
       return A * (B/2);
    else
        return (A/2) * B;
}

bool comp(const Record& r1, const Record& r2)
{
    return r1.pos < r2.pos;
}

void addToCost(int s, int e, long long mult, long long& cost)
{
    long long thisCost = ((fair(s,e) % MOD) * mult) % MOD;
    cost += thisCost;
    cost %=MOD;
}
    
int main()
{
    ifstream infile("file.in");
    ofstream outfile("file.out");
    
    int T;
    infile >> T;
    for (int t=1; t<=T; t++) {

        infile >> N >> M;
        
        deque<Record> trip;
        vector<Record> entrys;
        vector<Record> exits;
        
        long long cost = 0;
        for (int i=0; i<M; i++) {
            int s,e;
            long long p;
            infile >> s >> e >> p;
            entrys.push_back(Record(s,p));
            exits.push_back(Record(e,p));
            addToCost(s,e,p,cost);
        }
       
        std::sort(entrys.begin(), entrys.end(), comp);
        std::sort(exits.begin(), exits.end(), comp);
        
        int exitInd = 0;
        int entryInd = 0;
        
        long long newCost = 0;
        while (exitInd < exits.size()) {
            int exitPos = exits[exitInd].pos;
            while (entryInd < entrys.size() && entrys[entryInd].pos <= exitPos) {
                 trip.push_front(Record(entrys[entryInd].pos, entrys[entryInd].mult));
                 entryInd++;
             }
             
             long long allow = exits[exitInd].mult;
             while (allow > 0) {
                 Record& a = trip.front();
                 long long off = std::min(allow, a.mult);
                 allow -= off;
                 a.mult -= off;
                 addToCost(a.pos, exitPos, off, newCost);
                 if (a.mult == 0)
                    trip.pop_front();
             }
             
             exitInd++;
         }
         
            
        long long ans = cost - newCost;
        if (ans < 0) ans += MOD;
        
        outfile << "Case #"<<t<<": "<<ans<<endl;
    }
}

