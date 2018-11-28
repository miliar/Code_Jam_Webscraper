//http://www.cplusplus.com/forum/windows/10436/
#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
    int T,i;
    double C,F,X,rate,sum,initial,temp,answer;
    cin>>T;
    for(i=1;i<=T;i++)
    {
        cin>>C>>F>>X;
        cout<<"Case #"<<i<<": ";
        rate=2;
        initial=X/rate;
        sum=C/rate;
        temp=X/(rate+F);
        answer=sum+temp;
        if(initial<answer)
        {
            cout<<setprecision(10)<<initial<<endl;
        }
        else
        {
            while(1)
            {
                rate+=F;
                sum+=(C/rate);
                temp=X/(rate+F);
                if(answer<(sum+temp))
                   break;
                else
                    answer=sum+temp;
            }
            cout<<setprecision(10)<<answer<<endl;
        }
    }
    return 0;
}
