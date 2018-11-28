#include<iostream>
using namespace std;
int main()
{
        int t;
        cin>>t;
        int i=1;
        while(t--)
        {
                cout<<"Case #"<<i<<": ";
                int a,b,c;
                cin>>a>>b>>c;
                for(int j=1;j<=a;j++)
                        cout<<j<<" ";
                cout<<endl;
                i++;
        }
        return 0;
}
