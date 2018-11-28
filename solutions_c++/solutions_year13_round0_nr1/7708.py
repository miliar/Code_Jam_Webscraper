#include<iostream>
#include<cstdio>
#include<cstring>
int main()
{
   FILE *fp,*fp1;
   int i,j,k,l,m,s1,s2,s3,s4,ts1,ts2;
   int sta[100];
   char st[6][6];
   fp1=fopen("f:\\codejam\\A-large.in","r");
   fp=fopen("f:\\codejam\\outputa.txt","w");
   fscanf(fp1,"%d",&k);
   for(l=1;l<=k;l++)
   {
      i=0;
      s1=0,s2=0,s3=0,s4=0;
      j=0;
      while(i<4) 
      {
         fscanf(fp1,"%s",&st[i]);
         i++;
      }
      for(i=0;i<4;i++)
      {
         sta[46]=0;
         sta[79]=0;
         sta[84]=0;
         sta[88]=0;
         for(j=0;j<4;j++) sta[st[i][j]]++;
         if(sta[46]>0) s1=1;
         else if(sta[79]+sta[84]==4) s2++;
         else if(sta[88]+sta[84]==4) s3++;
      }
      for(j=0;j<4;j++)
      {
         sta[46]=0;
         sta[79]=0;
         sta[84]=0;
         sta[88]=0;
         for(i=0;i<4;i++) sta[st[i][j]]++;
         if(sta[46]>0) s1=1;
         else if(sta[79]+sta[84]==4) s2++;
         else if(sta[88]+sta[84]==4) s3++;
      }
      sta[46]=0;
      sta[79]=0;
      sta[84]=0;
      sta[88]=0;
      for(i=0;i<4;i++) sta[st[i][i]]++;
      if(sta[46]>0) s1=1;
      else if(sta[79]+sta[84]==4) s2++;
      else if(sta[88]+sta[84]==4) s3++;
      sta[46]=0;
      sta[79]=0;
      sta[84]=0;
      sta[88]=0;
      for(i=0;i<4;i++) sta[st[i][3-i]]++;
      if(sta[46]>0) s1=1;
      else if(sta[79]+sta[84]==4) s2++;
      else if(sta[88]+sta[84]==4) s3++;
      if(s1>0&&s2==0&&s3==0) fprintf(fp,"Case #%d: Game has not completed\n",l);
      else if(s1==0&&s2==0&&s3==0) fprintf(fp,"Case #%d: Draw\n",l);
      else if(s3>0) fprintf(fp,"Case #%d: X won\n",l);
      else fprintf(fp,"Case #%d: O won\n",l);
   }
    fclose(fp); 
   fclose(fp1);
   return 0;
}
