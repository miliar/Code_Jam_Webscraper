#include <iostream>
#include <stdio.h>
#include <memory.h>
#include <cmath>
#include <utility>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string>
#include <vector>


#define MOD 1000000007
#define f first
#define s second

using namespace std;

string S;

int n,t;

int main(){
    srand(time(0));
freopen("input.in","r",stdin);
freopen("output.txt","w",stdout);
cin>>t;

int test=1;

int k=0;


while(t--){
        k=0;
    cin>>n;
    cin>>S; //cout<<S<<endl;
    int q=0,ch;
    for(int j=0;j<=n;j++){
        if(j<=k){
            ch=S[j];
            k+=ch-48;
        }
        else{
            //cout<<k<<endl;
            q+=j-k;
            k+=j-k;
            ch=S[j];
            k+=ch-48;
        }
    }

    cout<<"Case #"<<test<<": "<<q<<endl;
    test++;
}


return 0;
}
