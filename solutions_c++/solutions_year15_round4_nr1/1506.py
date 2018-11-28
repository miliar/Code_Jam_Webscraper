#include<stdio.h>
#include<string>
#include<list>

char f[10001];
char fnd[10001];

int main(int agrc,char*argv[]){
  int T;scanf("%d",&T);
  for(int tc=1;tc<=T;tc++){
    int R,C;scanf("%d%d",&R,&C);
    printf("Case #%d: ",tc);
    for(int i=0;i<R*C;i++) scanf(" %c",&f[i]);
    for(int i=0;i<R*C;i++) fnd[i]=0;
    int mxc=0;
    int s;
    for(int i=0;i<R*C;i++){
      switch(f[i]){
        case '.': break;
        case '^': s=i-C; while(s>=0 && f[s]=='.'){ s-=C;} fnd[i]=(s>=0 && f[s]!='.')?1:2; break;
        case 'v': s=i+C; while(s<R*C && f[s]=='.'){ s+=C;} fnd[i]=(s<R*C && f[s]!='.')?1:2; break;
        case '>': s=i+1; while(s%C!=0 && f[s]=='.'){ s+=1;} fnd[i]=(s%C!=0 && f[s]!='.')?1:2; break;
        case '<': s=i-1; while((s+1)%C!=0 && f[s]=='.'){ s-=1;} fnd[i]=((s+1)%C!=0 && f[s]!='.')?1:2; break;      
      }
    }
    bool ps=true;/*
    printf("\n");
    for(int i=0;i<R;i++){
      for(int k=0;k<C;k++) printf("%d",fnd[i*C+k]);
      printf("\n");
    }
    printf("\n");*/
    for(int i=0;i<R*C && ps;i++) if(fnd[i]==2){
        s=i-C; while(s>=0 && f[s]=='.'){ s-=C;}         if(s>=0 && f[s]!='.'){ mxc++; continue;}
        s=i+C; while(s<R*C && f[s]=='.'){ s+=C;}        if(s<R*C&& f[s]!='.'){ mxc++; continue; }
        s=i+1; while(s%C!=0 && f[s]=='.'){ s+=1;}       if(s%C!=0&& f[s]!='.'){ mxc++; continue; }
        s=i-1; while((s+1)%C!=0 && f[s]=='.'){ s-=1;}   if((s+1)%C!=0 && f[s]!='.'){ mxc++; continue; }
        ps=false;
    }
    if(ps){
      printf("%d\n",mxc);
    }else{
      printf("IMPOSSIBLE\n");
    }
  }
  return 0;
}
