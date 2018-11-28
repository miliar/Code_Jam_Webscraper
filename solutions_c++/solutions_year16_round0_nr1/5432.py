#include <bits/stdc++.h>
#include<iostream>
using namespace std;
typedef long long int lli;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
#define read() freopen("A-large.in", "r", stdin)
#define write() freopen("output1.txt", "w", stdout)
int main()
{
    read();
    write();
    map<lli, lli> m;
    lli t,n,flag=0,y, c=0,x; cin>>t; x=t;
    while(t--){
        cin>>n;
        if(n==0) {
            cout<<"Case #"<<x-t<<": INSOMNIA"<<endl;
            continue;
        }
        flag=0;c=0;
        for(lli i=0; i<=9; i++)m[i]=0;
        lli i=1;
        while(1){
            y=i*n;
            while(y){
                if(m[y%10]==0){
                    m[y%10]=1;
                    c++;
                }if(c==10) {
                    flag=1;
                    break;
                }y/=10;
            }
            if(flag==1) break;
            if(c==10) break;
            i++;
        }
        cout<<"Case #"<<x-t<<": "<<i*n<<endl;
    }
}
