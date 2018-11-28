#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    int test,row1,row2,num,count,cards1[4][4],cards2[4][4],temp1[4],temp2[4],flag;
    FILE *ptr;
    ptr=fopen("input1.in","r");
    fscanf(ptr,"%d",&test);
    for(int t=0;t<test;t++)
    {
        count=0;
        flag=0;
        fscanf(ptr,"%d",&row1);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                fscanf(ptr,"%d",&cards1[i][j]);
        }
        for(int i=0;i<4;i++)
            temp1[i]=cards1[row1-1][i];
        fscanf(ptr,"%d",&row2);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                fscanf(ptr,"%d",&cards2[i][j]);
        }
        for(int i=0;i<4;i++)
            temp2[i]=cards2[row2-1][i];
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(temp1[i]==temp2[j])
                    {
                        count++;
                        if(count==1)
                            num=temp1[i];
                    }

                if(count >1)
                {
                    cout<<"Case #"<<t+1<<": Bad magician!"<<endl;
                    flag=1;
                    break;
                }
            }
            if(flag==1)
                break;
        }
        if(count==0)
           cout<<"Case #"<<t+1<<": Volunteer cheated!"<<endl;
        if(count==1)
            cout<<"Case #"<<t+1<<": "<<num<<endl;
    }
    fclose(ptr);
    return 0;
}
