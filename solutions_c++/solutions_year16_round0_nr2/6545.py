#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;
int main()
{
    FILE *fp;
    int t,tc=1,l,i,j,ans;
    char s[101],tmp[1000],temp[100]="Case #",com[100];
    cin>>t;
    fp=fopen("out.txt","a");
    while(t--)
    {
        ans=0;
        cin>>s;
        l=strlen(s);
        for(i=l-1;i>=0;i--)
        {
            if(s[i]=='-')
            {
                ans++;
                for(j=i;j>=0;j--)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }
        }
        strcpy(com,temp);
        itoa(tc,tmp,10);
        strcat(com,tmp);
        itoa(ans,tmp,10);
        strcat(com,": ");
        strcat(com,tmp);
        strcat(com,"\n");
        fprintf(fp,com);
        cout<<"Case #"<<tc<<": "<<ans<<endl;
        tc++;
    }
    fclose(fp);
    return 0;
}
