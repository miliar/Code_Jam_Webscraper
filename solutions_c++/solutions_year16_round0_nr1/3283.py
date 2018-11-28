#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    int T,N,i,j;
    ofstream file1;
    file1.open("B.txt");
    cin >>T;

    for(j=1;j<=T;j++)
    {
        cin >>N;
        int a[10]={0};

        long long int ans=0;
        int flag=0;

        file1<<"Case #"<<j<<": ";
        if(N==0)
            file1<<"INSOMNIA\n";
        else
        {
            while(flag==0)
        {
            ans=ans+N;
            long long int temp=ans;
            while(temp!=0)
            {
                a[temp%10]=1;
                temp=temp/10;
            }

            for(i=0;i<10;)
            {
                if(a[i]==1)
                    i++;
                else
                    break;
            }
            if(i==10)
                flag=1;
            else
                flag=0;
        }


           file1<<ans<<endl;
        }

    }

    return 0;
}
