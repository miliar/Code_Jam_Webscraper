#include <bits/stdc++.h>

using namespace std;

typedef long long int Int;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    Int n;
    int kase,k = 1;
    cin >> kase;
    while(kase--){
    cin >> n;
    int i = 1,cnt = 0;
    set<int>s;
    s.clear();
    bool flag = true;
    Int ret,num;
    while((int)s.size() < 10){
       // cout << len << endl;
        ret = i * n;
        num = ret;
      //  cout << ret << endl;
        if(num==0){
            flag = false;
            break;
        }
        while(num){
            int r = num % 10;
            s.insert(r);
            num /= 10;
        }
        i++;
        cnt++;
    }
    if(!flag) cout << "Case #"<<k <<": "<< "INSOMNIA"<<"\n";
    else cout << "Case #" <<k <<": "<< ret << "\n";
    k++;
    }
    return 0;
}
