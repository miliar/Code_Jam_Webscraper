
#include<stdio.h>

int T;

int main()
{
    scanf("%d",&T);
    int D,din,res,min,counter;
    int arr[1001];
    for(int i=0;i<T;i++)
    {
        scanf("%d",&D);
        for(int j=0;j<1001;j++)
            arr[j]=0;
        for(int j=0;j<D;j++)
        {
            scanf("%d",&din);
            arr[j]=din;
        }
        min=1000;
        for(int tope=1000;tope>0;tope--){
            counter=0;
            for(int j=0;j<D;j++){
                if(arr[j]>tope){
                    counter+=arr[j]/tope;
                    if((arr[j]%tope)==0)
                        counter--;
                }
            }
            if(counter+tope<min)
                min=counter+tope;
        }
        printf("Case #%d: %d\n",i+1,min);
    }
    return 0;
}
