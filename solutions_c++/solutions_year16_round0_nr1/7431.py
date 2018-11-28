#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("codejam.txt","w",stdout);
    int tc,i=1;
    cin>>tc;
    while(tc--)
    {
        unsigned long long x;
        cin>>x;
        bool arr[10]= {0};
        cout<<"Case #"<<i<<": ";
        if(x==0)
            cout<<"INSOMNIA"<<endl;
        else
        {
            unsigned long long num,ans;
            for(int j=1; j<=100000000; j++)
            {
                if(arr[0] && arr[1] && arr[2] && arr[3] && arr[4] && arr[5] && arr[6] && arr[7] && arr[8] && arr[9])
                    break;
                else
                {
                    num=x*j;
                    ans=num;
                    while(num)
                    {
                        arr[num%10]=1;
                        num/=10;
                    }
                }
                }
                cout<<ans<<endl;
        }
        i++;
    }
    fclose(stdout);
    return 0;
}
