#include <bits/stdc++.h>

using namespace std;

int main()
{
    FILE *in,*out;
    in=fopen("input.txt","r");
    out=fopen("output.txt","w");
    int t,i,j,s,k;
    char x[1002];
    fscanf(in,"%d",&t);
    for(int y=1;y<=t;y++)
    {
        fprintf(out,"Case #%d: ",y);
        x[0]='\0';
        fscanf(in,"%d%s",&s,x);
        j=0;
        k=0;
        //cout<<"x="<<x<<endl;
        for(i=0;i<=s;i++)
        {
            //cout<<k<<endl;
            if(k<i && x[i]!='0')
            {
                j+=(i-k);
                k+=(i-k);
            }
            k+=(x[i]-'0');
        }
        fprintf(out,"%d\n",j);
    }
    fclose(in);
    fclose(out);
    return 0;
}
