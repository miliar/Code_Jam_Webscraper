#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<cstdio>
#include <cmath>
#include <climits>
#define FOR(i,n) for(int i=0;i<n;i++)
using namespace std;
int maxi = 0;
int calc(vector<int>& tabl,int cur_prof=0,int prof_max=INT_MAX){
    if(cur_prof > prof_max){
        return INT_MAX-100;
    }
    int id_m=0;
    FOR(i,tabl.size()){
        if(tabl[i]>tabl[id_m]){
            id_m = i;
        }
    }
    int val_m = tabl[id_m];
    if(val_m<=3){
        return val_m;
    }
    int res=val_m;
    
    for(int i=1;i<val_m;i++){   
        tabl[id_m] = i;
        tabl.push_back(val_m - i);
        res = min(res,1+calc(tabl,cur_prof+1,min(prof_max,val_m-cur_prof+1)));
        tabl.pop_back();
        tabl[id_m]=val_m;
    }
    return res;
}

int main(){
    int T;
    cin>>T;
    FOR(k,T){
        int n;
        cin>>n;
        vector<int> t(n,0);
        
        FOR(i,n){
            cin>>t[i];
            maxi = max(maxi,t[i]);
        }
        int r = calc(t);
        cout<<"Case #"<<k+1<<": "<<r<<endl;
    }
}
