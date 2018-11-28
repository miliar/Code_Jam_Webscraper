#include <bits/stdc++.h>
#include<algorithm>
using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.out","w",stdout);
    int t,i,j;
    long long int n;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        cin>>n;
        int bits=1023;
        if(n==0)
        {
            cout<<"INSOMNIA"<<endl;
        }
        else
        {
            long long int num=0;
            
            for(j=0;j<1000000 && bits;j++)
            {
                
                    num+=n;
                    long long int temp=num;
                    while(temp)
                    {
                        bits &= ~(1 << (temp%10) );
                        temp/=10;
                    }
            }
            if(j==1000000)
            {
                
                cout<<"INSOMNIA"<<endl;
            }
            else
            cout<<num<<endl;
        }
        
    }
	return 0;
}

