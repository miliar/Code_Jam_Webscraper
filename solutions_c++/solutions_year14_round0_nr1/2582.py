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
using namespace std;
int main(){
    ifstream fi("F:/draft/A-small-attempt0.in");
    ofstream fo("F:/draft/A-small-attempt0.out");
    int T=0;
    fi>>T;
    int A[ ][4]={{1,2,3,4},{1,2,3,4},{1,2,3,4},{1,2,3,4}};
    int B[ ][4]={{1,2,3,4},{1,2,3,4},{1,2,3,4},{1,2,3,4}};
    
    for(int caseInd=1;caseInd<=T;++caseInd){
        int rowA;
        fi>>rowA;
        for(int i=0;i<4;++i){
            for(int j=0;j<4;++j){
                fi>>A[i][j];
            }
        }
        int rowB;
        fi>>rowB;
        for(int i=0;i<4;++i){
            for(int j=0;j<4;++j){
                fi>>B[i][j];
            }
        }
        int num=-1;
        int numSize=0;
        for(int i=0;i<4;++i){
            for(int j=0;j<4;++j){
                if(A[rowA-1][i]==B[rowB-1][j]){
                    numSize++;
                    num=A[rowA-1][i];
                }
            }
        }
        fo<<"Case #"<<caseInd<<": ";
        if(numSize==0){
            fo<<"Volunteer cheated!";
        }else if(numSize>1){
            fo<<"Bad magician!";
        }else{
            fo<<num;
        }
        fo<<"\n";
    }
   
    
    return 0;
}