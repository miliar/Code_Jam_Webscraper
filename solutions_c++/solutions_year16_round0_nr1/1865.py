#include <bits/stdc++.h>

using namespace std;

bool found[10];
char sNum[30];
int sumaCheck;
bool check(int num)
{
    
    sprintf(sNum,"%d",num);
    int len = strlen(sNum);
    for(int i=0;i<len;i++)
    {
        int digit =sNum[i]-'0';
        if(!found[digit])
        {
            found[digit]=true;
            sumaCheck++;
        }
    }
    return sumaCheck==10;
}

int main()
{
    int t;
    scanf("%d",&t);
    for(int caso=1;caso<=t;caso++)
    {
        
        int n;
        scanf("%d",&n);
        int finded=-1;
        printf("Case #%d: ",caso);
        if(n==0)
           finded=-1;
        else
        {
            memset(found,0,sizeof found);   
            sumaCheck=0;
            
            for(int i=1;i<20000;i++)
            {
                if(check(n*i))
                {
                    finded=n*i;
                    break;
                }
                
            }
        }
            
        finded==-1?printf("INSOMNIA\n"):printf("%d\n",finded);

        
    }
    return 0;
}