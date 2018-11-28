/*************************************************************************
	> File Name: bb.cpp
	> Author: 
	> Mail: 
	> Created Time: 日  4/12 03:53:00 2015
 ************************************************************************/

#include<iostream>
#include<set>
using namespace std;


const int MAX_N = 1010;
int T, D, p[MAX_N];

int main(){
    ios_base::sync_with_stdio(false);
    cin>>T;
    for(int c = 0; c < T; c++){
        cin>>D;
        multiset<int> v;
        int ans = 0;
        for(int i = 0; i < D; i++){
            cin>>p[i];
            ans = max(ans, p[i]);
        }
        int maxp = ans;
        // eat minutes
        for(int i = 1; i <= maxp; i++){ 
            int nval = i;
            for(int j = 0; j < D; j++){
                if(p[j] <= i) continue;
                nval += (p[j] + i - 1) / i - 1;
            }
            ans = min(ans, nval);
        }
        printf("Case #%d: %d\n", c + 1, ans);
    }
    return 0;
}
