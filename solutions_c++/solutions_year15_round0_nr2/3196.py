#include <iostream>
#include <algorithm>


using namespace std;

int Dp[1005][1005];

int generateDp()
{
    int curValue;
    int minValue;
    for(int i=1;i<=1000;i++)
    {
        for(int j=1;j<i;j++)
        {
            minValue=2000;
            for(int k=1;k<=i/2;k++)
            {
                curValue=Dp[k][j]+Dp[i-k][j];
                if(curValue<minValue)
                    minValue=curValue;
            }
            Dp[i][j]=minValue+1;
        }
    }
    return 0;
}

int main()
{
    int size;
    int dNum;
    freopen("D:\\ccpptrain\\codejamPancakes\\B-large.in","r",stdin);
   freopen("D:\\ccpptrain\\codejamPancakes\\pancakesoutput3.txt","w",stdout);
    cin>>size;
    memset(Dp,0,sizeof(Dp));
    generateDp();
    for(int i=0;i<size;i++)
    {
        cin>>dNum;
        int *input=new int[dNum];
        int maxValue=0;
        for(int j=0;j<dNum;j++)
        {
            cin>>input[j];
            if(input[j]>maxValue)
                maxValue=input[j];
        }
        int  minStep=2000;
        for(int k=1;k<=maxValue;k++)
        {
             int curStep=k;
             for(int m=0;m<dNum;m++)
             {
                    curStep+=Dp[input[m]][k];
             }
             if(curStep<minStep)
             {
                 minStep=curStep;
             }
        }
        cout<<"Case #"<<i+1<<": "<<minStep<<endl;
        delete []input;
    }
    return 0;
}
