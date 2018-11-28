#include<stdio.h>
FILE *read,*write;

void accept(int a[],int rowno)
{
    int i,j;
    for(i=1;i<=(rowno-1)*4;i++)
      fscanf(read,"%d",&j);

    fscanf(read,"%d %d%d%d",&a[0],&a[1],&a[2],&a[3]);

    for(i=0;i<(4-rowno)*4;i++) fscanf(read,"%d",&j);

}
int main()
{
    read=fopen("input.txt","r");
write=fopen("output.txt","w");
    int a[4],b[4],t,m,i,j,frow,srow,nomatches,item;

    fscanf(read,"%d",&t);

    m=t;
    while(m>0)
    {

        fscanf(read,"%d",&frow);
        accept(a,frow);
        fscanf(read,"%d",&srow);
        accept(b,srow);
        nomatches=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[i]==b[j])
                {

                   ++nomatches;
                   item=a[i];
                   if(nomatches>1) {fprintf(write,"Case #%d: Bad magician!\n",t-m+1);break;}
                }
            }
            if (nomatches>1) break;
        }
        if(nomatches==0)  fprintf(write,"Case #%d: Volunteer cheated!\n",t-m+1);
        else if(nomatches==1) fprintf(write,"Case #%d: %d\n",t-m+1,item);
        --m;
    }
 return 0;
}
