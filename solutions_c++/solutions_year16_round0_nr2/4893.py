#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
int main()
{
    //FILE *f=freopen("test.in","rt",stdin);
    //FILE *f1=freopen("test.ou","wt",stdout);
    int t;
    cin>>t;
    for (int c=0;c<t;c++)
    {
        char s[101];
        int cou=0;
        cin>>s;
        for (int i=1;i<strlen(s);i++)
            if (s[i]!=s[i-1]) cou++;
        if (s[strlen(s)-1]=='-') cou++;
        cout<<"Case #"<<c+1<<": "<<cou<<endl;
    }
    return 0;
}
