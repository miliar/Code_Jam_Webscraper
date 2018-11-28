#include<bits/stdc++.h>
#define MAX 10005
using namespace std;
bool check(pair<int,int> a[],int n,int v,int total)
{
    int i;
    if(a[n-1].first==1 && total%2==1)
        return false;

    if(v==1)
    {
        for(i=0;i<n;i++)
        {
            if(a[i].first>0)
            {
                if((total-a[i].first-1)<(a[i].first-1))
                    return false;
            }
        }
    }
    else
    {
        for(i=0;i<n-1;i++)
        {
            if(a[i].first>0)
            {
                if((total-a[i].first-2)<(a[i].first))
                    return false;
            }
        }
    }
    return true;
}
int main()
{
    FILE *fr , *fw;
    fr=fopen("in.txt","a+");
    fw=fopen("out.txt","w+");
    int t;
    fscanf(fr,"%d",&t);
    for(int k=1;k<=t;k++)
    {
        int n,i,j;
        fscanf(fr,"%d",&n);
        //cout<<t<<"\t"<<n<<"\n";
        pair<int,int> a[n];
        int total=0;
        for(i=0;i<n;i++)
            fscanf(fr,"%d",&a[i].first),a[i].second=i,total+=a[i].first;

        fprintf(fw,"Case #%d: ",k);

        while(1)
        {
            if(total==0)
                break;
            sort(a,a+n);
            if(a[n-1].first==a[n-2].first && a[n-1].first>0 && check(a,n,1,total))
            {
                total-=2;
                fprintf(fw,"%c%c ",'A'+a[n-1].second,'A'+a[n-2].second);
                a[n-1].first--;
                a[n-2].first--;
            }
            else if(a[n-1].first>1 && check(a,n,2,total))
            {
                total-=2;
                fprintf(fw,"%c%c ",'A'+a[n-1].second,'A'+a[n-1].second);
                a[n-1].first-=2;
            }
            else if(a[n-1].first>0)
            {
                total--;
                fprintf(fw,"%c ",'A'+a[n-1].second);
                a[n-1].first--;
            }


        }
        fprintf(fw,"\n");

    }
    fclose(fw);
    fclose(fr);
    return 0;
}
