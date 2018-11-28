#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    char inputstr[100];

    int T,k;
    int count=0;

    cin>>T;

    int outputArray[T];

    for(k=0; k<T; k++)
    {
        cin>>inputstr;

        for(int i=strlen(inputstr);i>=0; i--)
        {
            if(inputstr[i]=='-')
            {
                count++;
                for(int j=strlen(inputstr);j>=0;j--)
                {
                    if(inputstr[j]=='-')
                        inputstr[j]='+';
                    else
                        inputstr[j]='-';

                }

            }
        }

        outputArray[k] = count;
        count=0;
    }

    for(k=0; k<T; k++)
        cout<<"Case #"<<k+1<<": "<<outputArray[k]<<endl;
    return 0;
}
