#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    char str[100];

    int T,k;
    int count=0;
    cout<<"helloamit";
    cin>>T;

    int outputArr[T];

    for(k=0; k<T; k++)
    {
        cin>>str;

        for(int i=strlen(str);i>=0; i--)
        {
            if(str[i]=='-')
            {
                count++;
                for(int j=strlen(str);j>=0;j--)
                {
                    if(str[j]=='-')
                        str[j]='+';
                    else
                        str[j]='-';

                }

            }
        }

        outputArr[k] = count;
        count=0;
    }

    for(k=0; k<T; k++)
        cout<<"Case #"<<k+1<<":"<<outputArr[k]<<endl;
    return 0;
}
