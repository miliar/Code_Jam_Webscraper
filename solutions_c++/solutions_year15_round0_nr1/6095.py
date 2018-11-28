#include<stdio.h>

int main(){
    FILE *fin,*fout;
fin= fopen("A-large.in","r");
fout= fopen("output.txt","w");
long long smax,cas=0,a[1010],t,i,csum,added;
char c;
fscanf(fin,"%lld",&t);

while(t--){
    fscanf(fin,"%lld",&smax);
    fgetc(fin);

    for(i=0;i<=smax;i++){
        c=fgetc(fin);
        a[i]=c-48;
    }

    csum=added=0;
    for(i=1;i<=smax;i++){
    csum+=a[i-1];
    if(csum<i){
        csum++; added++;
    }
    }
    fprintf(fout,"Case #%lld: %lld\n",++cas,added);
}
fclose(fin);
fclose(fout);
}
