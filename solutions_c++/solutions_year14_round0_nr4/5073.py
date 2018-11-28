#include<iostream>
#include<algorithm>
using namespace std;
int compare(const void*a,const void *b)
{
    float *a1=(float *)a;
    float *b1=(float *)b;
    if((*a1-*b1)>0)
        return 1;
    else
        return 0;
}
int main()
{
    int t,l=0;
    cin>>t;
    while(t--)
    {
        l++;
        int n,i,j,w=0,dw=0;
        cin>>n;
        float a[n],b[n];
        for(i=0;i<n;i++)
            cin>>a[i];
        for(i=0;i<n;i++)
            cin>>b[i];
        qsort(a,n,sizeof(int),compare);
        qsort(b,n,sizeof(int),compare);
        for(i=0;i<n;i++)
            cout<<b[i];
        /*sort(a,a+n);
        sort(b,b+n);
        */i=0;j=0;
        while(j<n)
        {
            if(a[i]>b[j])
                j++;
            else
            {
                w++;
                i++;
                j++;
            }
        }
        w=n-w;
        i=0;j=0;
        while(i<n)
        {
                if(a[i]>b[j])
                {
                    dw++;
                    i++;j++;
                }
                else
                    i++;
        }
        cout<<"\nCase #"<<l<<": "<<dw<<" "<<w<<endl;
    }
    return 0;
}
