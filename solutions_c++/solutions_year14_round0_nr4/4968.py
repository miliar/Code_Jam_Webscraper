#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
int t,n,l,i,j,win1,win2,m,flag;
float a1[1000],a2[1000];
cin>>t;
l=t;
while(t--)
{
    flag=win1=win2=0;
cin>>n;
    for(i=0;i<n;i++)cin>>a1[i];
    for(i=0;i<n;i++)cin>>a2[i];
   sort(a1,a1+n);
   sort(a2,a2+n);
   m=n;
for(i=0;i<n;i++)
{
    flag=0;
    for(j=0;j<m;j++)
    {
        if(a1[i]<a2[j])
        {
            swap(a2[j],a2[m-1]);m=m-1;sort(a2,a2+m);flag=1;break;
        }

    }
if(flag==0)
    {
                win2++;swap(a2[0],a2[m-1]);m=m-1;sort(a2,a2+m);

    }

}

sort(a1,a1+n);
   sort(a2,a2+n);
    for(j=0;j<n;j++)
    {

        if(a1[j]>a2[j])win1++;
        else {swap(a2[j],a2[n-1]);sort(a2+(j+1),a2+n);}

    }
cout<<"Case #"<<l-t<<": "<<win1<<" "<<win2<<endl;

}
return 0;
}
