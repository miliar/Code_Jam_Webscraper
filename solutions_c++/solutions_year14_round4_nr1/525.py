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
        int N, X;
        cin >> N >> X;
        vector<int> sizes(N);
        for(int i=0;i<N;i++) cin >> sizes[i];
        sort(sizes.begin(), sizes.end());
        
        int low = 0;
        int high = N-1;
        int ans = N;
        while(low < high){
            if(sizes[high] + sizes[low] <= X){
                ans--;
                high--;
                low++;
            }else{
                high--;
            }
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    
    return 0;
}