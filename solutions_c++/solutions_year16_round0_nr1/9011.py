#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int k=0;k<T;k++)
    {
        long long N,i=1;
        cin>>N;
        bool A[10] = {false};
        if(N==0)
        {
            cout<<"Case #"<<k+1<<": INSOMNIA"<<endl;
            continue;
        }
        while(1)
        {
            int flag=0;
            long long f = i*N;
            while(1)
            {
                if(A[f%10]==false)
                    A[f%10] = true;
                if(f/10==0)
                    break;
                f/=10;
            }

            for(int j=0;j<10;j++)
            {
                if(A[j]==false)
                {
                    flag++;
                }
            }
            if (flag==0)
                break;
            i++;
        }
        cout<<"Case #"<<k+1<<": "<<i*N<<endl;

    }
    return 0;
}
