#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <functional>

using namespace std;

int main()
{
    int i,j,k,l;
    int T,t;

    freopen("B-large.in","r",stdin);
    freopen("output-B.txt","w",stdout);

    cin>>T;
    for(t=1;t<=T;++t)
    {
        int N,M;
        int arr[200][200]={0};
        int maxC[200]={0},maxR[200]={0},minC[200]={0},minR[200]={0};
        bool ans=true;

        cin>>N>>M;

        for(i=0;i<N;++i)
        {
            for(j=0;j<M;++j)
            {
                cin>>arr[i][j];
                if(arr[i][j]>maxC[j])
                    maxC[j]=arr[i][j];
                if(arr[i][j]>maxR[i])
                    maxR[i]=arr[i][j];
                if(arr[i][j]<minC[j])
                    minC[j]=arr[i][j];
                if(arr[i][j]<minR[i])
                    minR[i]=arr[i][j];
            }
        }
        for(i=0;i<N;++i)
        {
            for(j=0;j<M;++j)
            {
                if(arr[i][j]==maxC[j]||arr[i][j]==maxR[i])
                    ;
                else
                {
                    ans=false;
                    break;
                }
            }
        }


        cout<<"Case #"<<t<<": "<<(ans==true?"YES":"NO")<<endl;
    }


    return 0;
}
