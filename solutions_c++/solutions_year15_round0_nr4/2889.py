#include<bits/stdc++.h>
using namespace std;
int main()
{
    int x,r,c,flag,t;
    FILE *fr=fopen("D-small-attempt0.in","r");
    FILE *fw=fopen("codejam4small.txt","w");
    //cin>>t;
    fscanf(fr,"%d",&t);
    for(int tc=1;tc<=t;tc++){
        //cin>>x>>r>>c;
        fscanf(fr,"%d%d%d",&x,&r,&c);
        if(x==1){
            //cout<<"GABRIEL\n";
            fprintf(fw,"Case #%d: GABRIEL\n",tc);
            continue;
        }
        if(r==1){
            if(x==2){
            if(c==2 || c==4)    flag=1;
            else flag=0;}

            if(x==3 || x==4){
                flag=0;
            }
        }
        else if(r==2){
            if(x==2)    flag=1;
            if(x==3){
                if(c==3)    flag=1;
                else flag=0;
            }
            if(x==4)    flag=0;
        }
        else if(r==3){
            if(x==2){
                if(c==2 || c==4)    flag=1;
                else flag=0;
            }
            if(x==3){
                if(c==1)    flag=0;
                else flag=1;
            }
            if(x==4){
                if(c==4)    flag=1;
                else flag=0;
            }
        }
        else if(r==4){
            if(x==2)    flag=1;
            if(x==3){
                if(c==3)    flag=1;
                else flag=0;
            }
            if(x==4){
                if(c==1 || c==2)    flag=0;
                else flag=1;
            }
        }
        if(flag==0) fprintf(fw,"Case #%d: RICHARD\n",tc);//cout<<"RICHARD\n";
        else fprintf(fw,"Case #%d: GABRIEL\n",tc);//cout<<"GABRIEL\n";
    }
    return 0;
}
