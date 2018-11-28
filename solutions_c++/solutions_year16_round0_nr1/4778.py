#include <iostream>
#include <set>
using namespace std;
int main(){
    set<int>Used;
    int n;
    int y;
    cin >> n;
    for(int Case=0;Case!=n;Case++){
        int N;
        cin >> N;
        if(N == 0){
            cout << "Case #" << Case+1 << ": INSOMNIA" << endl;
            continue;
        }
        y = N;
        for(;;y+=N){
            int x = y;
            for(;x!=0;x/=10){
                Used.insert(x%10);
            }
            if(Used.size()==10){
                cout << "Case #" << Case+1 << ": " << y << endl;
                Used.erase(Used.begin(),Used.end());
                break;
            }
        }
    }
    return 0;
}