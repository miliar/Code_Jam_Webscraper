#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
using namespace std;
#include <stdio.h>
#include <iostream>
#include <cstring>
using namespace std;
bool takena[1200];
bool takenb[1200];
double help[1200];
double a[1200];
double b[1200];
int m;

int firstbiggest(double array[],bool taken[],double value)
{
    for(int i=0; i<m; i++)
        if(array[i]>value && taken[i])
            return i;
    return -1;
}

int getsmallest(double array[],bool taken[])
{
    for(int i=0; i<m; i++)
        if(taken[i])
            return i;
    return -1;
}
int getbiggest(double array[],bool taken[])
{
    for(int i=m-1; i>=0; i--)
        if(taken[i])
            return i;
    return -1;
}

int war()
{
    memset(takena, true, sizeof(takena));
    memset(takenb, true, sizeof(takenb));

    int ret=0;
    int j=m-1;

    int naomi,ken;
    double x,y;

    for(int i=0; i<m; i++)
    {
        ken=firstbiggest (b,takenb,a[i]);
        if(ken!=-1)
        {
            takenb[ken]=false;
        }
        else
        {
            ken=getsmallest(b,takenb);
            takenb[ken]=false;
            ret++;
        }
        takena[i]=false;
    }
    return ret;
}

int decitfulwar()
{
    memset(takena, true, sizeof(takena));
    memset(takenb, true, sizeof(takenb));

    int ret=0;
    int j=m-1;

    int naomi,ken;
    double x,y;

    for(int i=0; i<m; i++)
    {
        x=b[j];
        naomi=getbiggest(a,takena);

        if(a[naomi]>b[j])
        {
            ret++;
            takena[naomi]=false;
        }
        else
        {
            naomi=getsmallest(a,takena);
            takena[naomi]=false;
        }
        takenb[j]=false;
        j--;
    }
    return ret;
}

void merge(int s,int e,double array[])
{
    int mid=(e-s)/2;
    mid=mid+s;
    int p1=s;
    int p2=mid+1;
    int mainp=s;

    for(int i=s;i<=mid;i++)
        help[i]=array[i];

    while(mainp<=e)
    {
        if(p1>mid)
        {
            array[mainp]=array[p2];
            p2++;
            mainp++;
            continue;
        }

        if(p2>e)
        {
            array[mainp]=help[p1];
            p1++;
            mainp++;
            continue;
        }

        if(help[p1]<array[p2])
        {
            array[mainp]=help[p1];
            p1++;
        }
        else
        {
            array[mainp]=array[p2];
            p2++;
        }
        mainp++;
    }
    return ;
}

void merge_sort(int s,int l,double array[])
{
    if(s>=l)
        return;

    int mid=(l-s)/2;
    mid=s+mid;
    merge_sort(s,mid,array);
    merge_sort(mid+1,l,array);
    merge(s,l,array);
    return;
}



int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("output.out","w",stdout);

    int cases,p=1;
    scanf("%d",&cases);
    while(cases--)
    {
        scanf("%d",&m);

        for(int i=0; i<m; i++)
            cin>>a[i];

        for(int i=0; i<m; i++)
            cin>>b[i];


        merge_sort(0,m-1,a);
        merge_sort(0,m-1,b);

        printf("Case #%d: ",p);
        printf("%d %d\n",decitfulwar(),war());

        p++;
    }
    return 0;
}



/*
bool compare_as_ints (double i,double j)
{
  return ((i)<(j));
}
bool compare_ints (double i,double j)
{
  return ((i)>(j));
}

int main()
{
    // freopen("D-small-attempt0.in","r",stdin);
    //freopen("output.out","w",stdout);
    int n,c=0,cs=1,kz,ctmp=0;
    double t;
    //double a[10],b[10];
    cin>>kz;
    while(kz--)
    {
    vector<double>a,b,tmp;
    cin>>n;
    for(int i=0;i<n;cin>>t,a.push_back(t),i++);
    for(int i=0;i<n;cin>>t,b.push_back(t),tmp.push_back(t),i++);
stable_sort (a.begin(), a.end(), compare_as_ints);
stable_sort (tmp.begin(), tmp.end(), compare_as_ints);
stable_sort (b.begin(), b.end(), compare_ints);
    //qsort (values, 6, sizeof(int), compare);
    for(int i=0;i<n;cout<<a[i++]<<" ");
    cout<<"\n";
    for(int i=0;i<n;cout<<b[i++]<<" ");
    cout<<"\n";
    for(int i=0;i<n;i++){
        if(a[i]>b[i])c++;
        if(a[i]>tmp[i]) ctmp++;}
      cout<<"Case #"<<cs++<<": ";
      if(c>=ctmp)
    cout<<c<<" "<<c/2<<"\n";
    else
        cout<<ctmp<<" "<<ctmp/2<<"\n";
    c=0,ctmp=0;
    }
    return 0;
}

bool compare_as_ints (double i,double j)
{
  return ((i)<(j));
}
bool compare_ints (double i,double j)
{
  return ((i)>(j));
}

int main()
{
     freopen("D-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int n,c=0,cs=1,kz,ctmp=0;
    double t;
    //double a[10],b[10];
    cin>>kz;
    int s=0;
    while(kz--)
    {
        bool flgs[100];
    vector<double>a,b,tmp;
    cin>>n;
    for(int i=0;i<n;cin>>t,a.push_back(t),i++);
    for(int i=0;i<n;cin>>t,b.push_back(t),tmp.push_back(t),i++);
stable_sort (a.begin(), a.end(), compare_ints);
stable_sort (b.begin(), b.end(), compare_ints);
for(int i=0;i<n;i++)
 if(a[i]>b[i]&&!flgs[i])cout<<a[i]<<" "<<b[i]<<"\n", s++,flgs[i]=1;
 else
 {
    for(int j=i+1;j<n;j++)
          if(a[i]>b[j] &&!flgs[j]){cout<<a[i]<<" "<<b[i]<<"\n",s++;flgs[j]=1; break;}
 }
 cout<<s<<"-------------------\n";
   s=0;
   }
    return 0;
}
*/
