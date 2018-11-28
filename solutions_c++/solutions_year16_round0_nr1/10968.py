#include<iostream>
#include <cstdio>
//#define ONLINE
using namespace std;
int main()
{
#ifndef ONLINE
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
#endif // ONLINE
    int t;
    cin>>t;
    int arr[11]= {0},count,i,counter=1;;
    long long N,tmp;
    while(t--)
    {
        cout<<"Case #"<<counter++<<": ";
        for(i=0; i<11; i++)
            arr[i]=0;
        cin>>N;
        if(N!=0)
        {
            tmp = N;
            count=10;
            i=1;
            while(count)
            {

                while(tmp!=0)
                {
                    if(arr[tmp%10]==0)
                    {
                        arr[tmp%10] = 1;
                        count--;
                    }
                    tmp/=10;
                }
                tmp = ++i*N;
            }
            cout<<--i*N<<endl;
        }
        else cout<<"INSOMNIA\n";
    }
}
