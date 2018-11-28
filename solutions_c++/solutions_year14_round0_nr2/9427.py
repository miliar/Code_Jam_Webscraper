#include <iostream>
#include  <iomanip>
using namespace std;

int main()
{
    double c,f,x,t[10001][3],rate=2.0,rate2,sum,sum2,ans[10001];
    int i,j,n;
    cin>>n;

    for(j=1;j<=n;j++){
        cin>>c;
        cin>>f;
        cin>>x;
        rate=2.0;
        ans[1]=x/2.0;
        t[1][1]=c/rate;
        t[1][2]=x/rate;
        sum=t[1][1];

        for(i=2;i<=10000;i++){
            rate=rate+f;
            t[i][1]=c/rate;
            t[i][2]=x/rate;
            ans[i]=sum+t[i][2];
            sum=sum+t[i][1];
        }
        double min=ans[1];
        for(i=2;i<=10000;i++){
            if(ans[i]<min){
                min=ans[i];
            }
        }
        cout<<"Case #"<<j<<": ";
            std::cout <<fixed << std::setprecision(7) <<min<<endl;
    }
    return 0;
}

/*
int main()
{
    double c,f,x,t[10000][3],rate=2.0,rate2,sum,sum2;
    int i,j,n;
    cin>>n;

    for(j=1;j<=n;j++){
        cin>>c;
        cin>>f;
        cin>>x;
        rate=2.0;
        //start with rate 2
        if(x/rate<=c/rate){
            cout<<"Case #"<<j<<": ";
            std::cout <<fixed << std::setprecision(7) <<x/2.0<<endl;
        }else{
            i=2;
            rate=2.0;
            t[1][1]=c/rate;
            t[1][2]=x/rate;
            sum=t[1][1];
            int run=1;
            while(run){
                rate=rate+f;
                t[i][1]=c/rate;
                t[i][2]=x/rate;
                //cout<<t[i][1]<<" | "<<t[i][2]<<endl;
                if(sum+t[i][2]<sum+t[i][1]+(x/(rate+f))){
                    run=0;
                    cout<<"Case #"<<j<<": ";
                    std::cout <<fixed << std::setprecision(7) <<sum+t[i][2]<<endl;
                }
                sum=sum+t[i][1];
                i++;
            }
        }
    }
    return 0;
}
*/
