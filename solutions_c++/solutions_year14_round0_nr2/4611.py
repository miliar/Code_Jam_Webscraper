#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
int test;
cin>>test;
int z = 0;
while(test--)
{
    double c,f,x;
    cin>>c>>f>>x;
    double cookies = 0.0;
    double rate = 2.0;
    double time1 = 0.0;
    double time2 = 0.0;
    double time3 = 0.0;
    double ans = 0.0;
    time1 = x / rate;
    while(true)
    {
        
        time2 = time2 + c / rate;
        rate = rate + f;
        time3 = x / rate;
        if(time2 + time3 < time1)
            {
                time1 = time2 + time3;

            }
        else
            break; 
    }
    z++;
    cout<<"Case #"<<z<<": ";
    printf("%.7lf",time1);
    cout<<endl;
}
//system("pause");
return 0;
}
