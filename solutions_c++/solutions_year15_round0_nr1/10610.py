#include<iostream>
using namespace std;
int main()
{
    long long int t,s,c;
    string s2;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        c=0;
        cin>>s;
        cin>>s2;
        long long int po=s2[0]-48;
        for(int k=1;k<s2.length();k++)
        {
            while(po<k)
            {
                po++;
                c++;
            }
            po=po+(s2[k]-48);
        }
        cout<<"Case #"<<i<<": "<<c<<endl;

    }

    return 0;
}
