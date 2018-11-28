#include<bits/stdc++.h>
using namespace std;
int main()
{

    freopen("A-small-attempt6.in","r",stdin);
    freopen("out2.o","w",stdout);
    int visited[12];
    int i,j,k,l,m,n,u=1,t;
    long long a,b,c,d,e;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        scanf("%d",&m);
        int cou=0;
        memset(visited,0,sizeof visited);
         j=1;
        while(cou!=10&&m!=0){

        b=m*j;
    //    cout<<b<<endl;
    c=b;
        while(b!=0){
            d=b%10;
       //     cout<<"fdgd"<<d<<endl;
            if(visited[d]==0){
                visited[d]=1;
                cou++;
            }
            b=b/10;
        }
        j++;
        if(cou>=10)break;
    }
    if(cou==10){
        printf("Case #%d: %I64d\n",u++,c);
    }
      //  fprintf(y,"Case #%d: %I64d\n",u++,c);}
    else {
        printf("Case #%d: INSOMNIA\n",u++);
    }
       // fprintf(y,"Case #%d: INSOMNIA\n",u++);}
    }

}

