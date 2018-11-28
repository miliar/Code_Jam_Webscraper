#include <bits/stdc++.h>
using namespace std;
unsigned long long int  N;
bool visited[10]={false};
int nb;
void find_and_fill(unsigned long long int m){

    while(m!=0){
        if(!visited[m % 10])
            nb++;
        visited[m%10]=true;
        m/=10;
    }
    return ;

}
int main (){
    freopen("A-Large.in","r",stdin);
    freopen("A-small-attempt0.out","w+",stdout);
    int cas;
    cin>>cas;
    for (int caseof=1 ; caseof <= cas ; caseof++){
    cin>> N ;
    nb=0;
    memset(visited,false, sizeof visited);
    if (N == 0 ){
            cout<<"Case #"<<caseof<<": "<<"INSOMNIA"<<endl;

        continue;
    }
    unsigned long long int  j = 1;
    while(nb!=10){
            //cout<<N*j<<endl;
            find_and_fill(N*j);
            j++;

    }
    cout<<"Case #"<<caseof<<": "<<N*--j<<endl;
    }
}
