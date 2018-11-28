#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
int main()
{

    int t,cases=1;
    cin>>t;
    while(t--)
    {
        int num;
        cin>>num;

        double arr[1005],copyarr[1005], arr2[1005], copyarr2[1005];
        for(int i=0; i<num; i++)
        {
            cin>>arr[i];
            copyarr[i]=arr[i];

        }
        for(int i=0; i<num; i++)
        {
            cin>>arr2[i];
            copyarr2[i]=arr2[i];

        }

        sort(arr,arr+num);
        sort(arr2,arr2+num);

        sort(copyarr,copyarr+num);
        sort(copyarr2,copyarr2+num);


        double maxNum =0;
        int save,j=0;
        int count=0;
        int c2=0;
        for(int i=0; i<num; i++)
        {

            if(arr[i]!=0)
            {

                for( j=0; j<num; j++)
                {

                    if(arr2[j]!=0 && arr2[j]<arr[i])
                    {

                        count++;
                        arr[i]=0;
                        arr2[j]=0;
                        break;
                    }
                }
                if(j==num)
                {

                    for( j=0; j<num; j++)
                    {

                        if(arr2[j]!=0 && arr2[j]>arr[i])
                        {
                            if(arr2[j]>maxNum)
                            {
                                maxNum=arr2[j];

                                save=j;
                            }
                        }

                    }
                    arr2[save]=0;
                arr[i]=0;

                }




            }

        }


        for(int i=0; i<num; i++)
        {
            if(copyarr[i]!=0)
            {
                for( j=0; j<num; j++)
                {

                    if(copyarr2[j]!=0 && copyarr2[j]>copyarr[i])
                    {

                        c2++;
                        copyarr[i]=0;
                        copyarr2[j]=0;
                        break;

                    }
                }
            }
        }

        printf("Case #%d: %d %d\n",cases++,count,num-c2);

    }
    return 0;
}
