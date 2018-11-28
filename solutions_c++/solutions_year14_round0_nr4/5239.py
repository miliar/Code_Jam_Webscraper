#include <iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
    int t,n,i,c_1,c_2,x=1,j;
    cin>>t;
    while(t--)
    {
        c_1=0;
        c_2=0;
        cin>>n;
        double ken[n],naomi[n],ken_2[n],naomi_2[n],temp;
        cin>>naomi[0];
        naomi_2[0]=naomi[0];
        for(i=1;i<n;++i)
        {
            cin>>naomi[i];
            naomi_2[i]=naomi[i];
        }
        sort(naomi,naomi+n);
        sort(naomi_2,naomi_2+n);

        cin>>ken[0];
        ken_2[0]=ken[0];
        for(i=1;i<n;++i)
        {
        	cin>>ken[i];
            ken_2[i]=ken[i];
        }

        sort(ken,ken+n);
        sort(ken_2,ken_2+n);
        for(i=n-1;i>=0;--i)
        {
            if(naomi[i]>ken[i])
            {
                c_1++;
                for(j=0;j<i+1;++j)
                    ken[j]=ken[j+1];
            }
        }
        j=n-1;
        for(i=0;i<n;++i)
        {
            for(j=0;j<n;++j)
            {
                if(naomi_2[j]>ken_2[i])
                   {
                    naomi_2[j]=0;
                    c_2++;
                    break;
                    }

            }
        }

        cout<<"Case #"<<x<<": "<<c_2<<" "<<c_1<<"\n";
        x=x+1;
    }
    return 0;

    }

