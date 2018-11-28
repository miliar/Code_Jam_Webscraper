#include<iostream>
#include<string.h>
#include<string>
using namespace std;
int main()
{

int cases,ans,length,k=0,i;
string s;
cin>>cases;

while(cases--)
{
    cin>>s;
    k++;
    i=0;length=0;
    ans = 0;
    do
    {
        if(s[i]=='\0') break;
        else length++,i++;
    }while(true);


    for(int i=length;i>=0;i--)
    {
        if((s[i]=='-')&&(ans%2==0))
        {
            ans++;
        }
        else if((s[i]=='+')&&(ans%2!=0))
        {
            ans++;
        }

    }
    cout<<"Case #"<<k<<": "<<ans<<endl;


}

return 0;
}
