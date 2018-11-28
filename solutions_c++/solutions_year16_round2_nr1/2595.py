#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <set>
using namespace std;
int main(){
    ifstream fcin;
    ofstream fout;
    fcin.open("input.in");
    fout.open("output.out");
    int T;
    long len;
    //0 8 6 4 2 3 5 1 7 9 순으로 넣자
    //Z G X U W R F O V
    fcin>>T;
    string s;
    set<int> sx;
    int wordCnt[27]={0,};
    int numCnt[10]={0,};
    for(int i=1;i<=T;i++){
        fcin>>s;
        len=s.length();
        memset(wordCnt,0,sizeof(wordCnt));
        memset(numCnt,0,sizeof(numCnt));
        for(int j=0;j<len;j++){
            wordCnt[s[j]-'A'+1]++;
        } //무조건
        
        numCnt[0]+=wordCnt['Z'-'A'+1];
        wordCnt['E'-'A'+1]-=wordCnt['Z'-'A'+1];
        wordCnt['R'-'A'+1]-=wordCnt['Z'-'A'+1];
        wordCnt['O'-'A'+1]-=wordCnt['Z'-'A'+1];
        wordCnt['Z'-'A'+1]=0;
        //0

        numCnt[8]+=wordCnt['G'-'A'+1];
        wordCnt['E'-'A'+1]-=wordCnt['G'-'A'+1];
        wordCnt['I'-'A'+1]-=wordCnt['G'-'A'+1];
        wordCnt['H'-'A'+1]-=wordCnt['G'-'A'+1];
        wordCnt['T'-'A'+1]-=wordCnt['G'-'A'+1];
        wordCnt['G'-'A'+1]=0;
        //8
        
        numCnt[6]+=wordCnt['X'-'A'+1];
        wordCnt['S'-'A'+1]-=wordCnt['X'-'A'+1];
        wordCnt['I'-'A'+1]-=wordCnt['X'-'A'+1];
        wordCnt['X'-'A'+1]=0;
        //6
        numCnt[4]+=wordCnt['U'-'A'+1];
        wordCnt['F'-'A'+1]-=wordCnt['U'-'A'+1];
        wordCnt['O'-'A'+1]-=wordCnt['U'-'A'+1];
        wordCnt['R'-'A'+1]-=wordCnt['U'-'A'+1];

        numCnt[2]+=wordCnt['W'-'A'+1];
        wordCnt['T'-'A'+1]-=wordCnt['W'-'A'+1];
        wordCnt['O'-'A'+1]-=wordCnt['W'-'A'+1];
        
        numCnt[3]+=wordCnt['T'-'A'+1];
        wordCnt['H'-'A'+1]-=wordCnt['T'-'A'+1];
        wordCnt['R'-'A'+1]-=wordCnt['T'-'A'+1];
        wordCnt['E'-'A'+1]-=wordCnt['T'-'A'+1];
        wordCnt['E'-'A'+1]-=wordCnt['T'-'A'+1];
        
        numCnt[5]+=wordCnt['F'-'A'+1];
        wordCnt['I'-'A'+1]-=wordCnt['F'-'A'+1];
        wordCnt['V'-'A'+1]-=wordCnt['F'-'A'+1];
        wordCnt['E'-'A'+1]-=wordCnt['F'-'A'+1];

        numCnt[1]+=wordCnt['O'-'A'+1];
        wordCnt['N'-'A'+1]-=wordCnt['O'-'A'+1];
        wordCnt['E'-'A'+1]-=wordCnt['O'-'A'+1];
        
        numCnt[7]+=wordCnt['V'-'A'+1];
        wordCnt['S'-'A'+1]-=wordCnt['V'-'A'+1];
        wordCnt['E'-'A'+1]-=wordCnt['V'-'A'+1];
        wordCnt['E'-'A'+1]-=wordCnt['V'-'A'+1];
        wordCnt['N'-'A'+1]-=wordCnt['V'-'A'+1];
        
        numCnt[9]+=wordCnt['E'-'A'+1];

        fout<<"Case #"<<i<<": ";
        for(int l=0;l<10;l++){
            for(int k=0;k<numCnt[l];k++){
                fout<<l;
            }
        }
        fout<<"\n";
    }
}

