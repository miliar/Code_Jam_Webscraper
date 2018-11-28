#include <iostream>



using namespace std;


int main()
{
    int n;
    string s;
    int t;
    cin>>t;
    int total,req,temp;
    for(int j=1;j<=t;j++)
    {
        req=temp=0;
        cin>>n;
        cin>>s;
        for(int i=0;i<=n;i++)
        {
          //  cout<<i<<" "<<req<<" "<<temp<<endl;
            if(i <= req+temp)
            {
                req += (s[i]-'0');
            }
            else
            {
                temp += (i-req-temp);
                req +=(s[i]-'0');
            }
        }
        cout<<"Case #"<<j<<": "<<temp<<endl;
    }
    return 0;
}
