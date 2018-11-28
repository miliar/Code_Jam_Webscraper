#include<cstdio>
#include<cstdlib>
#include<iostream>    

using namespace std;

int main(){
    int t,r1,r2,tmp,a1,a2;
    int m1[4][4],m2[4][4];
    
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        a1=a2=0;
        scanf("%d",&r1);
        r1=r1-1;
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                scanf("%d",&tmp);
                m1[j][k]=tmp;
            }
        }
        scanf("%d",&r2);
        r2=r2-1;
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                scanf("%d",&tmp);
                m2[j][k]=tmp;
            }
        }
        //cout<<"testando"<<endl;
        for(int j=0;j<4;j++){
            tmp=m1[r1][j];
          //  cout<<"R1 "<<tmp<<endl;
            for(int k=0;k<4;k++){
            //    cout<<m2[r2][k]<<endl;
                if(tmp==m2[r2][k]){
                    if(a1==0){
                        a1=tmp;
                    }else if(a1>0){
                        a1=20;
                    }
                }                    
            }            
        }
    //printf("case #%d: %d\n",i+1,a1);
    if(a1>0 && a1!=20)
        printf("case #%d: %d\n",i+1,a1);    
    if(a1==0)
        printf("case #%d: Volunteer cheated!\n",i+1);    
    if(a1==20)
        printf("case #%d: Bad magician!\n",i+1);
    
    }    

    
    return 0;
}
