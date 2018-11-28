#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
//Magic trick <A-small-attempt0> file.out;
using namespace std;


int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
freopen("final1.out", "w", stdout);
    int t,t1,row,temp,tempr=1,i=0,j=0,icount=0,k=0,r=0;
    scanf("%d",&t);
    t1=t;
    int first[4];
    int second[4];
    int result[t];

    while(t--)
    {
        scanf("%d",&row);
int val=16;
        while(val--)

        {
           if(tempr==row)
           {
               scanf("%d",&temp);
               first[i]=temp;
               ++icount;
               ++i;
           }

            else if(tempr!=row)
            {
                scanf("%d",&temp);
                ++icount;
            }
            if(icount==4)
            {
                ++tempr;
                icount=0;
            }


        }

        icount=0;tempr=1;i=0;

         scanf("%d",&row);
val=16;
        while(val--)

        {
           if(tempr==row)
           {
               scanf("%d",&temp);
               second[i]=temp;
               ++icount;
               ++i;
           }

            else if(tempr!=row)
            {
                scanf("%d",&temp);
                ++icount;
            }
            if(icount==4)
            {
                ++tempr;
                icount=0;
            }


        }
        sort(first,first+4);
        sort(second,second+4);
       /* val=4;i=0;
        cout<<endl;
        while(val--)
          {

           cout<<first[i]<<"  " ;
        ++i;}

         val=4;i=0;
        cout<<endl;
        while(val--)
          {

           cout<<second[i]<<"  " ;
        ++i;}*/
        i=0;j=0;

        while(i<4&&j<4)
        {

            if(first[i]<second[j])
                  ++i;
                  else if(first[i]>second[j])
                    ++j;
                  else if(first[i]==second[j])
                {
                    if(k==0)
                    {


                        k=first[i];
                        ++i;++j;}

                    else {

                        k=17;
                        break;
                    }
                }


        }
       // cout<<r<<" k is-- "<<k<<"  ";
        result[r]=k;
        k=0;
        ++r;
        icount=0;
        i=0;j=0;
        tempr=1;


    }
    i=0;
    for(i=0;i<t1;i++)
    {
        if(result[i]==0)
            printf("Case #%d: Volunteer cheated!\n",i+1);
        else if(result[i]==17)
            printf("Case #%d: Bad magician!\n",i+1);
        else
            printf("Case #%d: %d\n",i+1,result[i]);
    }



   return 0;

}
