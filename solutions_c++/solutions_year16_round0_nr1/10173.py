#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
    int s,n,p;
    int t;
    bool combo[10],ok=false;
    FILE *f,*sortie;
    f = fopen("C:\\Users\\HCurti$\\Desktop\\A-large.in","r");
    sortie = fopen("C:\\Users\\HCurti$\\Desktop\\Output","w");
    fscanf(f,"%d",&t);

    //printf("%d\n",t);
    for(int i = 1;i<=t;i++){

        fscanf(f,"%d",&s);
        if(s==0){
            fprintf(sortie,"Case #%d: %s\n",i,"INSOMNIA");
        }else{


        for(int a=0;a<10;a++)combo[a]=false;
        ok=false;
        n=s;
        int k=1;
       //printf("boucle% d****************************%d***************************\n",i,s);
        while(!ok){

            s=n*k;
            p=s;
            k+=1;
           // printf("n=%d\t",s);
            int mod = s%10;
            if(mod<0)mod+=10;
        while(mod!=s){
            combo[mod]=true;
            //printf("%d\t",mod);
            s=s-mod;
            s/=10;

           //printf("s=%d\t",s);
            mod = s%10;
           if(mod<0)mod+=10;
        }
        combo[mod]=true;
        int j = 0;
        while(combo[j]){/*
             printf("\n%d\n",j);*/
            j++;
        }
        if(j>9){
            fprintf(sortie,"Case #%d: %d\n",i,p);

            //printf("\n%d\n",n);
            ok=true;


        }
        }
        }

    }

    fclose(f);
    fclose(sortie);
    return 0;
}

