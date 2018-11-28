//revenge of the pancakes
#include<iostream>
#include<stdio.h>
#include<string.h>
int main()
{
    using namespace std;

    int t,i,j,k;
    char s[100][101],org;
    cin>>t;

    for(i=0;i<t;i++)
        scanf("%s",s[i]);

    i=0;
    j=0;
    int flag=0;
    while(i<t)
    {   org=s[i][0];
        flag=0;



        while(j<(strlen(s[i])-1))
        {
        for(j=0;s[i][j]==org;j++);

        for(k=0;k<j;k++)
        {
            if(j==strlen(s[i])&&org=='+')
                break;
            else
            {
            if(s[i][j]=='+')
                s[i][k]='+';
            else
                s[i][k]='-';
            }
        }

        if(j!=strlen(s[i]))
        {k=0;
         org=s[i][k];
         flag++;
        }
        }

        if(s[i][0]=='-')
            flag++;
        cout<<"Case #"<<i+1<<": ";
        cout<<flag<<"\n";
        j=0;
        i++;
    }
    return 0;
}
