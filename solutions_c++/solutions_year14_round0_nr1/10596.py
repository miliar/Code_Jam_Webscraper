#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    FILE *infile;
    infile = fopen("output.txt", "w");
    int t,n,i,j,f[20][20],m,s[20][20],ans,count1[20],count2[20],f1;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        for(i=1;i<=16;i++)
        {
            count1[i]=0;
            count2[i]=0;
        }
        f1=0;
        cin>>n;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>f[i][j];
            }
        }
         cin>>m;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>s[i][j];
            }
        }

            for(j=1;j<=4;j++)
            {
               count1[f[n][j]]++;
               count2[s[m][j]]++;
            }
            for(i=1;i<=16;i++)
            {
                if(count1[i]==1&&count2[i]==1)
                {
                    f1++;
                    ans=i;
                }
            }

            if(f1==0)
                fprintf(infile,"Case #%d: Volunteer cheated!\n",k);
            else if(f1>1)
            fprintf(infile,"Case #%d: Bad magician!\n",k);
            else
                fprintf(infile,"Case #%d: %d\n",k,ans);

        /*if(f1==0)
            cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
        else if(f1>1)
            cout<<"Case #"<<k<<": Bad magician!"<<endl;
        else
            cout<<"Case #"<<k<<": "<<ans<<endl;*/
    }
     fclose(infile);
}
