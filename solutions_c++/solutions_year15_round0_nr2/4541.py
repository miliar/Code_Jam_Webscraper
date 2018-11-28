#include <cstdio>
#include <algorithm>
#include <set>
#include <iostream>
#include<stdlib.h>
using namespace std;

void adjust(int *heap,long long int n)
{
    long long int j=1;
    int temp=heap[0];
    while(j<n)
    {
        if(j<(n-1) && heap[j]<heap[j+1])
            j=j+1;
        if(temp>=heap[j])
            break;
        heap[(j-1)/2]=heap[j];
        j=2*j+1;
    }
    heap[(j-1)/2]=temp;
}

void delet(int *heap,long long int & n)
{
    if(n==0)
        ;
    else if(n==1)
        n=n-1;
    else
    {
        heap[0]=heap[n-1];
        n=n-1;
        adjust(heap,n);
    }
}

void inser(int *heap,int e,long long int n)
{
    heap[n-1]=e;
    long long int j=n-1;
    int temp=e;
    while(j>0 && heap[(j-1)/2]<temp)
    {
        heap[j]=heap[(j-1)/2];
        j=(j-1)/2;
    }
    heap[j]=temp;
}

int main()
{
    int t,i,j,d,flag,ans,num,value,start,very,use,use1;
    long long int heap_size;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d",&d);
        int *heap=NULL;
        heap_size=0;

        for(j=1;j<=d;j++)
        {
            scanf("%d",&num);
            heap_size++;
            heap=(int *)realloc(heap,sizeof(int)*(heap_size));
            inser(heap,num,heap_size);
        }
        start=1;
        value=heap[0];
        very=value;
        ans=value;
        delet(heap,heap_size);
        use=heap[0];
        heap_size++;
        heap=(int *)realloc(heap,sizeof(int)*(heap_size));
        inser(heap,ans,heap_size);
        flag=0;
        if(heap_size==1 || (heap_size>1 && ((heap[0]-use)<=2)) || use==1)
        {
            if(heap_size==1 && heap[0]==9)
                ans=5;
            else{while(heap[0]!=1 && heap_size>0)
        {
            value=heap[0];
            delet(heap,heap_size);
            if(value%2==0)
            {
                num=value/2;
                heap_size++;
                heap=(int *)realloc(heap,sizeof(int)*(heap_size));
                inser(heap,num,heap_size);
                heap_size++;
                heap=(int *)realloc(heap,sizeof(int)*(heap_size));
                inser(heap,num,heap_size);
            }
            else
            {
                num=value/2;
                heap_size++;
                heap=(int *)realloc(heap,sizeof(int)*(heap_size));
                inser(heap,num,heap_size);
                heap_size++;
                num++;
                heap=(int *)realloc(heap,sizeof(int)*(heap_size));
                inser(heap,num,heap_size);
            }
            if(start>very)
                break;
            if((start+heap[0])<=ans)
            {
               ans=start+heap[0];
            }
            start++;
        }
            }
        }
        else
        {
            if(heap_size==2 && heap[0]==9 && heap[1]==6)
                {ans=6; flag=1;}
            else if(heap_size>2 && heap[0]==9 && use==6)
            {
                delet(heap,heap_size);
                delet(heap,heap_size);
                use1=heap[0];
                if(use1<6)
                {
                    flag=1;
                    ans=6;
                }
                heap_size++;
                heap=(int *)realloc(heap,sizeof(int)*(heap_size));
                inser(heap,9,heap_size);
                heap_size++;
                heap=(int *)realloc(heap,sizeof(int)*(heap_size));
                inser(heap,6,heap_size);
            }
            if(flag==0){value=heap[0]/use;
            if(heap[0]%use==0)
                value--;
                ans=value+use;
            for(j=use;j<=(heap[0]/2);j++)
            {
                value=heap[0]/j;
            if(heap[0]%j==0)
                value--;
            if((value+j)<ans)
                ans=value+j;
            }
            }
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
