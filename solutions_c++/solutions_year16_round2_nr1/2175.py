#include<stdio.h>
#include<string.h>
#include<map>
using namespace std;
map<char,int> m;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large1.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        char name[2002];
        scanf("%s",name);
        for(int j=0;j<strlen(name);j++){
            m[name[j]]++;
        }
        int a[10]={0};
        if(m['Z']>0){
            a[0]+=m['Z'];
            m['E']-=m['Z'];
            m['R']-=m['Z'];
            m['O']-=m['Z'];
            m['Z']=0;
        }
        if(m['W']>0){
            a[2]+=m['W'];
            m['T']-=m['W'];
            m['O']-=m['W'];
            m['W']=0;
        }
        if(m['U']>0){
            a[4]+=m['U'];
            m['F']-=m['U'];
            m['O']-=m['U'];
            m['R']-=m['U'];
            m['U']=0;
        }
        if(m['X']>0){
            a[6]+=m['X'];
            m['S']-=m['X'];
            m['I']-=m['X'];
            m['X']=0;
        }
        if(m['G']>0){
            a[8]+=m['G'];
            m['E']-=m['G'];
            m['I']-=m['G'];
            m['H']-=m['G'];
            m['T']-=m['G'];
            m['G']=0;
        }
        if(m['F']>0){
            a[5]+=m['F'];
            m['I']-=m['F'];
            m['V']-=m['F'];
            m['E']-=m['F'];
            m['F']=0;
        }
        if(m['V']>0){
            a[7]+=m['V'];
            m['S']-=m['V'];
            m['E']-=2*m['V'];
            m['N']-=m['V'];
            m['V']=0;
        }
        if(m['H']>0){
            a[3]+=m['H'];
            m['T']-=m['H'];
            m['R']-=m['H'];
            m['E']-=2*m['H'];
            m['H']=0;
        }
        if(m['O']>0){
            a[1]+=m['O'];
            m['N']-=m['O'];
            m['E']-=m['O'];
            m['O']=0;
        }
        if(m['I']>0){
            a[9]+=m['I'];
            m['N']-=2*m['I'];
            m['E']-=m['I'];
            m['I']=0;
        }
        printf("Case #%d: ",i);
        for(int j=0;j<10;j++){
            for(int k=0;k<a[j];k++){
                printf("%d",j);
            }
        }
        printf("\n");
    }
}
