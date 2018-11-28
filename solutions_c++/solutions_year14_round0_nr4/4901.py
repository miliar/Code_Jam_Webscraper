

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




int main()




{

    

    FILE *fp=fopen("Bla.txt", "w");

    int n,m,r,t,i,j,k=0,p,q;

    double a[10],b[10];

    

/*

    char mine[50][50];

    for (i=0; i<50; i++) {

        for (j=0; j<50; j++) {

            mine[i][j] = '.';

        }

    }

    mine[0][0] = 'c';

  */

    

    scanf("%d",&t);

    while (k++<t)

        

    {

        p=0,q=0;

        scanf("%d",&m);

        for (i=0; i<m; i++) {

            scanf("%lf",&a[i]);

        }

        for (i=0; i<m; i++) {

            scanf("%lf",&b[i]);

        }

        

        sort(a, a+m);

        sort(b, b+m);

        

        for (i=0,j=0; i<m; i++) {

            for (; j<m; j++) {

//                cout<<a[i]<<' '<<b[j]<<endl;

                if (a[i]<b[j]) {

                    q++;

                    j++;

                    break;

                }

            }

        }

        for (i=0,j=0; j<m; j++) {

            for (; i<m; i++) {

                if (a[i]>b[j]) {

                    p++;

                    i++;

                    break;

                }

            }

        }

        q=m-q;

        printf("Case #%d: %d %d\n",k,p,q);

        fprintf(fp,"Case #%d: %d %d\n",k,p,q);

        

        

    }

    

    

    

    fclose(fp);




    

    return 0;

    

    

    

}
