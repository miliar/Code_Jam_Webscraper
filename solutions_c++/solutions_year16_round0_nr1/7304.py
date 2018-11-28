#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,k,m,i,t,temp=1,count=1;
    cin>>t;
    for(temp=1;temp<=t;temp++) {
        cin>>n;
        m=n;
        k=n;
        int a[10]={0};
        count=1;
        int j=0;
        while(count<=100){
            while(m>0){
                i=m%10;
                m=m/10;
                if(a[i]==0)
                    a[i]=1;
                
            }
            for(j=0;j<10;j++){
                if(a[j]!=1)
                break;
            }
            if(j==10)
              break;
            count++;
            m=n*count;
            k=m;
            
        }
        if(count<101)
            cout<<"Case #"<<temp<<": "<<k<<endl;
        else
            cout<<"Case #"<<temp<<": "<<"INSOMNIA"<<endl;
    }
        
          
    
    
    
    return 0;
}
