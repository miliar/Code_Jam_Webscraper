#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <stdio.h>
using namespace std;
vector<double> a1,a2,b1,b2;
int T;

int main()
{

    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;

    for(int t=1;t<=T;t++)
    {

        a1.clear();
        a2.clear();
        b1.clear();
        b2.clear();

        int N;
        cin>>N;
        double n,max1=0,max2=0;

        for(int i=0;i<N;i++){
            cin>>n;
            a1.push_back(n);
            a2.push_back(n);
        }

        for(int i=0;i<N;i++){
            cin>>n;
            b1.push_back(n);
            b2.push_back(n);
            max1=max(max1,n);
            max2=max(max2,n);
        }

        sort(a1.begin(),a1.begin()+N);
        sort(a2.begin(),a2.begin()+N);
        sort(b1.begin(),b1.begin()+N);
        sort(b2.begin(),b2.begin()+N);
        int z=0,y=0;

        for(int i=0;i<N;i++){
            int now=-1;
            for(int k=0;k<b2.size();k++){
                if(a2[i]>b2[k]){
                    now=k;
                    y++;
                    break;
                }
            }
            if(now!=-1){
                b2.erase(b2.begin()+now);
            }
        }
        printf("Case #%d: ",t);

        printf("%d",y);

        while(a1.size()!=0){
            int now=0;
            for(int i=0;i<b1.size();i++){
                if(a1[0]<b1[i]){
                    now=i;
                    z++;
                    break;

                }
            }
            b1.erase(b1.begin()+now);
            a1.erase(a1.begin());

        }
        printf(" %d\n",N-z);


    }

}
