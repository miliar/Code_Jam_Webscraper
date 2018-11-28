#include<iostream>
#include<set>
#include<algorithm>
using namespace std;

int main()
{
    int i,j,k,z,x,y;
    int test,N;
    cin>>test;
    int ind=0;
    while(test--)
    {
        ind++;
        set<int> cnt;
        cin>>N;

        if(N==0)
        {
            cout<<"Case #"<<ind<<": INSOMNIA"<<endl;
            continue;
        }

        long long int temp=N;

        i=1;
        while(cnt.size()!=10)
        {
            temp=N*i;
            i++;
            while(temp>0)
            {
                cnt.insert(temp%10);
                temp=temp/10;
            }
        }

        long long int ans=N*(i-1);
        cout<<"Case #"<<ind<<": "<<ans<<endl;

    }
}
