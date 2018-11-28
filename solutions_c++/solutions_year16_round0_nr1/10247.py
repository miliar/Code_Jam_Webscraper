#include <iostream>
#include<fstream>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int T,i,j,k,flag,a;
    cin>>T;
    for(i=0;i<T;i++)
    {
        int num[10]={0,0,0,0,0,0,0,0,0,0};
        int N;
        cin>>N;
        if(N==0)
        {
            cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
            continue;
        }
        for(j=1;;j++)
        {
            long long n;
            flag=0;
            n=j*N;

            while(n!=0)
            {

                a=n%10;
                if(num[a]==0)
                    num[a]=1;
                n=n/10;
            }
            for(k=0;k<10;k++)
            {
                if(num[k]==1)
                    flag+=1;
            }
            if(flag==10)
            {
                cout<<"Case #"<<i+1<<": "<<(j*N)<<endl;
                break;
            }
        }
    }
    return 0;
}
