#include <iostream>
#include <fstream>
#define MAXLEN 10000
using namespace std;
bool used[MAXLEN];
int filecount, capacity;
int files[MAXLEN];
struct disc {
    int first;
    int second;
    const int size() {
        return files[first] + files[second];
    }
    
    bool operator<(const disc& that) const {
        return (files[first] + files[second]) < (files[that.first] + files[that.second]);
    }
    
    disc(int first, int second) {
        this->first = first;
        this->second = second;
    }
    disc() {
        
    }
};
/*
int needed(int filesUsed, int remaining, int ondisc) {
    if(filesUsed == filecount)
        return 0;
    for(int i=0;i<filecount;i++) {
        if(used[i])
            continue;
        if(files[i] <= remaining) {
            used[i] = true;
            return needed(filesUsed + 1, remaining - used[i]);
        }
        else {
            used[i] = true;
            return needed(filesUsed + 1, capacity - used[i]) + 1;
        }
    }
    return -1;
 }*/
disc discs[MAXLEN * MAXLEN / 2];

int main() {
    ifstream in("in.txt");
    ofstream out("out.txt");
    int T;
    in>>T;
    
    for(int k=0;k<T;k++) {
        cout<<k<<"\n";
        for(int i=0;i<MAXLEN;i++)
            used[i] = false;
        in>>filecount;
        in>>capacity;
        for(int i=0;i<filecount;i++)
            in>>files[i];
        int on = 0;
        for(int i=0;i<filecount;i++)
            for(int i2=i+1;i2<filecount;i2++)
                discs[on++] = disc(i, i2);
        sort(&discs[0], &discs[on]);
        reverse(&discs[0], &discs[on]);
        int total = 0;
        int usedFiles = 0;
        for(int i=0;i<on && usedFiles < filecount - 1;i++) {
            if(discs[i].size() <= capacity && !used[discs[i].first] && !used[discs[i].second]) {
                used[discs[i].first] = true;
                used[discs[i].second] = true;
                total++;
                usedFiles += 2;
            }
        }
        total += filecount - usedFiles;
        out<<"Case #"<<(k+1)<<": "<<total<<"\n";
    }
    out.close();
}