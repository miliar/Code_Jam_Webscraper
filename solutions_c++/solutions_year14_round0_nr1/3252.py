#include<cstdio>
#include<fstream.h>
using namespace std;
int main()
{
    int a,i,j,t,ans,tt,c;
    bool ar[16],br[16];
    ifstream ifile;
    ifile.open("A-small-attempt1.in");
    //scanf("%d",&t);
    ifile>>t;
    FILE * pf= fopen("ans.txt","w");
    for(tt=0;tt<t;tt++)
    {
        for(i=0;i<16;i++)
        {
            ar[i]=false;
            br[i]=false;
        }
        //scanf("%d",&ans);
        ifile>>ans;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                //scanf("%d",&a);
                ifile>>a;
                if(ans==i+1)ar[a-1]=true;
            }
        }
        //scanf("%d",&ans);
        ifile>>ans;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                //scanf("%d",&a);
                ifile>>a;
                if(ans==i+1)
                {
                    if(ar[a-1])
                    {
                        br[a-1]=true;
                    }
                }
            }
        }
        c=0;
        for(i=0;i<16;i++)
        {
            if(br[i])
            {
                c++;
                ans=i;
            }
        }
        if(c==1)fprintf(pf,"Case #%d: %d\n",tt+1,ans+1);
        else if(c==0)fprintf(pf,"Case #%d: Volunteer cheated!\n",tt+1);
        else fprintf(pf,"Case #%d: Bad magician!\n",tt+1);
    }
    ifile.close();
    fclose(pf);
}
