#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    int test=1,t,n,answ,ansd,i,j;
    cin>>t;
    while(test<=t)
    {
        answ=ansd=0;
        cin>>n;
        double naomi[n+1],ken[n+1];
        for(i=0;i<n;i++)
            cin>>naomi[i];
        for(i=0;i<n;i++)
            cin>>ken[i];
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        i=j=0;
        while(i<n && j<n)
        {
            if(naomi[i]>ken[j])
                i++,j++,ansd++;
            else i++;
        }
        i=j=0;
        answ=n;
        while(i<n && j<n)
        {
            if(naomi[i]<ken[j])
            {
                i++,j++;
                answ--;
            }
            else j++;
        }
        cout<<"Case #"<<test<<": "<<ansd<<" "<<answ<<endl;;
        test++;
    }
}
