#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#define fr(i,a,b) for(int i=a; i<b; i++)

using namespace std;
typedef vector<int> vi;


int main(){
    freopen("D-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T, X, R, C;
    cin>>T;
    fr(t,0,T){
        bool rich=0;
        cin>>X>>R>>C;
        if((R*C)%X) rich=1;
        else if((X+1)/2>min(R,C)) rich=1;
        else if(X>max(R,C)) rich=1;
        else if(X>6) rich=1;
        else if(!(X%2)&&X-1>min(R,C)) rich=1;
        if(rich) cout<<"Case #"<<t+1<<": RICHARD"<<endl;
        else cout<<"Case #"<<t+1<<": GABRIEL"<<endl;
    }
}
