#include<iostream>
using namespace std;
int countdig(bool *a, int n)
{
    char dig[30];
    sprintf(dig,"%d%c",n,0);
    for(int i=0;i<strlen(dig);i++)
    {
        a[dig[i]-'0'] = 1;
    }
    
    for(int i=0;i<10;i++)
        if(a[i] == 0)
            return false;
    return true;
}
int main()
{
    int T;
    cin>>T;
    for(int tt=1;tt<=T;tt++)
    {
        int  i;
        cin>>i;
        if(i==0)
        {
            cout<<"Case #"<<tt<<": INSOMNIA"<<endl;
        }
        else
        {
            int x = i;
            bool *a = new bool[10];
            memset(a,0,10);
            for(int j=1;;j++)
            {
                if(countdig(a,x))
                {
                    break;
                }
                else
                    x = i*j;
            }
            cout<<"Case #"<<tt<<": "<<x<<endl;
        }
    }
    
}