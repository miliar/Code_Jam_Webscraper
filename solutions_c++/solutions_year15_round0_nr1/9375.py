#include<iostream>
#include<cstring>

using namespace std;

int main()
{
    int t;
    cin>>t;
    int k=0;
    while(t--)
    {
        int n; cin>>n;
        char a[n+1];

        cin>>a;

        int c=0,curr=0;
        for(int i=0;i<=n;i++)
        {
            if(a[i]!='0')
            {
                if(curr<i)
                {
                 c+=i-curr;
                curr+=i-curr+a[i]-'0';
                }
                else
                    curr+=a[i]-'0';
            }

        }
        cout<<"Case #"<<++k<<": "<<c<<endl;

    }
}
