#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
    int t,i,j,current,n,ans;
    char a[10000];
    FILE *fp,*fi;
    //fi = fopen("A-large.in","r");
    //fp = fopen("p1bans.txt","w");
    fscanf(stdin,"%i",&t);
    for(j=0;j<t;j++)
    {
        fscanf(stdin,"%i",&n);
        current = ans = 0;
        fgetc(stdin);
        fscanf(stdin,"%s",a);
        for(i=0;i<=n;i++)
        {
            if(current>=i)
            {
                current+=(a[i]-48);
            }
            else if(a[i]!=48)
            {
            ans+= (i-current);
            current+=(i-current);
            current +=(a[i]-48);
            }
        }
        fprintf(stdout,"Case #%i: %i\n",j+1,ans);
    }
    fclose(fp);
    fclose(fi);
    return 0;
}
