#include<bits/stdc++.h>
using namespace std;int main()
{
    freopen ("D-large.in","r",stdin);
    freopen ("output.txt","w",stdout);
    int t,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        int i,j,n,c1=0,c2=0,f=0;
        scanf("%d",&n);
        double*A,*B,*C;
        B=new double[n+50];
        A=new double[n+50];
        C=new double[n+50];
        for(i=0;i<n;i++)
        {
            scanf("%lf",&A[i]);
        }
        for(i=0;i<n;i++)
        {
            scanf("%lf",&B[i]);

        }
        sort(B,B+n);
        sort(A,A+n);
        for(i=0;i<n;i++) C[i]=B[i];

        for(i=0,j=0;i<n;i++)
        {
            if(A[i]>C[j])
            {
                c1++;
                j++;
            }
        }
        /*cout<<n<<endl;
        for(i=0;i<n;i++)
            cout<<A[i]<<" ";
        cout<<endl;
        for(i=0;i<n;i++)
            cout<<B[i]<<" ";
        cout<<endl;
        */
        for(i=0,j=0;i<n;i++)
        {
            for( ;j<n;j++)
            {
                if(A[i]<B[j])
                {
                    B[j]=0;
                    c2++;
                    break;
                }

            }
            if(j==n) break;
        }

        printf("Case #%d: %d %d\n",k,c1,n-c2);

    }
    fclose (stdout);
    fclose (stdin);
    return 0;
}
