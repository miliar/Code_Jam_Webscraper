#include<bits/stdc++.h>

using namespace std;

int main()
{
    ofstream oyf("yes.txt");
    ifstream myf("sam.txt");
    if(myf.is_open()){
    int t,x=1;
    myf>>t;
    while(t--)
    {
        int n,i,c=0,j,ans1,ans2;
        myf>>n;
        int flag[1001]={0},flag1[1001]={0};
        double a[n],b[n];
        for(i=0;i<n;i++)
            myf>>a[i];
        for(i=0;i<n;i++)
            myf>>b[i];
        sort(a,a+n);
        sort(b,b+n);
        int idx=n-1;
        for(i=0;i<n;i++){
            int chk=0;
            for(j=0;j<n;j++)
            {
                if(a[i]>b[j] && flag1[j]==0)
                {
                    flag1[j]=1;
                    c++;
                    chk=1;
                    break;
                }
            }
            if(chk==0)
                flag1[idx--]=1;
        }
        ans1=c;
        c=0;
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
            {
                if(a[i]<b[j] && flag[j]==0)
                {
                    flag[j]=1;
                    c++;
                    break;
                }
            }
        //cout<<c<<endl;
        ans2=n-c;
        oyf<<"Case #"<<x++<<": "<<ans1<<" "<<ans2<<endl;
    }}
    return 0;
}
