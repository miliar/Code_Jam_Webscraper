#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <fstream>
#include <vector>
using namespace std;
int pState[10]= {0};
int prev(int val) {
    for(int i=val; i>=0; i--) {
        if(pState[i]!=0)
            return i;
    }
    return 0;
}
int solve(vector<int> pState,int presentMax) {
    //cout<<presentMax<<endl;
    //system("pause");
    int ans=10;
    if(presentMax==1)
        return 1;
    for(int i=1; i<presentMax; i++) {
        pState[i] += pState[presentMax];
        pState[presentMax - i] += pState[presentMax];
        for (int j = presentMax - 1; j > 0; j--) {
            if (pState[j] > 0) {
                ans=min(ans, solve(pState,j));
                break;
            }
        }
        pState[i] -= pState[presentMax];
        pState[presentMax - i] -= pState[presentMax];
    }
    ans = min(ans+pState[presentMax], presentMax);
    for (int i = 0; i < presentMax; i++)
        pState[i]=pState[i+1];
    pState[presentMax]=0;
    for (int i = presentMax-1; i > 0; i--)
        if (pState[i] > 0) {
            ans=min(ans, solve(pState,i)+1);
            break;
        }
    return ans;
}
int main(int argc, char* argv[]) {
    ifstream input(argv[1]);
    ofstream output(argv[2]);
    int t;
    input>>t;
    int k=0;
    while(k!=t) {
        k++;
        vector<int>pState(10,0);
        int D;
        input>>D;
        int maxCakes=-1;
        for(int i=0; i<D; i++) {
            int noOfPancackes;
            input>>noOfPancackes;
            pState[noOfPancackes]++;
            maxCakes =max(noOfPancackes,maxCakes);
        }
        int ans= solve(pState,maxCakes);
        output<<"Case #"<<k<<": "<<ans<<endl;
    }

    return 0;
}
