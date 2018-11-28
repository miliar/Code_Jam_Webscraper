#include <iostream>
using namespace std;

int main()
{
    long n;
    cin>>n;
    int a,b,k;
    int result=0;
    int l=1;
    while(n>0){
        result=0;
        cin>>a>>b>>k;
        int t1=a-1,t2=b-1,t3=k-1;
        int t4=0;
        for(int i=t1;i>=0;i--){
            for(int j=t2;j>=0;j--){
                
                t4=i&j;
               
                for(int m=t3;m>=0;m--){
               
                    if(m==t4){
                        result++;
                    }
                }
                
            }
            
        }
    
    cout<<"Case #"<<l<<": "<<result<<endl;
    n--;
    l++;
    }
    return 0;
}