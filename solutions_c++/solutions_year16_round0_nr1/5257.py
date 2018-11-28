#include <iostream>
#include <bits/stdc++.h>

using namespace std;
int total;
void digits(bool a[10],long long int n){
    int k=n;
    while(k>0){
        int temp=k%10;
        if(a[temp]==false){
            a[temp]=true;
            total++;
        }
        k=k/10;
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ans3.txt","w",stdout);
    bool visited[10];
    int t;
    cin>>t;
    for(int h=1;h<=t;h++){
    int n;
    cin>>n;
    cout<<"Case #"<<h<<": ";
    fill(visited,visited+10,false);
    total=0;
    long long int k=n;
    if(n==0)
        cout<<"INSOMNIA"<<endl;
    else{
    while(total!=10){
        digits(visited,k);
        k+=n;
    }
    cout<<k-n<<endl;
   }
    }
    return 0;
}
