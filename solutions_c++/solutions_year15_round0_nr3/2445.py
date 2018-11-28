#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits.h>
#define fir(i,n,m) for(int i=n;i<m;i++)
#define fdr(i,n,m) for(int i=n;i>=m;i--)
#define pb push_back
#define vi vector<int>
#define vs vector<string>
#define sz(v) (int)v.size()
#define all(v) v.begin(),v.end()
using namespace std;

map<string, string> qTable;
;
void init(){;
    qTable["11"] = "1";
    qTable["1i"] = "i";
    qTable["1j"] = "j";
    qTable["1k"] = "k";
    qTable["1-1"] = "-1";
    qTable["1-i"] = "-i";
    qTable["1-j"] = "-j";
    qTable["1-k"] = "-k";
    qTable["i1"] = "i";
    qTable["ii"] = "-1";
    qTable["ij"] = "k";
    qTable["ik"] = "-j";
    qTable["i-1"] = "-i";
    qTable["i-i"] = "1";
    qTable["i-j"] = "-k";
    qTable["i-k"] = "j";
    qTable["j1"] = "j";
    qTable["ji"] = "-k";
    qTable["jj"] = "-1";
    qTable["jk"] = "i";
    qTable["j-1"] = "-j";
    qTable["j-i"] = "k";
    qTable["j-j"] = "1";
    qTable["j-k"] = "-i";
    qTable["k1"] = "k";
    qTable["ki"] = "j";
    qTable["kj"] = "-i";
    qTable["kk"] = "-1";
    qTable["k-1"] = "-k";
    qTable["k-i"] = "-j";
    qTable["k-j"] = "i";
    qTable["k-k"] = "1";
    qTable["-11"] = "-1";
    qTable["-1i"] = "-i";
    qTable["-1j"] = "-j";
    qTable["-1k"] = "-k";
    qTable["-1-1"] = "i";
    qTable["-1-i"] = "i";
    qTable["-1-j"] = "j";
    qTable["-1-k"] = "k";
    qTable["-i1"] = "-i";
    qTable["-ii"] = "1";
    qTable["-ij"] = "-k";
    qTable["-ik"] = "j";
    qTable["-i-1"] = "i";
    qTable["-i-i"] = "-1";
    qTable["-i-j"] = "k";
    qTable["-i-k"] = "-j";
    qTable["-j1"] = "-j";
    qTable["-ji"] = "k";
    qTable["-jj"] = "1";
    qTable["-jk"] = "-i";
    qTable["-j-1"] = "j";
    qTable["-j-i"] = "-k";
    qTable["-j-j"] = "1";
    qTable["-j-k"] = "-i";
    qTable["-k1"] = "-k";
    qTable["-ki"] = "-j";
    qTable["-kj"] = "i";
    qTable["-kk"] = "1";
    qTable["-k-1"] = "k";
    qTable["-k-i"] = "j";
    qTable["-k-j"] = "-i";
    qTable["-k-k"] = "-1";
    qTable["i"]="i";
    qTable["1"]="1";
    qTable["j"]="j";
    qTable["k"]="k";
    qTable["-i"]="-i";
    qTable["-1"]="-1";
    qTable["-j"]="-j";
    qTable["-k"]="-k";
}

bool search(string seq, long long n){
    if(n==2){
        return false;
    }
    string pdt=seq.substr(0,1);
    int len = sz(seq);
    for(int i=1;i<n;i++){
        pdt = qTable[pdt+seq.substr((i%len),1)];
    }
    if(pdt!="-1"){
        return false;
    }
    vi ilist, klist;
    pdt = "";
    for(int i=0;i<n;i++){
        pdt = qTable[pdt+seq.substr((i%len),1)];
        if(pdt=="i"){
            ilist.pb(i);
        }
        if(pdt=="k"){
            klist.pb(i);
        }
    }

    // fir(i,0,sz(ilist)){
    //     cout<<ilist[i]<<" ";
    // }
    // cout<<endl;

    // fir(i,0,sz(klist)){
    //     cout<<klist[i]<<" ";
    // }
    // cout<<endl;

    for(int i=0;i<sz(ilist);i++){
        for(int j=0;j<sz(klist);j++){
            if(klist[j]>ilist[i]){
                pdt="";
                for(int k=ilist[i]+1;k<=klist[j];k++){
                    pdt = qTable[pdt+seq.substr((k%len),1)];
                }
                // cout<<j<<" "<<i<<" "<<klist[j]<<" "<<ilist[i]<<" "<<pdt<<endl;
                if(pdt=="j"){
                    string final = "";
                    for(int k = klist[j]+1;k<n;k++){
                        final = qTable[final+seq.substr((k%len),1)];
                    }
                    if(final=="k"){
                        return true;
                    }
                }
            }
        }
    }

    return false;
}

int main(){
    init();
    int t;
    int nCases = 1;
    cin>>t;
    while(t--){
        int l, x;
        cin>>l>>x;
        string seq;
        cin>>seq;
        string origSeq = seq;
        long long n = (long long)l*(long long)x;
        // cout<<"Seq: "<<seq<<endl;
        bool res = search(seq, n);
        if(res){
            cout<<"Case #"<<nCases<<": YES"<<endl;
        }
        else{
            cout<<"Case #"<<nCases<<": NO"<<endl;
        }
        nCases++;
    }
}
