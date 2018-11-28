#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;
#define FOR(i,a,b) for(int i=int(a);i<int(b);i++)
#define MAX 1000

bool pal(string cad){
    int n=cad.length(),t;
    t=n-1;
    FOR(i,0,(n/2)){
        if(cad[i]!=cad[t])return false;
        t--;
    }
    return true;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    long long val,a,b,s;
    cin>>n;
    FOR(i,1,n+1){
        cin>>a>>b;
        s=sqrt(a);
        if(s*s!=a)s++;
        val=s*s;
        string cad1,cad2;
        int count=0;
        while(val<=b){
            ostringstream stream1,stream2;
            stream1<<s;
            stream2<<val;
            cad1=stream1.str();
            cad2=stream2.str();
            //cout<<cad<<endl;
            if(pal(cad1)&&pal(cad2)){
                count++;
            }
            s++;
            val=(s*s);
        }
        cout<<"Case #"<<i<<": "<<count<<endl;
    }
    return 0;
}
