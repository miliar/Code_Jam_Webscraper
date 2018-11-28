#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <set>
#include <map>
#include <queue>
#include <vector>
using namespace std;

class Fenwick{
public:
    vector<int> tree;
    Fenwick(int n):tree(n+1){}
    int sum(int pos){
        ++pos;
        int ret=0;
        while(pos>0){
            ret+=tree[pos];
            pos&=(pos-1);
        }
        return ret;
    }
    void add(int pos,int val){
        ++pos;
        while(pos<tree.size()){
            tree[pos]+=val;
            pos+=(pos&-pos);
        }
    }
};


int main(){
    ifstream fcin;
    ofstream fout;
    fcin.open("A-large.in");
    fout.open("B.out");
    int testCase;
    long long len;
    fcin>>testCase;
    string s;
    set<int> sx;
    for(int i=1;i<=testCase;i++){
        fcin>>s;
        len=s.length();
        int alpha[27]={0,};
        int cnt[10]={0,};
        for(int j=0;j<len;j++){
            alpha[s[j]-'A'+1]++;
        }
        cnt[0]+=alpha['Z'-'A'+1];
        alpha['E'-'A'+1]-=alpha['Z'-'A'+1];
        alpha['R'-'A'+1]-=alpha['Z'-'A'+1];
        alpha['O'-'A'+1]-=alpha['Z'-'A'+1];
        alpha['Z'-'A'+1]=0;
        cnt[8]+=alpha['G'-'A'+1];
        alpha['E'-'A'+1]-=alpha['G'-'A'+1];
        alpha['I'-'A'+1]-=alpha['G'-'A'+1];
        alpha['H'-'A'+1]-=alpha['G'-'A'+1];
        alpha['T'-'A'+1]-=alpha['G'-'A'+1];
        alpha['G'-'A'+1]=0;
        cnt[6]+=alpha['X'-'A'+1];
        alpha['S'-'A'+1]-=alpha['X'-'A'+1];
        alpha['I'-'A'+1]-=alpha['X'-'A'+1];
        alpha['X'-'A'+1]=0;
        cnt[4]+=alpha['U'-'A'+1];
        alpha['F'-'A'+1]-=alpha['U'-'A'+1];
        alpha['O'-'A'+1]-=alpha['U'-'A'+1];
        alpha['R'-'A'+1]-=alpha['U'-'A'+1];
        cnt[2]+=alpha['W'-'A'+1];
        alpha['T'-'A'+1]-=alpha['W'-'A'+1];
        alpha['O'-'A'+1]-=alpha['W'-'A'+1];
        cnt[3]+=alpha['T'-'A'+1];
        alpha['H'-'A'+1]-=alpha['T'-'A'+1];
        alpha['R'-'A'+1]-=alpha['T'-'A'+1];
        alpha['E'-'A'+1]-=alpha['T'-'A'+1];
        alpha['E'-'A'+1]-=alpha['T'-'A'+1];
        cnt[5]+=alpha['F'-'A'+1];
        alpha['I'-'A'+1]-=alpha['F'-'A'+1];
        alpha['V'-'A'+1]-=alpha['F'-'A'+1];
        alpha['E'-'A'+1]-=alpha['F'-'A'+1];
        cnt[1]+=alpha['O'-'A'+1];
        alpha['N'-'A'+1]-=alpha['O'-'A'+1];
        alpha['E'-'A'+1]-=alpha['O'-'A'+1];
        cnt[7]+=alpha['V'-'A'+1];
        alpha['S'-'A'+1]-=alpha['V'-'A'+1];
        alpha['E'-'A'+1]-=alpha['V'-'A'+1];
        alpha['E'-'A'+1]-=alpha['V'-'A'+1];
        alpha['N'-'A'+1]-=alpha['V'-'A'+1];
        cnt[9]+=alpha['E'-'A'+1];
        fout<<"Case #"<<i<<": ";
        for(int j=0;j<10;j++){
            for(int k=0;k<cnt[j];k++){
                fout<<j;
            }
        }
        fout<<"\n";
    }
}