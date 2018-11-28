#include<cstdio>
#include<fstream>
#include<algorithm>
using namespace std;
int main()
{
    int t,x,n,i,j,y,z,lk,sk,ln,sn;
    double na[1001],k[1001];
    bool arr[1001];
    ifstream ifile;
    ifile.open("D-large.in");
    FILE * pf = fopen("ans.txt","w");
    ifile>>t;
    for(x=1;x<=t;x++)
    {
        ifile>>n;

        for(i=0;i<n;i++)
        {
            //fscanf(sf,"%lf",&na[i]);
            ifile>>na[i];
            //printf("%lf ",na[i]);
        }
       // printf("\n");
        for(i=0;i<n;i++)
        {
            //fscanf(sf,"%lf",&k[i]);
            ifile>>k[i];
        }
        //printf("\n");
        sort(na,na+n);
        sort(k,k+n);
        sn=0;
        z=n;
        lk=0;
        while(lk<n)
        {
            while(k[lk]<na[sn]&&lk<n)lk++;
            if(lk<n)z--;
            lk++;
            sn++;
        }
        y=n;
        sn=0;
        lk=n-1;
        sk=0;
        while(lk>sk&&lk>=0&&sk<n&&sn<n)
        {
            if(na[sn]>k[sk])
            {
                sn++;
                sk++;
            }
            else
            {
                lk--;
                sn++;
                y--;
            }
        }
        if(na[sn]<k[sk]&&sk<n&&sn<n&&lk==sk)y--;
        fprintf(pf,"Case #%d: %d %d\n",x,y,z);
        //printf("Case #%d: %d %d\n",x,y,z);
    }
//    fclose(sf);
    fclose(pf);
}
