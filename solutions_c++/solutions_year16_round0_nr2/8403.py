#include<bits/stdc++.h>
using namespace std;

int main()
{
freopen("B-large.in","r",stdin);
 freopen("B_output_file_name.out","w",stdout);
 long long int t=0,t1=1;
 scanf("%lld",&t);

 while(t1<=t)
    {
       char str[104];
       scanf("%s",&str);
       long long int flip=0,i=0;


       for(i=0;str[i]!='\0';)
        {
          if(str[i]=='-')
           {
             if(i==0)
                  flip++;
             else
                flip=flip+2;

             while(str[i]=='-')
                i++;
           }
           else
            i++;

        }




      printf("Case #%lld: %lld\n",t1,flip);
     t1++;
    }

return 0;
}
