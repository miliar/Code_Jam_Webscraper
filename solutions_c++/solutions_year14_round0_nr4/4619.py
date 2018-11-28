#include<iostream>
#include<cstdio>

using namespace std;

float naomi[1000],naomi1[1000];
float ken[1000],ken1[1000];


int dwar(int size)
{
    int count=0,count1=0;
    float temp;
    int i,j,a,b,min;
    for(i=0;i<size;i++)
    {
        if(naomi1[i]<ken1[0])
        {
            count1++;
            naomi1[i]=0;
        }
    }
    for (a=0;a<size-1;a++)
    {
        min=a;
        for(b=a+1;b<size;b++)
        {
            if(naomi1[b]<naomi1[min])
                min=b;
        }
        if(min!=a)
        {
            temp=naomi1[min];
            naomi1[min]=naomi1[a];
            naomi1[a]=temp;
        }
    }
    for(j=0;j<size-count1;j++)
    {
        for(i=0;i<size;i++)
        {
            if(naomi1[i]>ken1[j])
            {
                naomi1[i]=0;
                count++;
                break;
            }
        }
        ken1[j]=0;
    }
    return count;
}


int war(int size)
{
    int count=0,count1=0;
    int i,j;
    for(i=0;i<size;i++)
    {
        for(j=0;j<size;j++)
        {
            if(ken[j]>naomi[i])
            {
                //cout<<naomi[i]<<" "<<ken[j]<<" ";
                ken[j]=0;
                count1++;
                break;
            }
        }
        naomi[i]=0;
    }
    //cout<<"\n"<<count1<<"\n";
    count=size-count1;
    return count;
}

int main()
{
    int i,size,a,b,min,test_case,k;
    float temp;
    cin>>test_case;
    for(k=0;k<test_case;k++){
    cin>>size;
    for(i=0;i<size;i++)
    {
        cin>>naomi[i];
    }
    for(i=0;i<size;i++)
    {
        cin>>ken[i];
    }
    for(i=0;i<size;i++)
    {
        naomi1[i]=naomi[i];
        ken1[i]=ken[i];
    }
    for (a=0;a<size-1;a++)
    {
        min=a;
        for(b=a+1;b<size;b++)
        {
            if(naomi[b]<naomi[min])
                min=b;
        }
        if(min!=a)
        {
            temp=naomi[min];
            naomi[min]=naomi[a];
            naomi[a]=temp;
        }
    }
    for (a=0;a<size-1;a++)
    {
        min=a;
        for(b=a+1;b<size;b++)
        {
            if(ken[b]<ken[min])
                min=b;
        }
        if(min!=a)
        {
            temp=ken[min];
            ken[min]=ken[a];
            ken[a]=temp;
        }
    }
    for (a=0;a<size-1;a++)
    {
        min=a;
        for(b=a+1;b<size;b++)
        {
            if(ken1[b]<ken1[min])
                min=b;
        }
        if(min!=a)
        {
            temp=ken1[min];
            ken1[min]=ken1[a];
            ken1[a]=temp;
        }
    }
    cout<<"Case #"<<(k+1)<<": "<<dwar(size)<<" "<<war(size)<<"\n";}


}
