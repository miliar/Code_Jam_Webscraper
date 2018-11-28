#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <iomanip>
#include <cstring>
#include <set>
using namespace std;
#define rep(i,n) for(int i = 0; i < n; ++i)
#define pii pair<int,int>

int main(){
    int M;
    cin>>M;

    rep(I,M){
        int T;
        cin>>T;
        set<pii, greater<pii> > vs;

        cout<<"Case #"<<I+1<<": ";

        int sum=0;
        rep(i,T){
            int tmp;
            cin>>tmp;
            vs.insert(pii(tmp,i));
            sum+=tmp;
        }

        rep(i,(sum/2)-1+sum%2){
            auto itr=vs.begin();
            auto p=*itr;

            cout<<(char)('A'+(*itr).second);
            if((*itr).first!=1){
                vs.insert(pii(p.first-1,p.second));
            }
            vs.erase(itr++);

            if(!(sum%2==1&&i==((sum/2)-1))){
                p=*itr;
                cout<<(char)('A'+(*itr).second)<<" ";

                if((*itr).first!=1){
                    vs.insert(pii(p.first-1,p.second));
                }
                vs.erase(itr);
            }
            else
            {
                cout<<" ";
            }
        }
        auto itr=vs.begin();
        cout<<(char)('A'+(*itr).second);
        itr++;
        cout<<(char)('A'+(*itr).second)<<endl;
    }

    return 0;
}
