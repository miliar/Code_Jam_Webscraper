#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;
int main()
{
    int t,n,i;
    float a[1000],b[1000];
    cin>>t;
    for(int k=1;k<=t;k++)    {
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>a[i];
        }
         for(i=0;i<n;i++)
        {
            cin>>b[i];
        }
        sort(a,a+n);
        sort(b,b+n);  // descending
        int win =0,win1=0;
        int j=0,l=n-1;
        for(i=0;i<n;i++)
        {
            if(a[i]<b[j])
               {
                   //cout<< a[i]<<" "<<b[l];
                   l--;
               }
            else
            {
                //cout<< a[i]<<" "<<b[j];
                j++;
                win++;
            }
            //cout<<endl;
        }
        //win = n - i;
        sort(b,b+n);

         for(i=0;i<n;i++)
        {
           int flag =1;
            for( j=0;j<n;j++)
            {
                if(a[i]<b[j]&& b[j]!=2)
                {
                    b[j]=2; flag=0;break;
                }

            }
            if(flag ==1)
            {
                win1++;
                int m=0;
                while(b[m]==2)
                    m++;
                b[m]=2;
            }

        }

    cout<<"Case #"<<(k)<<": "<<win<<" "<<win1;
    cout<<endl;
    }
    return 0;
}

