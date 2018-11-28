#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;
#define debug //printf

struct ataque{
       int dia,x,y,f;
       ataque(){}
       ataque(int dia,int x,int y,int f): dia(dia),x(x),y(y),f(f){}
       bool operator<(ataque comp)const{
            return dia<comp.dia;}}

v[110];
int muro[2020];
int update[2020];
int resp;


void atualiza(){
     for(int i=0;i<2000;i++)
             muro[i]=max(muro[i],update[i]);}

void processa(int idx){
     
     int ok=1;
     
     for(int i=v[idx].x;i<v[idx].y;i++){
             
             
             if(muro[i] < v[idx].f){
                        ok = 0;
                        update[i] = max(update[i],v[idx].f);}
             
             }
     debug("atq dia %d %d-%d f=%d ok=%d\n",v[idx].dia,v[idx].x,v[idx].y,v[idx].f,ok);
     if(!ok)resp++;
     }

main(){
       
       int te;
       scanf("%d",&te);
       
       for(int t=1;t<=te;t++){
               
               int qnt=0;
               memset(muro,0,sizeof(muro));
               memset(update,0,sizeof(update));
               int n;
               scanf("%d",&n);
               resp=0;
               
               for(int i=0;i<n;i++){
                       
                       int di,k,xi,yi,fi,dt,dx,df;
                       scanf("%d%d%d%d%d%d%d%d",&di,&k,&xi,&yi,&fi,&dt,&dx,&df);
                       xi+=500;
                       yi+=500;
                       
                       for(int j=0;j<k;j++){
                               
                               v[qnt++] = ataque(di+j*dt,xi+j*dx,yi+j*dx,fi+j*df);
                               debug("c: d=%d x=%d y=%d f=%d\n",di+j*dt,xi+j*dx,yi+j*dx,fi+j*df);
                               }
                       
                       
                       
                       }
               sort(v,v+qnt);
               
               processa(0);
               
               for(int i=1;i<qnt;i++){
                       
                       if(v[i].dia != v[i-1].dia)atualiza();
                       processa(i);
                       
                       
                       
                       }
               
               
               printf("Case #%d: %d\n",t,resp);
               }}
