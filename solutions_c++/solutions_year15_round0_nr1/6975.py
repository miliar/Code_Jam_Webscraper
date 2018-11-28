#include <iostream>

#include <vector>
using namespace std;

int solve(const std::vector<int>& data){
    int need = 0;
    int stand = data[0];
    for(int i = 1; i != data.size(); ++i){
        int nd = i - stand;
        if(nd > 0){
            stand += nd;
            need += nd;
        }
        stand += data[i];
    }
    return need;
}
int main(){
    int n;
    cin>>n;
    for(int i = 0; i != n; ++i){
        vector<int> d;
        int x;
        cin>>x;
        for(int j = 0; j <= x; ++j){
            char c;
            cin>>c;
            d.push_back(c - '0');
        }
        cout<<"Case #"<<(i+1)<<": "<<solve(d)<<endl;
    }
    return 0;
}
