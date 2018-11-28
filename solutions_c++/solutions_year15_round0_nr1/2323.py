#include <iostream>
using namespace std;

int main()
{   
    int t,k=1;
    cin>>t;
    while(t--)
    {
        int n,i,count=0;
        cin>>n;
        char str[1050];
        cin>>str;
        int s=str[0]-'0';
        for(i=1;i<=n;i++)
        {
            if(i>s)
            {
                count+=i-s;
                s=s+(i-s);
                
            }
            s=s+(str[i]-'0');
            
        }
            
        cout<<"Case #"<<k++<<": ";
        cout<<count<<endl;
       
    }
    return 0;
}