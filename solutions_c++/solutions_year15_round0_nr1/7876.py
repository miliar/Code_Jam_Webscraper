#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);
    int T;
    cin>>T;
    for (int t=1; t<=T; t++)
    {
        int Sm;
        cin>>Sm;
        int standing=0, added=0;
        for (int i=0; i<=Sm; i++)
        {
            char in;
            cin>>in;
            int value = in-'0';
            if (standing<i)
            {
                added+=i-standing;
                standing+=i-standing;
            }
            standing+=value;
        }
        cout<<"Case #"<<t<<": "<<added<<endl;
    }
}
