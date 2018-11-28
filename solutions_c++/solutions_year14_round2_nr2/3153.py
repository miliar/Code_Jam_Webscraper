#include <iostream>
using namespace std;

int main()
{
    long n;
    cin>>n;
    long a,b,k;
    long result=0;
    long l=1;
    while(n>0){
        result=0;
        cin>>a>>b>>k;
        long t1=a-1,t2=b-1,t3=k-1;
        long t4=0;
        for(long i=t1;i>=0;i--){
            for(long j=t2;j>=0;j--){
                t4=i&j;
                for(long m=t3;m>=0;m--){
                    //cout<<t4<<" "<<m<<endl;
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