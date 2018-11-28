#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<iostream>


using namespace std;


#define FRO freopen("in.txt","r",stdin);
#define FRU freopen("out_wa.txt","w",stdout);




#define infinity 2147483647
#define pi 3.14159265358979323846
#define eps 1e-9



#define foreach(i,n) for(__typeof((n).begin())i =(n).begin();i!=(n).end();i++)
#define all(a) (a).begin(),(a).end()
#define in(n,a,b) ( n>=a && n<=b )




template< class T > T Min(T a, T b) { return a<b?a:b; }


#define Limit 10004

double C,F,X;

double rec(double curTime, double curPro, double rest)
{
    double re=C/curPro;
    if(re)return re=re+rest/curPro;

    re += C/curPro;
    return re=rec(re,curPro+F,rest-C);
}


double tb[Limit];

double dp(double curPro, int curStage)
{
    if(tb[curStage]>-1)return tb[curStage];
    if(curPro>C)return tb[curStage]=1.0;

    return tb[curStage] = C/curPro + dp(curPro+F,curStage+1);
}


int main()
{
    FRO
    FRU
    int tc,t=1,i,j,k,a,b,c,d;

double yqTestRt[Limit],yqUp2By[Limit],test[Limit];
int n;

    cin>>tc;
    for(t=1;t<=tc;t++)
    {
        cin>>C>>F>>X;

        for(i=0;i<Limit;i++)tb[i]=-1.0;
        dp(2.0,0);

        double yqTestRt[Limit],x;
        x=yqTestRt[0]=2.0;
        for(i=1;x<X;i++)
        {
            x=yqTestRt[i]=yqTestRt[i-1]+F;
        }
j=i;
//cout<<x<<endl;

        double costToBuy[Limit],costToComplete[Limit];
        costToBuy[0]=costToComplete[0]=C/2.0;
        for(i=1;i<j;i++)
        {
            costToBuy[i]=C/yqTestRt[i]+costToBuy[i-1];
            costToComplete[i]=X/yqTestRt[i];
        }

        double sum=0.0;
        for(i=0;i<j;i++)
        {
            if(costToBuy[i]+costToComplete[i+1]>costToComplete[i])
            {
                sum+=costToComplete[i];     a=i;
                break;
            }
            sum+=costToBuy[i];
            //cout<<sum<<endl;
        }


        yqTestRt[0]=2.0;
        for(i=1;yqTestRt[i-1]<=X;i++)yqTestRt[i]=yqTestRt[i-1]+F;
        n=i-1;              // cout<<n<<endl;

        yqUp2By[0]=0.0;
        for(i=1;i<n;i++)yqUp2By[i]=yqUp2By[i-1]+C/yqTestRt[i-1];
        for(i=0;i<n;i++)test[i]=yqUp2By[i]+X/yqTestRt[i];


//for(i=0;i<n;i++)cout<<yqUp2By[i]<<" ";


        //for(i=0;i<n;i++)cout<<i<<" "<<test[i]<<endl;
        double ans=infinity*1.0;
        for(i=0;i<n;i++)ans=Min(ans,test[i]);           //cout<<i<<endl;
        printf("Case #%d: %.7lf\n",t,ans);

/*
        for(i=0;i<j;i++)cout<<i<<" "<<
        tb[i]<<" "<<
        yqTestRt[i]<<" "<<
        tb[i]-tb[i+1]<<" "<<
        costToBuy[i]<<" "<<
        //X/yqTestRt
        costToComplete[i]<<endl;
*/


//        printf("Case #%d: %.7lf\n",t,rec(0.0,2.0,X));
    }
    return 0;
}

