#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
using namespace std;


void show(vector<int>& a,int l,int r){
    for(int i=l; i<=r; i++){
        cout << a[i] << " ";
    }
    cout << endl;
}

int solve(const int X,std::vector<int>& S){
    sort(S.begin(), S.end());
    
    int res = 0;
    int left = 0;
    int right = S.size()-1;

    while(left < right){
        // cout << "@" << left << " " << right << endl;
        if(S[left] + S[right] <= X){
            left++, right--, res++;
        }
        else{
            right--, res++;
        }
        // show(S,left,right);
    }
    res += (right == left);
    return res;
}


int main(){
    int Ncases;
    cin >> Ncases;
    for(int cases=1;cases<=Ncases;cases++){

        //solve it
        int N,X;
        vector<int> S;

        cin >> N >> X;
        for(int i=0;i<N;i++){
            int s;
            cin >> s;
            S.push_back(s);
        }
        
        cout << "Case #" << cases << ": "; 
    
        //output answer here
        cout << solve(X,S);

        cout << endl;
    }

    return 0;
}
