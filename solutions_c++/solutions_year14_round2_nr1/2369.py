#include<cstdio>
#include<fstream>
#include<cstring>
#include<cstdlib>
using namespace std;
int main()
{
    ifstream ifile;
    ifile.open("A-small-attempt2.in");
    FILE * pf = fopen("ans.txt","w");
    int t,n,i,j,num[100][100],k,l,m,s,avg,sa,sm,saa,x;
    char a[100][100],b[100][100];
    bool var;
    ifile>>t;
    for(x=1;x<=t;x++)
    {
        var=true;
        ifile>>n;
        for(i=0;i<n;++i)
        {
            ifile>>a[i];
            m=0;
            k=0;
            j=0;
            l=strlen(a[i]);
            while(j<l)
            {
                b[i][k]=a[i][m];
                num[i][k]=0;
                while(a[i][j]==a[i][m])
                {
                    ++j;
                    ++num[i][k];
                }
                m=j;
                ++k;
            }
            b[i][k]='\0';
            for(j=0;j<i;++j)
            {
                if(strcmp(b[i],b[j])!=0)
                {
                    var=false;
                    j=n;
                    i=n;
                }
            }
        }
            //for(j=0;j<n;++j)printf("%s\n",b[j]);
        if(!var)
        {
            fprintf(pf,"Case #%d: Fegla Won\n",x);
            printf("Case #%d: Fegla Won\n",x);
        }

        else
        {
            for(i=0;i<k;++i)
            {
                s=0;
                for(j=0;j<n;++j)
                {
                    s+=num[j][i];
                }
                avg=s/n;
                sa=0;
                sm=0;
                for(j=0;j<n;++j)
                {
                    saa=num[j][i]-avg;
                    if(saa<0)saa=-1*saa;
                    sa+=saa;
                    saa=num[j][i]-avg-1;
                    if(saa<0)saa=-1*saa;
                    sm+=saa;
                }
                if(sm<sa)num[0][i]=sm;
                else num[0][i]=sa;
            }
            saa=0;
            for(i=0;i<k;i++)saa+=num[0][i];
            fprintf(pf,"Case #%d: %d\n",x,saa);
            printf("Case #%d: %d\n",x,saa);
        }
    }
    fclose(pf);
}
