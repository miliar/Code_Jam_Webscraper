#include <iostream>
using namespace std;
int main()
{

    int t,n;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int count=0;
        int fr=0;
        cin>>n;
        char str[n+1];
        cin>>str;
        for(int j=0;j<=n;j++)
        {
            str[j]=str[j]-'0';

            if(count<=j)
                {
                fr+=j-count;
                count=j;
                }
                count+=str[j];

        }
        cout<<"Case #"<<i<<": "<<fr<<endl;

    }
    return 0;
}
