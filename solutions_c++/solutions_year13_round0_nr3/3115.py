#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <fstream>
#include <cmath>

using namespace std;

bool re(int a)
{
    int ac[105];
    for(int gg=0;gg<105;gg++) ac[gg]=-1;
    int flag=0;
    for(int c=104;c>=0;c--)
    {
        ac[c]=a%10;
        a=a/10;
        
        if(a==0)
        {
            flag=c;
            break;
        }
    }
    for(int s=flag;s<=(flag+104)/2;s++)
    {
        if(ac[s]!=ac[104-s+flag]) return false;
    }
    return true;
}
    
int main()
{
    ifstream in("input3.txt");
    ofstream out("output3.txt");
    int po=0;
    in>>po;
    for(int co=0;co<po;co++)
    {
        int m,n,ans=0;
        in>>m>>n;
        for(int a=m;a<=n;a++)
        {
            if(re(a))
            {
                if((double)sqrt(a)-(int)(sqrt(a)/1)==0)
                {
                    if(re((int)sqrt(a))) ans++;
                }
            }
        }
        out<<"Case #"<<co+1<<": "<<ans<<endl;
    }
}
                
        
    
