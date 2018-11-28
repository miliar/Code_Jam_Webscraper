#include <iostream>
#include<cstdio>
#include<algorithm>
#include<string>


using namespace std;

int main(){

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i=1;
    int tst;
    cin>>tst;
    while(tst--){
    int x;
    int y[1010];
    cin>>x;
    for(int i=0;i<=x;i++)
        scanf("%1d",&y[i]);

    long long sum=0; int cnt=0;
    for(int i=0;i<=x;i++)
    {
        if(sum>=i)
            sum+=y[i];
        else if(y[i]>0)
        {
            cnt+=i-sum;
            sum+=y[i]+(i-sum);

        }
    }
    printf("Case  #%d: %d\n",i++,cnt);
    }
    return 0;

}
