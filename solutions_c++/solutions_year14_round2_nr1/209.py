#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<vector>
#include<iostream>
using namespace std;


int n;
struct extractForm{
    vector<pair<char,int> > v;
    extractForm(string str){
        int idx=0;
        while(idx<str.size()){
            int i=0;
            for(i = idx ; i < str.size()&&str[i]==str[idx];++i);
            v.push_back(make_pair(str[idx],i-idx));
            idx=i;
        }
    }
};
vector<extractForm> v;
bool isPossible(){
    for(int i = 0 ; i < v.size() ; ++ i ){
        if(v[i].v.size()!=v[0].v.size())return false;
    }
    for(int i = 0 ; i < v[0].v.size();++i){
        for(int j = 0 ; j < v.size() ; ++ j ){
            if(v[j].v[i].first!=v[0].v[i].first)return false;
        }
    }
    return true;
}
void solve(){
    cin >> n;
    v.clear();
    for(int i =0  ; i < n ; ++ i ){
        string str;
        cin >> str;
        v.push_back(extractForm(str));
    }
    if(!isPossible()){
        printf("Fegla Won\n");
        return;
    }
    int minAns=0;
    for(int i = 0 ; i < v[0].v.size() ; ++ i ){
        int minAdjust=10000000;
        for(int k = 1;k<=200;++k){
            int toAdjust=0;
            for(int j = 0 ; j < v.size() ; ++ j ){
                toAdjust+=abs(v[j].v[i].second-k);
            }

            minAdjust=min(minAdjust,toAdjust);
        }

        minAns+=minAdjust;

    }
    printf("%d\n",minAns);
}
int main(){
    freopen("A-large"".in","r",stdin);
    freopen("A-large"".out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 0 ; i < t;  ++ i ){
        printf("Case #%d: ",i+1);
        solve();
    }

}
