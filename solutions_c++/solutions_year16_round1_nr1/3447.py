#include<iostream>
#include<string>
using namespace std;

int main()
{
    int cases,k=0,j=0,length;
    string str,ans;
    cin>>cases;

    while(cases--)
    {

        cin>>str;
        j++;
        ans = str[0];


        for(int i=1;;i++)
        {
            if(str[i]=='\0')
            {
                break;
            }

            if(str[i]>=ans[0])
            {
               ans = str[i] + ans;
            }
            else
            {
                ans = ans + str[i];
            }
        }

        cout<<"Case #"<<j<<": "<<ans<<endl;
    }


    return 0;
}
