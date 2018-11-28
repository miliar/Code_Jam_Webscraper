#include<stdio.h>
#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<string>
using namespace std;

#include <unordered_set>

int aa=10;
class Solution {
public:
    bool isScramble(string s1, string s2) {
        if(s1.length()!=s2.length())return false;
        if(s1.length()==0) return true;
        vector<vector<vector<bool>>> mtr;
        vector<vector<bool>> tmp1;
        vector<bool> tmp2;
        mtr.push_back(tmp1);
        for(int i=0;i<s1.length();++i){
            mtr[0].push_back(tmp2);
            for(int j=0;j<s1.length();++j){
                if(s1[i]==s2[j]) mtr[0][i].push_back(true);
                else mtr[0][i].push_back(false);
            }
        }
        for(int k=2;k<=s1.length();++k){
            mtr.push_back(tmp1);
            for(int i=0;i<=s1.length()-k;++i){
                mtr[k-1].push_back(tmp2);
                for(int j=0;j<=s2.length()-k;++j){
                    bool res=false;
                    /*if((s1[i]==s2[j]&&mtr[k-2][i+1][j+1])||(s1[i]==s2[j+k-1]&&mtr[k-2][i+1][j])){
                        //mtr[k-1][i].push_back(true);
                        res=true;
                    }*/
                    for(int n=i;n<i+k-1;++n){
                        if(mtr[n-i][i][j]&&mtr[i+k-1-n-1][n+1][j+n-i+1]) res=true;
                        if(mtr[n-i][i][j+k-1-(n-i)]&&mtr[i+k-1-n-1][n+1][j]) res=true;
                        if(res)break;
                    }
                    /*if((s1[i+k-1]==s2[j]&&mtr[k-2][i][j+1])||(s1[i+k-1]==s2[j+k-1]&&mtr[k-2][i][j])){
                        //mtr[k-1][i].push_back(true);
                        res=true;
                    }*/
                    mtr[k-1][i].push_back(res);
                }
            }
        }
        return mtr[s1.length()-1][0][0];
    }
    
};
/*int main(){
    Solution sss;
    vector<int> prices;
    prices.push_back(1);
    prices.push_back(2);
    prices.push_back(4);
    unordered_set<string> dict;
    //dict.insert("hot");
    //dict.insert("dog");
    //dict.insert("dot");
    //string start="hot";
    //string end="dog";
    //bool tmp=sss.isScramble("xstjzkfpkggnhjzkpfjoguxvkbuopi","xbouipkvxugojfpkzjhnggkpfkzjts");
    bool tmp=sss.isScramble("abcd","badc");
    cout<<tmp<<endl;
    //cout<<t<<endl;
    int a;
    cin>>a;
    return 0;
}*/

//source here
#include <iostream>
#include <fstream>
#include <math.h>
#include <iomanip> 
using namespace std;
int main(){
    ifstream fi("F:/draft/B-large.in");
    ofstream fo("F:/draft/B-large.out");
    //ifstream fi("F:/draft/in.txt");
    //ofstream fo("F:/draft/out.txt");
    int T=0;
    fi>>T;
    //int A[ ][4]={{1,2,3,4},{1,2,3,4},{1,2,3,4},{1,2,3,4}};
    //int B[ ][4]={{1,2,3,4},{1,2,3,4},{1,2,3,4},{1,2,3,4}};
    
    for(int caseInd=1;caseInd<=T;++caseInd){
        double C;
        double F;
        double X;
        fi>>C>>F>>X;
        int Q=ceil((X*F-C*F-2*C)/(C*F));
        double time=0;
        if(Q<=0){
            time=X/2;
        }else{
            for(int i=0;i<Q;++i){
                time+=C/(2+double(i)*F);
            }
            time+=X/(Q*F+2);
        }
        fo<<"Case #"<<caseInd<<": "<<setprecision(7)<<fixed<<time<<"\n";
    }
   
    
    return 0;
}