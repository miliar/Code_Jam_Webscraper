#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    freopen("input2.txt","r",stdin);
    freopen("output2.txt","w",stdout);
    int t=0;
    long double c,f,x,rate,sum;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        cin>>c>>f>>x;
        rate=2.0;
        sum=0.0;
        while(1)
        {
            //dont add farm
            if((c/rate+x/(rate+f))>=x/rate){
                sum+=x/rate;
                break;
            }
            //add farm
            sum+=c/rate;
            rate+=f;
        }
        cout.precision(7);
        cout<<"Case #"<<test<<": "<<fixed<<sum<<endl;

    }
}
