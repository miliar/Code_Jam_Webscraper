#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <iterator>
#include <cctype>

using namespace std;

//T N X S
int ev2(vector <int> &S,vector <int> &msk,int i){
    int sum = 0;
    
    for(int k=0;k<S.size();k++){
        if(i!=k){
            if(msk[i]==0){
                if(msk[k] ==0){
                    if((S[i]-S[k])*(long long)(i-k)<=0){
                        sum++;
                    }
                }
                else{
                    if(k<i)sum++;
                }
                
            }
            else{
                if(msk[k]==1){
                    if((S[i]-S[k])*(long long)(i-k)>=0){
                        sum++;
                    }
                }
                else if(k>i)sum++;
            }
        }
    }
    return sum;
}

int dif(vector <int> &S, vector <int> &msk, int i){
    int a = ev2(S,msk,i);
    msk[i] = 1-msk[i];
    int b =ev2(S,msk,i);
    msk[i] = 1-msk[i];
    
    return a-b;
}
int feval(vector <int> &S, vector <int> &msk){
    int sum =0;
    for(int i=0;i<S.size();i++){
        sum+=ev2(S,msk,i);
    }
    return sum/2;
}


int main(){
    int T;
    cin >> T;
    int result = 0;
    for(int t=0;t<T;t++){
        int N;
        cin >> N;
        vector <int> vS;
        for(int i=0;i<N;i++){
            int a;
            cin >> a;
            vS.push_back(a);
        }
        bool b = true;
        vector <int> msk;
        msk.assign(vS.size(),0);
        while(b){
            bool b2 = false;
            for(int i=0;i<vS.size();i++){
                int k = dif(vS,msk,i);
                if(k>0){
                    b2=true;
                    msk[i] = 1-msk[i];
                }
            }
            if(!b2) b = false;
        }
        result = feval(vS,msk);
        cout << "Case #" << t+1 << ": " << result << endl;
    }
    
    return 0;
}

