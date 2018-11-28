#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

using namespace std;
typedef long long ll;


int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        int N;
        cin >> N;
        vector<int> As(N);
        for(int i=0;i<N;i++) cin >> As[i];
        
        vector<bool> process(N, false);
        int total = 0;
        for(int i=0;i<N;i++){
            int mini = -1;
            for(int j=0;j<N;j++){
                if(!process[j]){
                    if(mini==-1 || As[j] < As[mini]) mini=j;
                }
            }
            process[mini] = true;
            int left = 0;
            int right = 0;
            for(int j=0;j<mini;j++) if(!process[j]) left++;
            for(int j=mini+1;j<N;j++) if(!process[j]) right++;
            
            total+= min(left, right);
            
        }
        
        
        cout << "Case #" << t << ": " << total << endl;
    }
    
    return 0;
}