#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int func(long long int r, long long int t)
{
    long long int temp=0;
    int counter=0;
    for(int i=0;temp<=t;i++)
    {
        counter++;
        temp+=((r+2*i+1)*(r+2*i+1)-(r+2*i)*(r+2*i)); 
        //cout<<temp<<endl;
    }
    return counter-1;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int temp,T;
  freopen("A-small-attempt0.in","r",stdin);
  freopen("key.txt","w",stdout);
    cin>>T;
    long long int r,t;
    for(int i=0;i<T;i++)
    {
            cin>>r>>t;
            cout<<"Case #"<<i+1<<": "<<func(r,t)<<endl;
    }
        //cin>>N;
    return 0;
}
