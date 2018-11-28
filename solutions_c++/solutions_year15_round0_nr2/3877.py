#include <bits/stdc++.h>

using namespace std;
int p[100010],L[100010],R[100010];
//set<int> p;
void merge1(int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;

    /* create temp arrays */
    //int L[n1], R[n2];

    /* Copy data to temp arrays L[] and R[] */
    for(i = 0; i < n1; i++)
        L[i] = p[l + i];
    for(j = 0; j < n2; j++)
        R[j] = p[m + 1+ j];

    /* Merge the temp arrays back into arr[l..r]*/
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

    /* Copy the remaining elements of L[], if there are any */
    while (i < n1)
    {
        p[k] = L[i];
        i++;
        k++;
    }

    /* Copy the remaining elements of R[], if there are any */
    while (j < n2)
    {
        p[k] = R[j];
        j++;
        k++;
    }
}

/* l is for left index and r is right index of the sub-array
  of arr to be sorted */
void mergeSort(int l, int r)
{
    if (l < r)
    {
        int m = l+(r-l)/2; //Same as (l+r)/2, but avoids overflow for large l and h
        mergeSort( l, m);
        mergeSort( m+1, r);
        merge1(l, m, r);
    }
}
int main()
{
    freopen("in2.in","r",stdin);
    freopen("out3.out","w",stdout);
    int i,t,d,cas = 0,ans,x,cunt,cunt1;
    cin>>t;
    while(t--)
    {
        cas++;
        printf("Case #%d: ",cas);
        cin>>d;
        for( i=0 ; i<d ; i++ )   cin>>p[i];
        mergeSort(0,d-1);
        //cout<<endl;for( i=0 ; i<d ; i++ )   cout<<p[i]<<" ";cout<<endl;
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
                //if(p[d-1]==7) cout<<t1<<t2;
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
        }
        printf("%d\n",ans);
    }
    return 0;
}
