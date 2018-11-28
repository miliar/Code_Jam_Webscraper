
#include<iostream>
#include<cstring>
#include<stdio.h>
#include<cstdlib>
#include<cmath>
#include<string>
#include<vector>
#include<list>
#include<map>
#include<queue>
#include<stack>
#include<algorithm>

using namespace std;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n;
    char c[105];
    cin>>n;
    for(int t=1 ; t<=n ; t++){
        cout<<"Case #"<<t<<": ";
        memset(c,NULL,sizeof(c));
        cin>>c;
        char cc;

        int res=0;

        if(c[0]=='-'){
            cc='+';
            res--;
        }else{
            cc='-';
        }

        for(int i=0 ; i<strlen(c) ; i++){
            if(c[i]!=cc){
                cc = c[i];
                if(c[i]=='-')
                    res += 2;
            }
        }
        cout<<res<<endl;

    }
    return 0;
}
