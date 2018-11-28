#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <iostream>
#include <fstream>
#include <map>
#include <utility>
#include <vector>
using namespace std;

long long int p,q;
string s;

void updatePQ(){
    p=0;
    q=0;
    //cout<<"done2";
    int len = s.length();
    //cout<< len;
    int i=0;
    char c = s.at(i);
    while(c != '/'){
        c = c-'0';
        p = p*10 + (long long int )c;
        i++;
        c = s.at(i);
    }
    //cout<<"done2";
    i++;
    //c = s.at(i);
    //cout<< "value of i :" << i;
    while(i<len){
        c = s.at(i);
        c = c-'0';
        q = q*10 + (long long int )c;
        i++;
        //cout<< "value of i :" << i << "is not a prob \n";
        //c = s.at(i);
    }
}

int main(){

    int T;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1; t<=T; t++){
        //scanf("%s",&s);
        cin>>s;
        //cout<<s;
        //cout<< "done";
        updatePQ();
        int ans = 0;
        while(p < q){
            p = p*2;
            ans++;
        }
        if(p==q){
            printf("Case #%d: %d\n",t,ans);
        }
        else if( q&(q-1) ){
            printf("Case #%d: impossible\n",t);
        }
        else{
            printf("Case #%d: %d\n",t,ans);
        }
    }

return 0;
}

