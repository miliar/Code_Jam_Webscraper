#include<bits/stdc++.h>
using namespace std;

#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

#define ll long long
#define ull unsigned ll

bool valid(int arr[30],int sum)
{
    //printf("CHeck Arr\n");
    //for(int i=0;i<30;i++)
   //     printf("%d ",arr[i]);
   // cout<<endl;
    for(int i=0;i<30;i++)
    {
        if(arr[i]>sum/2)
        return false;
    }
    return true;

}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
        int num[30],num2[30];
        vector<string> res;
        string temp="";
        int n;
        int sum=0;
        scanf("%d",&n);
        for(int i=0;i<30;i++)
        {
            num[i]=0;
            num2[i]=0;
        }
        for(int i=0;i<n;i++)
        {
            scanf("%d",&num[i]);
            sum += num[i];
        }
       // for(int i=0;i<30;i++)
        //    printf("num[%d]: %d\n",i,num[i]);
        while(sum>0)
        {
            temp="";
            int m1,m2;
            m1=-1;
            m2=-1;
            for(int i=0;i<30;i++)
            {
                if(m1==-1||num[i]>=num[m1])
                {
                    m2 = m1;
                    m1 = i;
                }
                else if(m2==-1 || num[i]>num[m2])
                {
                    m2 = i;
                }
            }
            if(num[m1]-1>num[m2])
            m2 = m1;

            for(int i=0;i<30;i++)
            num2[i]=num[i];
            num2[m1]--;
            num2[m2]--;
            if(valid(num2,sum-2))
            {

                temp.push_back(m1+'A');
                temp.push_back(m2+'A');
                res.push_back(temp);
                num[m1]--;
                num[m2]--;
                sum-=2;
            }
            else
            {

                temp.push_back(m1+'A');
                res.push_back(temp);
                num[m1]--;
                sum--;
            }
           // cout<<"test "<<m1<<" "<<m2<<endl;
           // cout<<temp<<endl;
        }
        printf("Case #%d: ",tt);
        for(int i=0;i<res.size();i++)
        printf("%s ",res[i].c_str());
        printf("\n");

    }
    return 0;
}
