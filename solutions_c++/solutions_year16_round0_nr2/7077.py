#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
int main() 
{
    int tc,i,j,k;
    char a[105];
    cin>>tc;
    k=1;
    while(tc--)
    {
        int count=0;
        cin>>a;
        i=0;
        while(i<strlen(a)-1)
        {
                if(a[i]==a[i+1])
                    {
                        i++;
                    }
                else
                    {
                        count++;
                        i++;
                    }
        }
        if(a[strlen(a)-1]=='-')
        count++;
        printf("Case #%d: %d\n",k,count);
        k++;
    }
	return 0;
}
