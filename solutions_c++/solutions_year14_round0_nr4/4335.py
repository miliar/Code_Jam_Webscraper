#include<iostream>
#include<list>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
double a[3000];
template<class T>
void quicksort(T A[],int l,int r)
{
     if(l>=r) return;
     int i=l;
     int j=r;
     T x=A[(l+r)/2];//x=A[random(l-r)]
     while(i<=j)
     {
                while(A[i]<x) i++;
                while(A[j]>x) j--;
                if(i<=j)
                {
                        T temp=A[i];
                        A[i]=A[j];
                        A[j]=temp;
                        i++;j--;
                }
     }
     quicksort(A,l,j);
     quicksort(A,i,r);

}
double naomi[3000];
double ken[30000];
int main()
{
    freopen("E:\\in.c","r",stdin);
    freopen("E:\\out","w",stdout);
    int i,j,t,k;
    cin>>t;
    for(int tc=1;tc<=t;++tc)
    {
        int n;
        cin>>n;
        for(i=0;i<n;++i)
            cin>>naomi[i];
        for(i=0;i<n;++i)
            cin>>ken[i];
        quicksort(ken,0,n-1);
        quicksort(naomi,0,n-1);
        list<double>lken;
        list<double>lnaomi;
        for(i=0;i<n;++i)
            lken.push_back(ken[i]);
        for(i=0;i<n;++i)
            lnaomi.push_back(naomi[i]);
        int naomiscore1=0;
        list<double>::iterator itn;
        list<double>::iterator itk;
        for(i=0;i<n;++i)
            {
                int f=0;
                itn=lnaomi.begin();
                for(itk=lken.begin();itk!=lken.end();++itk)
                {
                    if(*itk>*itn)
                    {
                        lken.erase(itk);
                        lnaomi.erase(itn);
                        f=1;
                        break;
                    }
                }
                if(f==0)
                {
                    itk=lken.end();
                    itk--;
                    lken.erase(itk);
                    lnaomi.erase(itn);
                    naomiscore1++;
                }
            }
           // cout<<naomiscore1<<"\n";

        lken.clear();
        lnaomi.clear();
        for(i=0;i<n;++i)
            lken.push_back(ken[i]);
        for(i=0;i<n;++i)
            lnaomi.push_back(naomi[i]);
        int naomiscore2=0;
        for(i=0;i<n;++i)
        {
            itk=lken.begin();
            int f=0;
            for(itn=lnaomi.begin();itn!=lnaomi.end();++itn)
            {
                if(*itn>*itk)
                {
                    naomiscore2++;
                    lken.erase(itk);
                    lnaomi.erase(itn);
                    f=1;
                    break;
                }
            }
            if(f==0)
            {
                itn=lnaomi.begin();
                lnaomi.erase(itn);
                itk=lken.end();
                itk--;
                lken.erase(itk);
            }
        }
        cout<<"Case #"<<tc<<": "<<naomiscore2<<" "<<naomiscore1<<"\n";
    }
}
