#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <iomanip>
#include<cstring>
using namespace std;
#define rep(i,n) for(int i = 0; i < n; ++i)
#define pii pair<int,int>

char letters[][6] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int kaku[4][2]={{'Z',0},{'W',2},{'X',6},{'G',8}};
int kaku2[2][2]={{'T',3}, {'U',4}};
int kaku3[3][2]={{'O',1}, {'F',5}, {'S',7}};

bool rm(int map[], int n){
    int i=0;
    bool flag=true;
    for(int i=0;letters[n][i]!='\0';i++){
        //cout<<letters[n][i]<<endl;
        if(map[letters[n][i]]!=0){
            flag=false;
            map[letters[n][i]]--;
        }
    }
    /*if(flag==false){
        for(int i=0;letters[n][i]!='\0';i++){
                map[letters[n][i]]++;
            }
        }
    }*/
    return flag;
}

int main(){
    int M;
    cin>>M;

    rep(i,M){
        int map['Z'+1]={};
        vector<int> ans;
        string S;
        cin>>S;

        rep(j,S.size()){
            map[S[j]]++;
        }

        rep(j,4){
            while(map[kaku[j][0]]){
                //cout<<map[kaku[j][0]]<<endl;
                ans.push_back(kaku[j][1]);
                rm(map,kaku[j][1]);
            }
        }
        rep(j,2){
            while(map[kaku2[j][0]]){
                ans.push_back(kaku2[j][1]);
                rm(map,kaku2[j][1]);
            }
        }
        rep(j,3){
            while(map[kaku3[j][0]]){
                ans.push_back(kaku3[j][1]);
                rm(map,kaku3[j][1]);
            }
        }

        rep(j,map['I']){
            ans.push_back(9);
        }

        sort(ans.begin(),ans.end());

        cout<<"Case #"<<i+1<<": ";
        rep(j,ans.size()) cout<<ans[j];
        cout<<endl;
    }

    return 0;
}
