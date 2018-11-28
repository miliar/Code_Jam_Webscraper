#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

double a[1010],b[1010];
int main()
{
    int t;
    //freopen("d.in","r",stdin);
   // freopen("d.out","w",stdout);
    cin >> t;
    for(int cas=1;cas<=t;cas++)
    {
        printf("Case #%d: ",cas);
        int n;
        cin >> n;
        for(int i=0;i<n;i++)
            cin >> a[i];
        for(int i=0;i<n;i++)
            cin >> b[i];
        sort(a,a+n);
        sort(b,b+n);
        int ans1=0,ans2=0;
        int p=0,q=0;
        while(p<n)
        {
            while(p<n)
            {
                if(a[p]>b[q])break;
                p++;
            }
            if(p!=n){
            ans1++;
            p++;
            q++;
        }
        }
        int j=0,i=0;
        while(i<n)
        {
           while(i<n)
           {
               if(a[j]<b[i])break;
               ans2++;
               i++;
           }
           if(i!=n){
           i++;
           j++;
        }
    }
        cout << ans1 <<" " << ans2 << endl;
    }
    //fclose(stdin);
    //fclose(stdout);
    return 0;
}
