#include<iostream>
#include<stdio.h>
#include<vector>
using namespace std;
#define LL long long int

int T, S, K, C;

int main(void)
{
     freopen("D-small-attempt0.in","r",stdin);
     freopen("D-small-attempt0.out","w",stdout);
     
     cin >> T;
     for (int cases = 1; cases <= T; cases++) {
         cin >> K >> C >> S;
         
         vector<LL> ans;
         
         for (int i = 1; i <= K; i++) {
             LL pos = i;
             for (int rep = 2; rep <= C; rep++) 
                 pos = (pos - 1) * (LL) K + (LL) i;
             
             ans.push_back(pos);
         }
         
         cout << "Case #" << cases << ":";
         for (int i = 0; i < ans.size(); i++)
             cout << " " << ans[i];
         cout << endl;
     }    
}
