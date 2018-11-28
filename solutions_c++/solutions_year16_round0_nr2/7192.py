#include <iostream>
#include <string.h>
#include <cstdio>
using namespace std;

int main()
{
    int t;
    scanf("%d",&t);
    for (int t1(1);t1<=t;t1++)
    {
       char a[101];char prev;
     scanf("%s",a);
       if (a[0]=='+')prev='+';
       else prev='-';
       int c(1);

       for (;c<strlen(a);c++)
       {
           if (a[c]!=prev)break;

        }

        int answer(0);
        if (prev=='-')answer++;
        int counter(0);prev='+';
        for (;c<strlen(a);c++)
        {
            if (a[c]==prev)counter++;
else {if (prev=='-')answer+=2;prev=a[c];counter=1;}
        }
        if (prev=='-')answer+=2;
        cout << "Case #"<<t1<<": " << answer << endl;
    }
    return 0;
}
