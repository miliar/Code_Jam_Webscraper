#include<bits/stdc++.h>


using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out1small.txt","w",stdout);
    int t,tc=1,k,i;
    char a[10005];
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %s",&k,a);
        int sum=0,add=0,res=0;
        for(i=0;i<=k;i++){
            if(i>sum){
                //cout<<"here\n";
                add=i-sum;
                res=res+add;
                sum=sum+add;
                sum=sum+(a[i]-'0');
            }
            else{
                sum=sum+(a[i]-'0');
               // cout<<sum<<endl;
            }
        }
        printf("Case #%d: %d\n",tc++,res);

    }

    return 0;
}
