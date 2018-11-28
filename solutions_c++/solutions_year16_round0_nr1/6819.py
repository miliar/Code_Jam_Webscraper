#include <bits/stdc++.h>

using namespace std;

#define ll long long


void comp(int visited[],ll num,ll i){
    ll temp=num*i;
    while(temp!=0){
        //cout<<"I am temp"<<temp<<endl;
        visited[temp%10]=1;
        temp/=10;
    }
}
int checkqq(int visited[]){
    for(int i=0;i<10;i++){
        if(!visited[i])
            return 0;
        //cout<<"retr"<<endl;
    }
    return 1;
}

int main() {
	// your code goes here
    ll t,num,i;
    cin>>t;
    for(int j=1;j<=t;j++){
        int visited[10]={0};
        cin>>num;
        i=0;
        if(num==0){
            cout<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        while(1){
            comp(visited,num,i);
            if(checkqq(visited)){
                cout<<"Case #"<<j<<": "<<num*i<<endl;
                break;
            }i++;
        }
    }
	
	return 0;
}