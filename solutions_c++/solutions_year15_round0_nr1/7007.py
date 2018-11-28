#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
    long long int t, no=0, ex=0, i, j, l=0;
    char s[1005];
    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>l>>s;
        ex=no=0;
        for(j=0;j<=l;j++)
        {
            if(j>no)
            {
                ex+=j-no;
                no+=j-no;
            }
            no+=s[j]-'0';
        }
        cout<<"Case #"<<i+1<<": "<<ex<<endl;
    }
}
