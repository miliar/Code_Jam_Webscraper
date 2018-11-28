#include<iostream>
using namespace std;
int main()
{
    int T,i;
    cin>>T;
    for(i=0;i<T;i++)
    {
        int j;
        long long int N,N1,N2;
        char A[10];
        cin>>N;
        if(N==0)
        {
            cout<<"Case #"<<i+1<<": INSOMNIA"<<"\n";
            continue;
        }
        N1=N;
        for(j=0;j<10;j++)
        {
            A[j]='F';
        }
        for(j=1;;j++)
        {
            N1=N*j;
            N2=N1;
            int k,x;
            while(N2>0)
            {
                x=N2%10;
                A[x]='T';
                N2=N2/10;
            }
            for(k=0;k<10;k++)
            {
                if(A[k]=='F')
                    break;
            }
            if(k==10)
            {
                cout<<"Case #"<<i+1<<": "<<N1<<"\n";
                break;
            }
        }
    }
    return 0;
}
