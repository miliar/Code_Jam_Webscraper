#include<iostream>
#include <iomanip>
using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

    int T;
    cin>>T;
    double c,f,x;
    double min;
    double now_farm_price,cost_on_farm,all_cost;
    double now_produce;

    cout<<fixed;
    for(int i=1;i<=T;i++)
    {
        cin>>c>>f>>x;
        min = x/2;

        now_produce = 2;
        now_farm_price = c/2;

        cost_on_farm = now_farm_price;
        for(;cost_on_farm<min; cost_on_farm += now_farm_price)
        {
            now_produce += f;
            all_cost = x/now_produce + cost_on_farm;
            if(all_cost < min)
                min = all_cost;
            else
                break;

            now_farm_price = c/now_produce; //现在买农场的时间
        }
        cout<<setprecision(7)<<"Case #"<<i<<": "<<min<<endl;
    }
}
