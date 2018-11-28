#include <iostream>

using namespace::std;
int n, num;
bool visited[15];

long long int solve(int num){
for(int i=0; i<10; i++) visited[i]=false;
int licz=0;
int i=1;
while(1){
    long long int temp = i*num;
    while(temp > 0){
        int x=temp%10;
        if(visited[x]==false){
            visited[x]=true;
            licz++;
            if(licz==10) return i*num;
        }
        temp/=10;
    }
    i++;
}



}

int main(){

    cin>>n;

    for(int i=0; i<n; i++){
        cin>>num;
        if(num==0)   cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
        else cout<<"Case #"<<i+1<<": "<<solve(num)<<endl;
    }



return 0;
}
