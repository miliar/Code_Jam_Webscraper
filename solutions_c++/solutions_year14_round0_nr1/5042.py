#include<iostream>
#include <algorithm>
#include"stdlib.h" 
using namespace std;
int cmp(const void*,const void*);
int main()
{
    int T,a[4][4],b[4][4],k,m,j,l,c,p;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
            cin>>k;k--;
            for(j=0;j<4;j++)
            for(l=0;l<4;l++)
            {cin>>a[j][l];   }
            qsort(a[k],4,sizeof(int),&cmp);
            //sort(a[k],a[k]+4);
            cin>>m;m--;
            for(j=0;j<4;j++)
            for(l=0;l<4;l++)
            {cin>>b[j][l];}
            qsort(b[m],4,sizeof(int),&cmp);
            c=0;
            for(j=0,l=0;j<4&&l<4;)
            {
                    if(a[k][j]>b[m][l]) {l++; continue;}
                    if(a[k][j]==b[m][l]) {c++; p=a[k][j]; l++;j++; continue;}
                    if(a[k][j]<b[m][l]) {j++; continue;}
            }
            switch(c)
            {
                     case 0: cout<<"Case #"<<i<<": Volunteer cheated!\n"; break;
                     case 1:cout<<"Case #"<<i<<": "<<p<<endl; break;
                     default:cout<<"Case #"<<i<<": Bad magician!\n"; break;
            }
    }
    return 0;
}
int cmp ( const void *a , const void *b )
{
return *(int *)a - *(int *)b;
}
