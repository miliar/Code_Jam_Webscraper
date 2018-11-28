#include <iostream>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstring>
#define LL long long
using namespace std;

int main()
{
    freopen("C:\\Users\\Balasubramanian\\Downloads\\B-small-attempt0.in", "r", stdin);
    freopen("C:\\Users\\Balasubramanian\\Desktop\\C++progs\\outputb1.out", "w", stdout);
     int t1;
    cin>>t1;
    int cc=0;
    while(t1--)
    {
        cc++;
        cout<<"Case #"<<cc<<": ";
        int a,b,k;
        cin>>a>>b>>k;
        int count=0;
        for(int i=0;i<a;++i)
        for(int j=0;j<b;++j)
        {
            if((i&j)<k)count++;
        }
       cout<<count<<endl;
       
       
       
       
       
       
       
       
       
       
       
       
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return 0;
}
