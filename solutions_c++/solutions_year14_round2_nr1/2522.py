#include<bits/stdc++.h>
#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define p(n) printf("%d\n",n)
#define mod 1000000007
#define ll long long
using namespace std;
int main()
{
    char str[101][102];
    char str1[102];
    int fre[101][101];
    int t,k,n,i,f,j,len;
    ifstream f1("input.txt");
    ofstream f2("output3.txt");
    cin>>t;
    for(k=1;k<=t;++k)
    {
        f=1;
        for(i=0;i<=100;++i)
        {

            for(j=0;j<=100;++j)
            {

                fre[i][j]=0;
            }
        }
        cout<<"Case #"<<k<<": ";
        int n;
        cin>>n;
        for(i=1;i<=n;++i)
            scanf(" %s",&str[i]);
            int ct;

        ct=0;
        str1[ct]=str[1][0];
        fre[1][ct]++;

        for(i=1;i<strlen(str[1]);++i)
        {
            if(str[1][i]!=str[1][i-1])
            {
                ct++;
                str1[ct]=str[1][i];

                fre[1][ct]++;
            }
            else{
                fre[1][ct]++;
            }
        }
        len=ct;
       // cout<<str1<<endl;
        for(i=2;i<=n;++i)
        {
            ct=0;
            if(str[i][0]!=str1[0])
            {
                f=0;
                break;
            }
            else{
                    fre[i][ct]++;

            }
            for(j=1;j<strlen(str[i]);++j)
            {
                if(str[i][j]!=str[i][j-1])
                {
                    ct++;
                    if(str[i][j]!=str1[ct])
                    {
                        f=0;
                        break;
                    }
                    else
                    fre[i][ct]++;
                }
               else{
                fre[i][ct]++;
                 }
            }
            if(ct!=len)
            {

                f=0;
                break;
            }
        }
            if(f==0)
                cout<<"Fegla Won\n";
            else{

               int ans=0;

                int tmp;
                for(i=0;i<=len;++i)
                {
                	int ans1=INT_MAX;
                    int minm,maxm;
                    minm=INT_MAX;
                    maxm=0;
                    for(j=1;j<=n;++j)
                    {
                       minm=min(minm,fre[j][i]);
                       maxm=max(maxm,fre[j][i]);
                    }

                   for(tmp=minm;tmp<=maxm;++tmp)
                   {

                     int ans2=0;
                        for(j=1;j<=n;++j)
                       {
                       ans2=ans2+abs(tmp-fre[j][i]);
                        }
                        ans1=min(ans1,ans2);
                    }
                    ans=ans+ans1;

                    }
                     cout<<ans<<endl;
                }


            }



    return 0;
}
