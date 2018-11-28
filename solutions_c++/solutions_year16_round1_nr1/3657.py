#include <iostream>
#include <string.h>
#include <cstring>
using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        string s;
        cin>>s;
        int l = s.length();
        char ans[l];
        int begin=0,end=0;
        ans[begin] = s[0];
        for(int i=1;i<l;i++)
        {
           if((int)(ans[begin]) > (int)(s[i]))
           {
               end++;
               ans[end] = s[i];
           } 
           else //append in beginning
           {
               end++;
               for(int i=end;i>begin;i--)
               {
                   ans[i] = ans[i-1];
               }
               ans[begin] = s[i];
           }
        }
        
        /*int ascii[l];
        for(int i=0;i<l;i++)
            ascii[i] = (int) s[i];
        for (int i = 0 ; i < ( l - 1 ); i++)
        {
            for (int j = 0 ; j < l - i - 1; j++)
            {
                if (ascii[j] < ascii[j+1]) /* For decreasing order use < */
          /*      {
                    int tempAscii = ascii[j];
                    ascii[j] = ascii[j+1];
                    ascii[j+1] = tempAscii;
                    
                    int tempStr = s[j];
                    s[j] = s[j+1];
                    s[j+1] = tempStr;
                }
            }
        }*/
        cout<<"Case #"<<t<<": ";
        for(int i=0;i<l;i++)
            cout<<ans[i];
        cout<<endl;
        
    }
}