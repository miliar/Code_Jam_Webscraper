#include<stdio.h>

int main()
{
    int kartu1[4][4],kartu2[4][4],baris,kolom,kolomBanding;
    int pilih1,pilih2;
    int kasus,hasil,nilai;
    
    scanf("%i",&kasus);
    while(kasus--)
    {
         printf("Case #%i: ",100-kasus);
         hasil=0;
         scanf("%i",&pilih1);
         for(baris=0;baris<4;baris++)
         {
              for(kolom=0;kolom<4;kolom++)
              {
                    scanf("%i",&kartu1[baris][kolom]);
              }
         }
         scanf("%i",&pilih2);
         for(baris=0;baris<4;baris++)
         {
              for(kolom=0;kolom<4;kolom++)
              {
                    scanf("%i",&kartu2[baris][kolom]);
              }
         }
         
         for(kolom=0;kolom<4;kolom++)
         {
              for(kolomBanding=0;kolomBanding<4;kolomBanding++)
              {
                   if(kartu1[pilih1-1][kolom]==kartu2[pilih2-1][kolomBanding]) {hasil=hasil+1; nilai=kartu1[pilih1-1][kolom];}                      
              }
         }
         if(hasil==0) printf("Volunteer cheated!\n");
         else if(hasil==1) printf("%i\n",nilai);
         else printf("Bad magician!\n");
    }
}
