#include<math.h>
#include<algorithm>
#include<iostream>
#include<cstdio>
#include<stdlib.h>
#include<cstring>
#include<vector>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    for(int i=1; i<=T;i++)
    {
        int n, z=0;
        cin>>n;
        int hash[10] = {0}, count = 0, num = n;
        cout<<"Case #"<<i<<": ";
        if(n == 0)
        {
            cout<<"INSOMNIA"<<endl;
        }
        else
        {
            while(count!=10)
            {
                z++;
                num = n*z;
                while(num)
                {
                    int dig = num%10;
                    num/=10;
                    if(!hash[dig])
                    {
                        count++;
                        hash[dig] = 1;
                    }
                }
            }
            cout<<n*z<<endl;
        }
    }
    return 0;
}
