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
#include <fstream>
using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define REMOVE(Itr,n) (Itr).erase(remove((Itr).begin(),(Itr).end(),n),(Itr).end())
#define PB_VEC(Itr1,Itr2) (Itr1).insert((Itr1).end(),(Itr2).begin(),(Itr2).end())
typedef long long ll;


bool all(bool used[10]){
    REP(i,10)if(!used[i])return false;
    return true;
}

int main(){
    ifstream ifs("/Users/kurodakousaku/Desktop/c練習/practice/practice/in.txt");
    string str;
    ifs>>str;
    
    int T = stoi(str);
    
    for(int i=0;i<T;i++){
        ifs>>str;
        int N = stoi(str);
        if(N==0){
            cout<<"Case #"<<i+1<<":"<<" INSOMNIA"<<endl;
        }else{
            bool used[10];
            REP(j,10)used[j]=false;
            int count=1;
            while(true){
                int t=count*N;
                while(t!=0){
                    used[t%10]=true;
                    t/=10;
                }
                
                if(all(used))goto succ;
                count++;
            }
        succ:;
            cout<<"Case #"<<i+1<<": "<<N*(count)<<endl;
        }
    }
    
    return 0;
}
