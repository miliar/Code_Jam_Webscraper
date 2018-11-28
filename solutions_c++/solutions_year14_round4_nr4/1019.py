#include <iostream>
#include <fstream>
#define MAXLEN 8
#define MAXN 4
using namespace std;
struct trie {
    trie* subtries;
    bool null[26];
    int nodes = 0;
    
    trie() {
        subtries = (trie*) malloc(26 * sizeof(trie));
        for(int i=0;i<26;i++)
            null[i] = true;
    }
    
    void addString(string st) {
        if(st.empty())
            return;
        char on = st.at(0);
        int index = on - 'A';
        if(null[index]) {
            subtries[index] = trie();
            nodes++;
            null[index] = false;
        }
        subtries[index].addString(st.substr(1));
    }
    
    int nodeCount() {
        int total = nodes;
        for(int i=0;i<26;i++)
            if(!null[i])
                total += subtries[i].nodeCount();
        return total;
    }
    
    void deletea() {
        if(this) {
            for(int i=0;i<26;i++)
                if(!null[i])
                    subtries[i].deletea();
            free((void*)subtries);
        }
    }
};
int main() {
    ifstream in("in.txt");
    ofstream out("out.txt");
    
    int T;
    in>>T;
    for(int k=0;k<T;k++) {
        cout<<k<<"\n";
        int M,N;
        in>>M;
        in>>N;
        string strings[MAXLEN];
        for(int i=0;i<M;i++) {
            in>>strings[i];
        }
        int divisions[MAXLEN];
        for(int i=0;i<M;i++)
            divisions[i] = 0;
        int best = 0;
        int with = 0;
        while(true) {
            trie tries[MAXN];
            for(int i=0;i<M;i++)
                tries[divisions[i]].addString(strings[i]);
            int total = 0;
            bool dqed = false;
            for(int i=0;i<N && !dqed;i++) {
                int next = tries[i].nodeCount();
                if(next == 0)
                    dqed = true;
                total += next + 1;
            }
            if(!dqed) {
                if(total > best) {
                    best = total;
                    with = 1;
                }
                else if(total == best)
                    with++;
            }
            divisions[M-1]++;
            for(int i=M-1;i>0;i--) {
                if(divisions[i] == N) {
                    divisions[i] = 0;
                    divisions[i-1] ++;
                }
            }
            if(divisions[0] == N)
                break;
            for(int i=0;i<MAXN;i++)
                tries[i].deletea();
        }
        out<<"Case #"<<(k+1)<<": "<<best<<" "<<with<<"\n";
    }
    out.close();
}