#include<iostream>
using namespace std;
int main()
{
    int testCases, rowNum1,rowNum2,posMatchFound,found;
    int t1,t2,t3,t4,tR;
    int cardGrid1[4],cardGrid2[4];
    scanf("%d" , &testCases);
    for (int tCase=1; tCase <= testCases; tCase++)
    {
        posMatchFound=-1;
        found=0;
        scanf("%d", &rowNum1);
        for(tR=1;tR<=4;tR++)
        {
                            if (tR != rowNum1) 
                            {
                               scanf("%d %d %d %d",&t1,&t2,&t3,&t4);
                            }
                            else 
                            {
                               scanf("%d %d %d %d",&cardGrid1[0],&cardGrid1[1],&cardGrid1[2],&cardGrid1[3]);
                            }
        }
        scanf("%d", &rowNum2);
        for(tR=1;tR<=4;tR++)
        {
                            if (tR != rowNum2) 
                            {
                               scanf("%d %d %d %d",&t1,&t2,&t3,&t4);
                            }
                            else 
                            {
                               scanf("%d %d %d %d",&cardGrid2[0],&cardGrid2[1],&cardGrid2[2],&cardGrid2[3]);
                            }
        }
        for ( int firstRec=0;firstRec<4;firstRec++) 
        {
            for (int secondRec=0;secondRec<4; secondRec++)
            {
//                    printf("\nmatching %d with %d",cardGrid1[firstRec],cardGrid2[secondRec]);
                    if (cardGrid1[firstRec]==cardGrid2[secondRec])
                    {
                       posMatchFound=firstRec;
                       found++;
//                       printf("MATCH FOUND FOR %d... Setting posMatchFound to %d",    cardGrid1[firstRec],posMatchFound);                                         
                    }                   
            }
        }
        if (posMatchFound < 0)
        {
              printf ("Case #%d: Volunteer cheated!\n",tCase );              
        }
        else if (found > 1)
        {
             printf ("Case #%d: Bad magician!\n",tCase);
        }
        else
        {
            printf ("Case #%d: %d\n",tCase,cardGrid1[posMatchFound]);
        }
    }

    return(0);
}
