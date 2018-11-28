#include<iostream>
#include<fstream>
#include<string>
#include<bitset>
#include<algorithm>
#include<set>
using namespace std;

string s[1000];
int main(){
    ifstream in("D.in"); ofstream out("D.out");
    int T;
    in>>T;
    for (int t=0;t<T;t++){
        out<<"Case #"<<t+1<<": ";
        int M,N;
        in>>M>>N;
        for (int i=0;i<M;i++) in>>s[i];

        int ans = -1;
        int cnt = 0;
        set<string> pres[N];
        for (int assn = 0; assn<(1<<2*M);assn++){
            bool used[N];
            for (int i=0;i<N;i++){
                pres[i].clear();
                used[i] = false;
            }
            bool works = true;
            for (int i=0;i<M;i++){
                int k = (assn>>(2*i))%4;
                if (k>=N){
                    works = false;
                    break;
                }
                used[k] = true;
                for (int j=0;j<=s[i].size();j++){
                    pres[k].insert(s[i].substr(0,j));
                }
            }
            for (int i=0;i<N;i++){
                if (!used[i]){
                    works = false;
                    break;
                }
            }
            //cout<<"here\n";
            if (!works) continue;
            int tmp = 0;
            for (int i=0;i<N;i++) tmp += pres[i].size();
            if (tmp==ans){
                cnt += 1;
            }
            if (tmp>ans){
                ans = tmp;
                cnt = 1;
            }
        }
        out<<ans<<" "<<cnt<<"\n";
    }
}
