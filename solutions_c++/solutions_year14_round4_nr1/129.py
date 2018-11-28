#include<iostream>
#include<fstream>
#include<string>
#include<bitset>
#include<algorithm>
#include<set>
using namespace std;
int discs[10005];
int main(){
    ifstream in("A.in"); ofstream out("A.out");
    int T;
    in>>T;
    multiset<int> d;
    for (int t=0;t<T;t++){
        out<<"Case #"<<t+1<<": ";
        int N,X;
        in>>N>>X;
        d.clear();
        for (int i=0;i<N;i++){
            in>>discs[i];
            d.insert(discs[i]);
        }
        multiset<int>::iterator it, it2;
        int ans = 0;
        while(!d.empty()){
            it = d.end();
            --it;
            int val = *it;
            d.erase(it);
            it2 = d.upper_bound(X - val);
            if (it2!=d.begin()){
                it2--;
                d.erase(it2);
            }
            ans++;
        }
        out<<ans<<"\n";
    }
}
