#include<iostream>
#include<cstdio>
int main()
{
   FILE *fp,*fpw;
   int sel1[5],sel2[5],in[5],i,j,k,l,n,m,ans;
   fp=fopen("input.txt","r");
   fpw=fopen("output.txt","w");
   fscanf(fp,"%d",&m);
   for(i=1;i<=m;i++)
   {
		l=0;
      ans=0;
      for(j=1;j<=2;j++)
      {
         fscanf(fp,"%d",&n);
         for(k=1;k<=4;k++)
         {
            fscanf(fp,"%d%d%d%d",&in[0],&in[1],&in[2],&in[3]);
            if(k==n&&j==1) sel1[0]=in[0],sel1[1]=in[1],sel1[2]=in[2],sel1[3]=in[3];
            if(k==n&&j==2) sel2[0]=in[0],sel2[1]=in[1],sel2[2]=in[2],sel2[3]=in[3];
         }
      }
      for(j=0;j<4;j++)
      {
         for(k=0;k<4;k++)
         {
            if(sel1[j]==sel2[k])
            {
               l++;
               ans=sel1[j];
               break;
            }  
         }
      }
      if(l<1) fprintf(fpw,"Case #%d: Volunteer cheated!\n",i);
      else if(l>1) fprintf(fpw,"Case #%d: Bad magician!\n",i);
      else fprintf(fpw,"Case #%d: %d\n",i,ans);
   }
   
}
