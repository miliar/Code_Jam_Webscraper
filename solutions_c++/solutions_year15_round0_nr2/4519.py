#include <bits/stdc++.h>

using namespace std;
int p[100010],L[100010],R[100010];
void merge1(int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;
    for(i = 0; i < n1; i++)
        L[i] = p[l + i];
    for(j = 0; j < n2; j++)
        R[j] = p[m + 1+ j];

    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            p[k] = L[i];
            i++;
        }
        else
        {
            p[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < n1)
    {
        p[k] = L[i];
        i++;
        k++;
    }
    while (j < n2)
    {
        p[k] = R[j];
        j++;
        k++;
    }
}
void mergeSort(int l, int r)
{
    if (l < r)
    {
        int m = l+(r-l)/2;
        mergeSort( l, m);
        mergeSort( m+1, r);
        merge1(l, m, r);
    }
}
int main()
{
    freopen("1.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i,t,d,cas = 0,ans,x,cunt,cunt1;
    cin>>t;
    while(t--)
    {
        cas++;
        printf("Case #%d: ",cas);
        cin>>d;
        for( i=0 ; i<d ; i++ )   cin>>p[i];
        mergeSort(0,d-1);
        int ttt=p[d-1];
        ans = p[d-1]; cunt = 0;
        while(p[d-1]>2) {
            cunt++;
            int t1,t2;
            if(p[d-1]%2!=0) {
                t1 = p[d-1]/2+1;
                t2 = p[d-1]-t1;
                while(t1<2*t2-1&&t1>2&&t2>2) {
                    t1++;t2--;
                }
                if(t2!=ceil(t1/2.0)) {
                    t1 = p[d-1]/2+1;
                    t2 = p[d-1]-t1;
                }
                if(t2==ceil(t1/2.0)) {
                    if( p[d-2] == t1 || p[d-2] <= t2);
                    else {
                        t1 = p[d-1]/2+1;
                        t2 = p[d-1]-t1;
                    }
                }
            }
            else {
                t1=t2=p[d-1]/2;
            }
            p[d-1]=-1;
            for(i=d-2;i>=0;i--) {
                if(p[i]<=t1) {
                    ;break;
                }
                p[i+1]=p[i];
            }
            p[i+1]=t1;
            for(i=d-1;i>=0;i--) {
                if(p[i]<=t2) {
                    ;break;
                }
                p[i+1]=p[i];
            }
            p[i+1]=t2;
            d++;
            if(cunt+p[d-1]<ans) ans=cunt+p[d-1];
            if(cunt>=ttt) break;
        }
        printf("%d\n",ans);
    }
    return 0;
}
