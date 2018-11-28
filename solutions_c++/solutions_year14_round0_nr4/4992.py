#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
double A[1001];
int main()
{
    int T;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        int N;
        cin>>N;
        double g[N];
        double b[N];
        double b1[N];
        int k;
        for( k=0;k<N;k++)
        cin >>g[k];
        for(k=0;k<N;k++)
        cin>>b[k];
        for(k=0;k<N;k++)
        b1[k]=b[k];
        sort(g,g+N);
        sort(b,b+N);
        sort(b1,b1+N);
        int cnt=0;
      // for(int m=0;m<N;m++)
       //cout <<b1[m]<<endl;
        for(int m=0;m<N;m++)
        {
            for(int l=0;l<N;l++)
            {
                if(g[m]<b[l]){
                cnt++;
                b[l]=0.0;
                break;
                }
            }
        }
        //cout <<N-cnt<<endl;
        //for(int m=0;m<N;m++)
        //{
        //	cout <<g[m]<<b1[m]<<endl;
        //}
        int cnt1=0;
        int p1=0;
        int p2=N-1;
        for(int m=0;m<N;m++)
        {
                if(g[m]<b1[p1]&&g[m]<b1[p2]){
                --p2;
                //cout <<p2<<endl;
                }
                else if(g[m]<b1[p2]&&g[m]>b1[p1]){
                ++p1;
                cnt1++;
                }
                else if(g[m]>b1[p1] &&g[m]>b1[p2]){
                  ++p1;
                    cnt1++;
        }

        }
       cout <<"Case #"<<i<<":  "<<cnt1 <<" "<<N-cnt<<endl;
        //cout <<p1<<p2<<endl;
    }
    return 0;
}
