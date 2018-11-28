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



















int main(void)




{

    

    int n,m,t,i,j,k=0,r=0,q=0;

    FILE *fp=fopen("A-small-attempt1.out.txt","w");

    scanf("%d",&t);

 //   cout<<t<<endl;

    while (r++<t)

        

    {

  //      cout<<r<<endl;




        

        scanf("%d",&n);

        for (i= 0 ; i<4; i++) {

            scanf("%d %d %d %d",&card[i][0],&card[i][1],&card[i][2],&card[i][3]);

        }

        

        scanf("%d",&m);

        for (i= 0 ; i<4; i++) {

            scanf("%d %d %d %d",&card_t[i][0],&card_t[i][1],&card_t[i][2],&card_t[i][3]);

        }

        

        

        k = 0;

        for (i=0; i<4; i++) {

            for (j=0; j<4; j++) {

 //               cout<<'*'<<card[n-1][i]<<' '<<card_t[j][m-1]<<'*'<<endl;

                if (card[n-1][i]==card_t[m-1][j]) {

                    k++;

                    q = card_t[m-1][j];

                }

            }

        }

        if (k>1) {

            printf("Case #%d: Bad magician!\n",r);
fprintf(fp,"Case #%d: Bad magician!\n",r);
        }

        if (k==1) {

            printf("Case #%d: %d\n",r,q);
fprintf(fp,"Case #%d: %d\n",r,q);
        }

        if (k==0) {

            printf("Case #%d: Volunteer cheated!\n",r);
               fprintf(fp,"Case #%d: Volunteer cheated!\n",r);
        }

         

         

    }
       fclose(fp);
//    cin>>n;    

    return 0;




}
