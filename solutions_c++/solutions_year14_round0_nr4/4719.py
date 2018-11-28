#include <iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("xyzout5.txt","w",stdout);

    int t;
    cin>>t;
    for(int test=1;test<=t;test++)
{
        int n;
        cin>>n;
        double na[n],ke[n];
        for(int i=0;i<n;i++)cin>>na[i];
        sort(na,na+n);
        for(int i=0;i<n;i++)cin>>ke[i];
        sort(ke,ke+n);


        //cin>>blocks;
        int res1=0,res2=0;
        int curr_posna=n-1;
        int curr_posk=n-1;
        for(int i=n-1;i>=0;i--)
        {
            if(na[curr_posna]>ke[curr_posk])
            {
                res1++;
                curr_posna--;
            }
            else
            {
                curr_posk--;
                curr_posna--;
            }
        }





        int x1=0,x2=0;
for(int i=0;i<n;i++)
{


if(na[x1]>ke[x2])
{
res2++;
x1++;
x2++;
}
else
x1++;
}
cout<<"Case #"<<test<<": "<<res2<<" "<<res1<<endl;
}
fclose(stdin);
    fclose(stdout);
return 0;
}
