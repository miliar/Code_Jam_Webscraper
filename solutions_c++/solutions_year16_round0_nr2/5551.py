#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;

char pancake[1024];

inline void flip(long long to){
    long long i;
    for(i=0;i<=to;i++){
        if(pancake[i]=='+')
            pancake[i]='-';
        else
            pancake[i]='+';
    }
    reverse(pancake,pancake+to+1);
}

int main(){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    long long tests,t,len,i,j,result;
    cin>>tests;
    for(t=1;t<=tests;t++){
        cin>>pancake;
        len=strlen(pancake);
        result=0;
        for(i=len-1;i>=0;i--){
            if(pancake[i]=='-'){
                if(pancake[0]=='-'){
                    flip(i);
                    result++;
                }else{
                    for(j=i;pancake[j]=='-';j--){}
                    flip(j);
                    flip(i);
                    result+=2;
                }
            }
            //cout<<pancake<<endl;
        }
        cout<<"Case #"<<t<<": "<<result<<"\n";
    }
    return 0;
}
