#include<iostream>
using namespace std;
char resetTarget(char t)
{
    if(t == '+')
    {
        t='-';
    }
    else
    {
        t='+';
    }
    
    return t;
}
int main()
{
    int T;
    cin>>T;
    for(int tt=1;tt<=T;tt++)
    {
        char * a = new char[100];
        memset(a,0,100);
        scanf("%s",a);
        
        int last = strlen(a);
        char target = '+';
        int ans = 0;
        for(int i=last-1;i>=0;i-- )
        {
            if( a[i] != target)
            {
                ans++;
                target = resetTarget(target);
            }
                
        }
        free(a);
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
    
}