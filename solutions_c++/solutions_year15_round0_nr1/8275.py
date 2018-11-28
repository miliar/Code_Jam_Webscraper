#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,Smax,current_number,extra,i,j;
    char inp[1005];
    cin >> T ;
    for(j=1;j<=T;j++)
    {
        current_number=extra=0;
        cin >> Smax >> inp;
        for(i=0;inp[i]!='\0';i++)
        {
            if(current_number<i)
            {
                extra+=i-current_number;
                current_number=i;
            }
            current_number+=(int)(inp[i]-'0');
        }

        printf("Case #%d: %d\n",j,extra);
    }
    return 0;
}
