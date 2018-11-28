#include<bits/stdc++.h>
using namespace std;
int a[10];
int check(int a[],int size)
{
    int i,c=0;
    for(i=0;i<10;i++)
    {
        if(a[i]>0)
            c++;
    }
    if(c==10)
        return 1;
    else
        return 0;
}
void insert(int a[],int size,int num)
{
    int rem;
    while(num>0)
    {
        rem=num%10;
        a[rem]++;
        num=num/10;
    }
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    int k=1;
    while(t--)
    {
        int n;
        cin>>n;
        for(int j=0;j<10;j++)
            a[j]=0;
        if(n==0)
            printf("Case #%d: INSOMNIA\n",k);
        else{
            int i=1;
            long long int temp;
            while(true)
            {
                temp=i*n;
                insert(a,10,temp);
                int ch=check(a,10);
                if(ch==1){
                    printf("Case #%d: %d\n",k,temp);
                    break;
                }
                else
                    i++;
            }
        }
        k++;
    }
}
