//




//  main.cpp




//  ACM_TEST




//




//  Created by Synceokhou on 2/23/14.




//  Copyright (c) 2014 Synceokhou. All rights reserved.




//



















#include <iostream>







#include <cstdio>




#include <stdlib.h>




#include <algorithm>










using namespace::std;







int card[4][4],card_t[4][4];



















int main()




{

    
    FILE *fp = fopen("A-small-attempt1.out.txt","w");
    int n,t,i,j,r=0;

    double c,f,x,q;

    scanf("%d",&t);

    while (r++<t)

    {

        //        cout<<r<<endl;

        

        scanf("%lf %lf %lf",&c,&f,&x);

        

        n=int(x/c);

        //    cout<<n;

        double *total_t = new double[n+2];

        //        double total_t[79];

        q = x/2;

 

        for (i=0; i<n+2; i++) {

            total_t[i]=0;

            //            cout<<i<<endl;

        }




        for (i=0; i<=n; i++) {

/*            for (j = 0; j<i; j++) {

                

                total_t[i] = total_t[i] + c/(2+j*f);

            }

            total_t[i] = total_t[i] + x/(2+j*f);

 */

            if (i==0) {

                total_t[i]=x/2;

            }

            else

            {

                total_t[i] = total_t[i-1]+(c-x)/(2+(i-1)*f)+x/(2+i*f);

                

            }

//            cout<<(c-x)/(2+(i-1)*f)<<' '<<(c-x)/(2+(i-1)*f)<<' '<<x/(2+i*f);

            if (q>total_t[i]) {

                q=total_t[i];

            }

            

        }

        

        

        

        

        

        

        printf("Case #%d: %.7f\n",r,q);
        fprintf(fp,"Case #%d: %.7f\n",r,q);

        

        

    }

    fclose(fp);

    return 0;

    

}
