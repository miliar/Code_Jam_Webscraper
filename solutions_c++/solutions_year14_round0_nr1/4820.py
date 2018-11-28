#include <bits/stdc++.h>
using namespace std;
vector<int>v;
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,a,b,i,j,CASE=0,k;
    cin>>T;
    while(T--){
        cin>>a;
        v.clear();
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                cin>>b;
                if(i==a){
                    v.push_back(b);
                }
            }
        }

        cin>>a;
        int c = 0,q = -1;
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                cin>>b;
                if(i==a){
                    for(k=0;k<v.size();k++){
                        if(v[k]==b){
                            c++;
                            q = b;
                        }
                    }
                }
            }
        }
        cout<<"Case #"<<++CASE<<": ";
        if(c==1)    cout<<q<<endl;
        else if(c==0)   puts("Volunteer cheated!");
        else    puts("Bad magician!");
    }
}
