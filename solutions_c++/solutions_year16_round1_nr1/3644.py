#include <iostream>
#include <string.h>
using namespace std;
long long int t;
int main()
{   ios_base::sync_with_stdio(false);
    cin>>t;
    int l;
    char s[1005],s2[1005],s3[1005];
    for(int k=0;k<t;k++)
    {l=1;
    cin>>s;
    s2[0]=s[0];
    s2[1]='\0';
    for(int i=1;i<strlen(s);i++)
    {
    if(s[i]>=s2[0])
    {
    s3[0]=s[i];
    s3[1]='\0';
    strcat(s3,s2);
    strcpy(s2,s3);

    }
    else{
    s3[0]=s[i];
    s3[1]='\0';
    strcat(s2,s3);

    }
    }
    cout<<"Case #"<<k+1<<": "<<s2<<endl;
    }
    return 0;
}
