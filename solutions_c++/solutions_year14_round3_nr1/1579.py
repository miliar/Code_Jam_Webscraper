#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int a,b,z,x,y,k;
    int i,t,tes;
    char s[2423];
    //freopen("#in.txt", "r", stdin);
   // freopen("#out.txt", "w", stdout);
    scanf("%d",&t);
    for(tes=1;tes<=t;tes++)
    {
        printf("Case #%d: ",tes);
        scanf("%s",s);
        i=0;
        a=0;
        while(s[i]!='/')
        {
            a=a*10+s[i]-'0';
            i++;
        }

        i++;
        b=0;
        while(s[i]!='\0')
        {
            b=b*10+s[i]-'0';
            i++;
        }
        //if(a>b) {printf("impossible\n");continue;}
       // printf("%lld %lld\n",a,b);

       x=a;
       y=b;
       while(y!=0)
       {
           z=x;
           x=y;
           y=z%y;
       }
       a=a/x; b=b/x;
       i=0;
       z=1;
       while(i<40) {z=z*2; i++;}
      // printf("%lld",z);
      if(z%b==0)
      				{
      					long long int y=z/b;
      					b=b*(y);
      					a=a*(y);
      				}
      else {printf("impossible\n");continue;}

      int check=0;
      i=0;

      while((a<b)&&(i<=40))
       {
          if(b%2==0) b=b/2;

          else {check=1; break;}

          i++;
       }

       if((check==1)&&(i>40)) {printf("impossible\n");}

       else printf("%d\n",i);
        }
    return 0;
}

