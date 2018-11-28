#include<iostream>
#include<stdio.h>
#include<vector>

using namespace std;

#define lli long long int
lli k,c,s;
vector<lli>ans;

lli power(lli n,lli p){
    lli t = 1;
    while(p--) t = t * n;
    return  t;
}

void compute(lli k,lli c){
    ans.clear();
    if(c==1){
        for(int i=1;i<=k;i++) ans.push_back(i);
        return;
    }
    ans.push_back(1);
    lli tmp = power(k,c-1);
    lli now = 1;
    for(int i=2;i<=k;i++){
        now = i + (i-1)*tmp;
        ans.push_back(now);
    }
}

void print(){
    int len = ans.size();
    cout<<ans[0];
    for(int i=1;i<len;i++) cout<<" "<<ans[i];
    cout<<endl;
}

int main(){
    int t;

    freopen("D-small-attempt1.txt","r",stdin);

    freopen("out.txt","w",stdout);
    cin>>t;
    for(int cas=1;cas<=t;cas++){
        cin>>k>>c>>s;
        compute(k,c);
        cout<<"Case #"<<cas<<": ";
        //cout<<cas<<endl;
        print();
    }
}
