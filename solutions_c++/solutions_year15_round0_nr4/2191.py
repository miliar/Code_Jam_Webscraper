#include<cstdio>
int i,t,a,b,c;

void g(){printf("Case #%d: GABRIEL\n",i+1);}
void r(){printf("Case #%d: RICHARD\n",i+1);}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(i=0;i<t;i++) {
        scanf("%d%d%d",&a,&b,&c);
        if(a==1)g();
        else if(a==2){
            if(b%2==0 || c%2==0)g();
            else r();
        }
        else if(a==3){
            if((b==2&&c==3)||(b==3&&c==2)||(b==4&&c==3)||(b==3&&c==4)||(b==3&&c==3))g();
            else r();
        }
        else if(a==4){
            if((b==3&&c==4)||(b==4&&c==3)||(b==4&&c==4))g();
            else r();
        }
    }
}
