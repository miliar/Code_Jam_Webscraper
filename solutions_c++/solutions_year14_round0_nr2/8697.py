#include<iostream>
#include<stdio.h>
 using namespace std;
  int main()
  {
       int T;
        float c,f,x,min,c_temp,temp,t;
        cin>>T;
        // for(int m=1;m<=T;m++)
        int i=1;
        while(i<=T)
            {
                cin>>c>>f>>x; //printf("%.7f")
         t=2; temp=0;
         min=float(x/t);
          c_temp=c/t;
           t=t+f;
            temp=c_temp+float(x/t);
            while(temp<min)
                {
                    min=temp;
            c_temp=c_temp+float(c/t);
             t=t+f;
              temp=c_temp+float(x/t);
               }
                printf("Case #%d: %.7f",i,min);
                cout<<endl;
                i++;

                 }
                  return 0;
}
