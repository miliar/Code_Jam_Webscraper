#include<iostream>
#include<cmath>
#include<cstdio>
using namespace std ;
int main()
{
    int t,t1=1;
    cin>>t ;
    FILE *p ;
    p=fopen("output.txt","w") ;
    while(t1<=t)
    {
        int a[6][6],b[6][6] ;
        int f=0 ;
        int i,j,r1,r2,ans=0 ;
        cin>>r1 ;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>a[i][j] ;
            }
        }
        cin>>r2 ;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>b[i][j] ;
            }
        }
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(a[r1][i]==b[r2][j])
                {
                    ans=a[r1][i] ;
                    f++ ;
                }
            }
        }
        if(f==1)
        {
            fprintf(p,"Case #%d: %d\n",t1,ans) ;
            //cout<<"Case #"<<t1<<": "<<ans<<"\n" ;
        }
        else if(f>1)
        {
            fprintf(p,"Case #%d: Bad magician!\n",t1) ;
            //cout<<"Case #"<<t1<<": Bad magician!\n" ;
        }
        else
        {
            fprintf(p,"Case #%d: Volunteer cheated!\n",t1) ;
            //cout<<"Case #"<<t1<<": Volunteer cheated!\n" ;
        }
        t1++ ;
    }
    return 0 ;
}
