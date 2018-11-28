#include<iostream>
#include<string>
#include<fstream>
#include<algorithm>
#include<cmath>
using namespace std;

int main()
{
    fstream f1,f2;
    f1.open("input.in",ios::in);
    f2.open("output.txt",ios::out);
    int t,w=1;
    f1>>t;
    while(t--)
    {
        int i,j,k,cnt1=0,cnt2=0,n;
        double l,m,a[10010],b[10010];
        f1>>n;
        for(i=0;i<n;i++)
            f1>>a[i];
        for(i=0;i<n;i++)
            f1>>b[i];

        sort(a,a+n);
        sort(b,b+n);

        k=0;
        for(i=0;i<n;i++)
        {
            int flag=0;
            for(j=k;j<n;j++)
            {
                if(a[i]<b[j])
                {
                    k=j+1;
                    flag=1;
                    break;
                }
            }
            if(flag==0)
                cnt1++;
        }

        i=n-1;
        j=n-1;
        int temp=0;
        while(a[i]<b[j]&&j>=0)
        {
            j--;
            temp++;
        }
        k=0;

        for(i=temp;i<n;i++)
        {
            for(k=k;k<=j;k++)
            {
                if(a[i]>b[k])
                {
                    cnt2++;
                    k++;
                    break;
                }
                else
                {
                    break;
                }
            }
        }

        f2<<"Case #"<<w<<": "<<cnt2<<" "<<cnt1<<"\n";

        w++;
    }
    return 0;
}
