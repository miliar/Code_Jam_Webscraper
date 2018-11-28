#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int dziel(int a,int b){
    int res=a/b;
    if(a%b>0)
        res++;
    return res;
}
main(){
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    int licznik=1;
    while(t--){
        int n;
        cin >> n;
        vector<int> T(n);
        for(auto &i:T)
            cin >> i;
        sort(T.begin(),T.end());
        int miin=1e9;
        for(int i=1;i<=T.back();i++){
           int sum=i;
           for(auto &u:T)
                sum+=ceil(dziel(u,i))-1;
            miin=min(miin,sum);
        }
        cout << "Case #"<< licznik << ": "<< miin << endl;
        licznik++;
    }
    return 0;
}
