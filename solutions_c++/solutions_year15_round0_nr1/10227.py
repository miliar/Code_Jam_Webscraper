#include <iostream>
#include <string>

using namespace std;


int process(){
    int s;
    int count = 0;
    int ans = 0;
    string si;
    cin>>s;
    cin>>si;
    
    for (int i = 0; i<=s+1; i++) {
        int use = (int)si[i];
        use = use - (int)('0');
        if(count < i){
            ans += i - count;
            count = i;
        }
         count += use;
    }
    return ans;
}


int main(){
    int T;
    cin>>T;
    for (int i = 0; i<T; i++) {
        int ans = process();
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
    return 0;
}