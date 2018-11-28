#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ll;



int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        int r1, r2;
        vector<int> b1(16);
        vector<int> b2(16);
        
        cin >> r1;
        for(int i=0;i<16;i++) cin>>b1[i];
        cin >> r2;
        for(int i=0;i<16;i++) cin>>b2[i];
        vector<int> poss(17,0);
        for(int i=0;i<4;i++) poss[b1[4*(r1-1)+i]]++;
        for(int i=0;i<4;i++) poss[b2[4*(r2-1)+i]]++;
        
        int res = -1;
        int n2 = 0;
        for(int i=1;i<=16;i++){
            if(poss[i]==2){
                n2++;
                res = i;
            }
        }
        cout << "Case #" << t << ": ";
        if(n2==1) cout << res << endl;
        else if(n2==0) cout << "Volunteer cheated!" << endl;
        else if(n2>1) cout << "Bad magician!" << endl;
        
        
    }

    return 0;
}