#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

vector<double>Naomi;
vector<double>Ken;
int flag[11111];

int Play1() {
    int cnt = 0,found,ind;

    sort(Naomi.begin(),Naomi.end());
    sort(Ken.begin(),Ken.end());

    for(int i=0;i<Naomi.size();i++) flag[i] = 0;

    for(int i=0;i<Naomi.size();i++) {
        found = 0;
        ind = -1;
        for(int j=0;j<Ken.size();j++) {
            if(flag[j]==0) {
                if(Naomi[i]<Ken[j]) {
                    found = 1;
                    ind = j;
                    break;
                }
                if(ind==-1) ind = j;
            }
        }
        flag[ind] = 1;
        if(found==0) cnt++;
    }
    return cnt;
}

int Play2() {
    int cnt = 0,check = 0;

    sort(Naomi.begin(),Naomi.end());
    sort(Ken.begin(),Ken.end());

    //for(int i=0;i<Naomi.size();i++) cout<<Naomi[i]<<endl;

    if(Ken[Ken.size()-1]==1.0){
        check = 1;
    }

    for(int i=check,j=0;i<Naomi.size();i++,j++) {
        if(Naomi[i]>Ken[j]) {
            cnt++;
        } else j--;
    }

    return cnt;
}

int main() {

    freopen("D_small.in","r",stdin);
    freopen("D_small.out","w",stdout);

    int test,ans1,ans2,N,CS = 0;
    double val;

    cin>>test;

    while(test--){
        cin>>N;
        Naomi.clear();
        Ken.clear();
        for(int i=0;i<N;i++) {
            cin>>val;
            Naomi.push_back(val);
        }
        for(int i=0;i<N;i++) {
            cin>>val;
            Ken.push_back(val);
        }

        ans1 = Play1();
        ans2 = Play2();

        cout<<"Case #"<<++CS<<": "<<ans2<<" "<<ans1<<endl;
    }
}
