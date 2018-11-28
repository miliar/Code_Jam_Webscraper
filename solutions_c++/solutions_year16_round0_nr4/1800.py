#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
#include <cstdio>
#include <cmath>

using namespace std;
bool task_possible(vector<long long>& res, int K, int C, int S){
    int counter=0, cc=C, kk=K, ss=S;
    while(cc>1 && kk>0 && ss>0){
        if(kk==1){
                res.push_back((K+1)*counter*2+1);
                --kk;
        }
        else{
            res.push_back((K+1)*counter*2+2);
            counter++;
            cc--;
            kk-=2;
            ss--;
        }
    }
    if(kk==0) return true;
    else if(ss==0) return false;
    else if(ss>=kk){
        while(kk>0){
            res.push_back(K-kk+1);
            kk--;
        }
        return true;
    }
    else return false;
}

int main()
{
    freopen("D://D-small-attempt2.in", "r", stdin);
    freopen("D://D-small-attempt2.out", "w", stdout);
    int K, C, S, cases;
    cin>>cases;

    for(int i=0; i<cases; ++i){
        vector<long long> res;
        cin>>K>>C>>S;
        if(task_possible(res,K,C,S)){
            cout <<"Case #"<<i+1<<":";
            for(int j=0; j<res.size(); ++j) cout<<' '<<res[j];
            cout << endl;
        }
        else cout<< "Case #"<<i+1<<": IMPOSSIBLE"<<endl;
    }

    return 0;
}
