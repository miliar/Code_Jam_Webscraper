#include <iostream>


using namespace std;

void Sort(float k[],int lb,int ub)
{
 int i,j,flag=0;
 float temp,key;

 if (lb<ub)
    {
     i=lb;
     j=ub+1;
     key=k[i];
     while(flag!=1)
      {
       i++;
       while(k[i]<key)
        {
         i++;
        }
       j--;
       while(k[j]>key)
        {
         j--;
        }
       if (i<j)
          {
           temp=k[i];
           k[i]=k[j];
           k[j]=temp;
          }
       else
          {
           flag=1;
           temp=k[lb];
           k[lb]=k[j];
           k[j]=temp;
          }
      }
     Sort(k,lb,j-1);
     Sort(k,j+1,ub);
    }
}


int main()
{
    int t,n,r1[50],r2[50],chcount=0,nmcount=0;
    float a[1000]={0.0},b[1000]={0.0};
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>n;
        for(int j=0;j<n;j++)
            cin>>a[j];

        for(int j=0;j<n;j++)
            cin>>b[j];

        Sort(a,0,n-1);
        Sort(b,0,n-1);


        chcount=0;
        nmcount=0;
        int p,q;

        p=n-1;
        q=n-1;
        while(p>-1&&q>-1)
        {
          if(a[p]>b[q])
          {
            chcount++;
            p--;
            q--;
          }
          else
          {
              q--;
          }
        }
        r1[i]=chcount;

        p=0;
        q=0;

        while(p<n&&q<n)
        {
            if(b[q]>a[p])
            {
                nmcount++;
                q++;
                p++;
            }
            else
            {
                q++;
            }
        }
        r2[i]=n-nmcount;
    }

    for(int i=0;i<t;i++)
    {
        cout<<"Case #"<<i+1<<": "<<r1[i]<<" "<<r2[i]<<"\n";
    }
    return 0;
}
