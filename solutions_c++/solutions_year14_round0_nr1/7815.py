#include <iostream>
#include<stdio.h>

using namespace std;

int choose(int a[],int b[],int n)
{
    int card =0;
    int count =0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(a[i]==b[j])
                {
                    card = a[i];
                    count++;
                }
        }
    }
    if(count>1)
        return 17;
    else if(count ==0)
        return 0;
    else
        return card;

}
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small.out","w",stdout);

    int caseNum;
    cin>>caseNum;

    int firstArray[4][4];
    int secondArray[4][4];
    int firstRow,secondRow;
    int firstRowArray[4];
    int secondRowArray[4];

    int num =1;

    while(num<=caseNum)
    {
        cin>>firstRow;
        for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
            cin>>firstArray[i][j];
        if(i==firstRow-1)
        {
            for(int k=0;k<4;k++)
                firstRowArray[k] = firstArray[i][k];
        }
    }
        cin>>secondRow;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
            cin>>secondArray[i][j];
        if(i==secondRow-1)
        {
            for(int k=0;k<4;k++)
                secondRowArray[k] = secondArray[i][k];
        }

    }
    int flag = choose(firstRowArray,secondRowArray,4);
    if(flag == 0)
        cout<<"Case #"<<num<<": Volunteer cheated!"<<endl;
    else if(flag == 17)
        cout<<"Case #"<<num<<": Bad magician!"<<endl;
    else cout<<"Case #"<<num<<": "<<flag<<endl;

    num++;
    }


    return 0;
}
