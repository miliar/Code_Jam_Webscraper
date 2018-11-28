#include<cstdio>
#include<iostream>
using namespace std;
int main()
{

    //freopen("in.txt","r",stdin);
   // freopen("out.txt","w",stdout);
    int T,n,a,i;
    scanf("%d",&T);
    int ansk=1;
    while(T--)
    {
        printf("Case #%d: ",ansk++);
        scanf("%d",&n);
        int s=0,sum=0;
        string b;
        cin>> b;
        s=b[0]-'0';
        for(i=1;i<n;i++)
        {
            if(s>=i){
            a=b[i]-'0';
            s+=a;
            }else{
            a=b[i]-'0';
            s+=a;
            sum++;
            s++;
            }

        }//



           /* if(s>=i)
            {
                 a=b[i]-'0';
                 s+=a;
                printf("i=%d s=%d\n",i,s);

            }else {

                a=b[i]-'0';
                 s+=a;

                sum += (i-s);
                s+=(i-s);
                printf("i=%d s=%d  sum = %d\n",i,s,sum);
            }

        }
        printf("Ç°%d\n",sum);
        if(s<i) {sum += (i-s);}
        printf("ºó%d\n",sum);*/
        if(  !(s>=i) )sum++;
         printf("%d\n",sum);

    }
    return 0;
}
