#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>

using namespace std;

int main()
{
    int a;
    scanf("%d",&a);
    for(int i=0;i<a;i++)
    {
        int b, cou=0, cou2=0;
        string s;
        char c;
        scanf("%d",&b);
        getline(cin, s);
        //cout << s << " " << s.length() << endl;
        for(int j=1;j<s.length();j++)
        {
            //cout << "cou: " << cou << endl;
            if((j>1)&&(s[j]!='0'))
            {
                if(cou<j-1)
                {
                    cou2+=(j-1)-cou;
                    cou+=cou2;
                }
            }
            if(s[j]=='1') cou++;
            else if(s[j]=='2') cou+=2;
            else if(s[j]=='3') cou+=3;
            else if(s[j]=='4') cou+=4;
            else if(s[j]=='5') cou+=5;
            else if(s[j]=='6') cou+=6;
            else if(s[j]=='7') cou+=7;
            else if(s[j]=='8') cou+=8;
            else if(s[j]=='9') cou+=9;

        }
        printf("Case #%d: %d\n",i+1,cou2);
    }

    return 0;
}
