#include <iostream>
#include <stdio.h>
#include <string.h>
#include <fstream>
using namespace std;

int main()
{
    //cout << "Hello world!" << endl;
    char s[1001],p[10001];
    int t,l,i,j,k,m;
    fstream f2,f1;
    f2.open("input.txt",ios::in);
    f1.open("output.txt",ios::out);
    cin>>t;
    //f2>>t;
    m=1;
    char c[1001],f[2];
    while(m<=t)
    {
        scanf("%s",s);
       //f2>>s;
        l=strlen(s);
        p[0]=s[0];
        p[1]='\0';
                for(i=1;i<l;i++)
        {
            j = int(s[i]);
            k= int(p[0]);
            if(j>=k)
            {
                strcpy(c,"");
                f[0]=s[i];
                f[1]='\0';
                strcpy(c,f);
                strcat(c,p);
                strcpy(p,c);
            }
            else
            {
                f[0]=s[i];
                f[1]='\0';
                strcat(p,f);
            }
        }
       cout<<"Case #"<<m<<": "<<p<<"\n";
        //f1<<"Case #"<<m<<": "<<p<<"\n";
        m++;
    }
    return 0;
}
