#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>

using namespace std;

int main()
{
    int t;
    scanf("%d\n", &t);
    
    for (int ii = 1; ii <= t; ii++)
    {
        char str[110]={0};
        cout<<"Case #"<<ii<<": ";
        scanf("%s\n",str);
        int l = strlen(str);
        int ch = 0;
        for (int i = 1; i<l; i++)
        {
            if(str[i-1]!=str[i])
                  ch++;
        }
        if(str[l-1]=='-')
            ch++;
        cout<<ch<<endl;
    }
}