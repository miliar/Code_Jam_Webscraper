#include<iostream>
#include<cstdio>
#include<string>
#include<cstdlib>
#include<algorithm>
#include<set>
using namespace std;
int gh[34][34];
int main(){

set <int> jk;set <int> an;
    int y=0;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        int p,q;

set <int> jk;set <int> an;
        cin>>p;
        for(int u=1;u<=4;u++){
            for(int v=1;v<=4;v++){
                cin>>gh[u][v];
                if(u==p) jk.insert(gh[u][v]);
            }
        }
        cin>>q;
        for(int u=1;u<=4;u++){
            for(int v=1;v<=4;v++){
                cin>>gh[u][v];
                if(u==q&&jk.count(gh[u][v])==1) an.insert(gh[u][v]);
            }
        }
        //cout<<an.size()<<endl;
        if(an.size()==0) cout<<"Case #"<<i<<":"<<" Volunteer cheated!\n";
        if(an.size()==1) cout<<"Case #"<<i<<": "<<*(an.begin())<<endl;
        if(an.size()>1) cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;

    }


return 0;
}
