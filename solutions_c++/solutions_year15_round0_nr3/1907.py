#include<stdio.h>

int ch[10000];

int mult[8*8]; //1,i,j,k, -(1,i,j,k)  //res=8*f+s;
void inimult(){
  for(int s=0;s<4;s++){
    mult[s*8+s]=4;
    mult[s*8]=s;
    mult[s]=s;
  }
  mult[1*8+2]=3;mult[2*8+1]=3+4;
  mult[1*8+3]=6;mult[3*8+1]=2;
  mult[2*8+3]=1;mult[3*8+2]=5;
  for(int i=0;i<4;i++)
    for(int j=0;j<4;j++){
      mult[(i+4)*8+j]=(mult[i*8+j]+4)&7;
      mult[(i+4)*8+j+4]=mult[i*8+j];
      mult[i*8+j+4]=(mult[i*8+j]+4)&7;
    }
}

/*
void printqt(int q){
  if(q>=4)
    printf("-");
  switch((q&3)){
    case 0: printf("1"); break;
    case 1: printf("i"); break;
    case 2: printf("j"); break;
    case 3: printf("k"); break;
  }
}*/


int L,X;
bool splitable(){
  int prod=0;
  for(int i=0;i<L;i++)
    prod=mult[prod*8+ch[i]];
  int prodg=0;
  for(int i=0;i<(X&3);i++)
    prodg=mult[prodg*8+prod];
  if(prodg!=4) return false; //ijk==-1 <-> 4
  int pos=0;
  prod=0;
  while(pos<=4*L+2 && pos<L*X && prod!=1) // i <-> 1
    prod=mult[prod*8+ch[(pos++)%L]];
  if(prod!=1) return false;
  int posa=pos-1;
  prod=0;
  while(pos-posa<=4*L+2 && pos<L*X && prod!=2) // j <-> 2
    prod=mult[prod*8+ch[(pos++)%L]];
  if(prod!=2) return false;
  return (pos<L*X);
}

int main(int agrc,char*agrv[]){
  inimult();
  int T;scanf("%d",&T);
  for(int tc=1;tc<=T;tc++){
    scanf("%d%d",&L,&X);
    for(int i=0;i<L;i++){
      char c;scanf(" %c",&c);
      ch[i]=c-104;
    }
    printf("Case #%d: ",tc);
    printf((splitable()?"YES\n":"NO\n"));
  }
  return 0;
}
