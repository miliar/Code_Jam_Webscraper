#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("A-small-attempt1.txt", "w", stdout);
    int t,t_c,fst_r,scnd_r,i,j,k,l,a[10][10],m,n,f_s[10],s_s[10];
    cin>>t_c;
    for(t=1;t<=t_c;t++)
    {
        cin>>fst_r;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
             cin>>a[i][j];
        }
        for(i=0;i<4;i++) f_s[i]=a[fst_r-1][i];
        cin>>scnd_r;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
             cin>>a[i][j];
        }
        for(i=0;i<4;i++) s_s[i]=a[scnd_r-1][i];
        int count=0,ans;
         for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)

             {
                 if(f_s[i]==s_s[j])
                 {
                     count++;
                     ans=f_s[i];
                 }
             }
        }
        if(count==1) printf("Case #%d: %d\n",t,ans);
        else if(count>1) printf("Case #%d: Bad magician!\n",t);
        else if(!count) printf("Case #%d: Volunteer cheated!\n",t);
    }
    return 0;
}
