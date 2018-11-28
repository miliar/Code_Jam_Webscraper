#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <set>
#include <iomanip>
#include <fstream>
using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define REMOVE(Itr,n) (Itr).erase(remove((Itr).begin(),(Itr).end(),n),(Itr).end())
typedef long long ll;

vector<string> numbers({"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"});

int main(){
     ifstream ifs("/Users/kurodakousaku/Desktop/c練習/practice/practice/R1B_Al.txt");
     string str;
     ifs>>str;
    
    int T = stoi(str);
    
    for(int i=0;i<T;i++){
        
        string S;
        ifs>>S;
        
        vector<int> ans;
        
        /*ZERO*/
        for(int j=0;j<S.size();j++){
            if(S[j]=='Z'){
                j=-1;
                ans.push_back(0);
                REP(h,4)REP(k,S.size()){
                    if(S[k]==numbers[0][h]){
                        S.erase(S.begin()+k);
                        h++;k=-1;
                    }
                }
            }
        }
        
        /*TWO*/
        for(int j=0;j<S.size();j++){
            if(S[j]=='W'){
                j=-1;
                ans.push_back(2);
                REP(h,3)REP(k,S.size()){
                    if(S[k]==numbers[2][h]){
                        S.erase(S.begin()+k);
                        h++;k=-1;
                    }
                }
            }
        }
        
        /*FOUR*/
        for(int j=0;j<S.size();j++){
            if(S[j]=='U'){
                j=-1;
                ans.push_back(4);
                REP(h,4)REP(k,S.size()){
                    if(S[k]==numbers[4][h]){
                        S.erase(S.begin()+k);
                        h++;k=-1;
                    }
                }
            }
        }
        
        /*SIX*/
        for(int j=0;j<S.size();j++){
            if(S[j]=='X'){
                j=-1;
                ans.push_back(6);
                REP(h,3)REP(k,S.size()){
                    if(S[k]==numbers[6][h]){
                        S.erase(S.begin()+k);
                        h++;k=-1;
                    }
                }
            }
        }
        
        /*EIGHT*/
        for(int j=0;j<S.size();j++){
            if(S[j]=='G'){
                j=-1;
                ans.push_back(8);
                REP(h,5)REP(k,S.size()){
                    if(S[k]==numbers[8][h]){
                        S.erase(S.begin()+k);
                        h++;k=-1;
                    }
                }
            }
        }
        
        /*SEVEN*/
        for(int j=0;j<S.size();j++){
            if(S[j]=='S'){
                j=-1;
                ans.push_back(7);
                REP(h,5)REP(k,S.size()){
                    if(S[k]==numbers[7][h]){
                        S.erase(S.begin()+k);
                        h++;k=-1;
                    }
                }
            }
        }
        
        /*FIVE*/
        for(int j=0;j<S.size();j++){
            if(S[j]=='F'){
                j=-1;
                ans.push_back(5);
                REP(h,4)REP(k,S.size()){
                    if(S[k]==numbers[5][h]){
                        S.erase(S.begin()+k);
                        h++;k=-1;
                    }
                }
            }
        }
        
        /*ONE*/
        for(int j=0;j<S.size();j++){
            if(S[j]=='O'){
                j=-1;
                ans.push_back(1);
                REP(h,3)REP(k,S.size()){
                    if(S[k]==numbers[1][h]){
                        S.erase(S.begin()+k);
                        h++;k=-1;
                    }
                }
            }
        }
        
        /*NINE*/
        for(int j=0;j<S.size();j++){
            if(S[j]=='N'){
                j=-1;
                ans.push_back(9);
                REP(h,4)REP(k,S.size()){
                    if(S[k]==numbers[9][h]){
                        S.erase(S.begin()+k);
                        h++;k=-1;
                    }
                }
            }
        }
        
        /*THREE*/
        for(int j=0;j<S.size();j++){
            if(S[j]=='T'){
                j=-1;
                ans.push_back(3);
                REP(h,5)REP(k,S.size()){
                    if(S[k]==numbers[3][h]){
                        S.erase(S.begin()+k);
                        h++;k=-1;
                    }
                }
            }
        }
        
        sort(ans.begin(),ans.end());
        cout<<"Case #"<<i+1<<": ";
        REP(i,ans.size())cout<<ans[i];
        cout<<endl;
    }
    
    return 0;
}
