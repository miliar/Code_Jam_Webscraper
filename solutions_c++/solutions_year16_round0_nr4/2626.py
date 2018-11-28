#include<iostream>
#include<math.h>
#include<cstdio>

using namespace std;
int main()
{
    int T,K,C,S,x=1;
    cin>>T;
    while(T--)
    {
        cin>>K>>C>>S;
        if(S<K)
        {cout<<"Case #"<<x++<<": IMPOSSIBLE\n"; continue;}
        long long int KC=pow(K,C-1);
        cout<<"Case #"<<x++<<":";
        for(int i=0;i<K;i++)
            cout<<" "<<(1+(KC*i));
        cout<<endl;
    }
    return 0;
}
