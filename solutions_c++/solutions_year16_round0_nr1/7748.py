#include<iostream>
#include<cstdio>
using namespace std;
int main()
{

    int t;
    long n;
    int arr[10];
    freopen("A-large.in","r",stdin);
    freopen("output1.out","w",stdout);
    scanf("%d",&t);
    for(int k=0;k<t;k++)
    {
        scanf("%ld",&n);
        if(n==0)
        {   cout<<"case #"<<(k+1)<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        long temp=n;
        for(int i=0;i<10;i++)
            arr[i]=0;
        while(temp>0)
        {   int c=temp%10;
            arr[c]=1;
            temp/=10;
        }
        bool b=false;
        int i=2;
        while(b !=true)
        {
                temp=i*n;
                if(i>111)
                    break;
                while(temp>0)
                {
                    int c=temp%10;
                    arr[c]=1;
                    temp/=10;
                    b=true;
                    for(int j=0;j<10;j++)
                        if(arr[j]!=1)
                            b=false;
                }
                if(b==true)
                    break;
                    i++;
        }
        if(b==true)
                cout<<"case #"<<(k+1)<<": "<<i*n<<endl;
        else
                cout<<"case #"<<(k+1)<<": "<<"INSOMNIA"<<endl;
    }
    fclose(stdin);
    fclose (stdout);
    return 0;
}
