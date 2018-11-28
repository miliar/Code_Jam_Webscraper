#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int check0(char p[] , int i , int j)
{
    for( ; i<=j ; i++)
        if(p[i]=='+')
            return 0;
    return 1;        
}

void rev(char q[] , int start , int end)
{
    char temp;
    if( (end-start+1)%2 )
    {
        for( ; end>=start ; )
        {
            temp=q[end];
            if(q[start]=='+')
                q[end]='-';
            else
                q[end]='+';
            if(temp=='+')    
                q[start]='-';
            else
                q[start]='+';
            start++;end--;
        }
    }
    else
    {
       for( ; end>start ; )
        {
            temp=q[end];
            if(q[start]=='+')
                q[end]='-';
            else
                q[end]='+';
            if(temp=='+')    
                q[start]='-';
            else
                q[start]='+';
            start++;end--;
        } 
    }
}

int main()
{
    int t,count,check,i,j,k=1,start,n;
    char s[101];
    scanf("%d\n",&t);
    while(k<=t)
    {
        scanf("%s",s);
        count=0;
        n=strlen(s);
        start=0;
        for(i=n-1 ; i>=0 ; )
        {
           // printf("1.i=%d and s=%s\n",i,s);
            if(s[i]=='+')
            {
                while(s[i]=='+' && i>=0)
                    i--;
            }
            else
            {
                j=start;
                if( check0(s,j,i)==1  )
                {
             //       printf("ch1=%s j=%d i=%d\n",s,j,i);
                    check=1;
                    count++;
                    break;
                }
                j=start;
                
                if(s[j]=='+')
                {
                    while(s[j]=='+' && j<=i)
                    {
                        s[j]='-';
                        j++;
                    }
                    count++;
                }
            
                rev(s,0,i);
                count++;
                if(check0(s,0,i)==1)
                {
                //    printf("ch2=%s j=%d i=%d\n",s,j,i);
                    check=1;
                    count++;
                    break;
                }
                i=i-j;
               // printf("2.i=%d and s=%s\n",i,s);
            }
        }
        
        printf("Case #%d: %d\n",k,count);
        
        k++;
    }
    return 0;
}
