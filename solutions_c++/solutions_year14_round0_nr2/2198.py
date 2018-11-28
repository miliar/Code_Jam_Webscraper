#include "cstdio"
#include "cstring"
#include "iostream"
#include "iomanip"

using namespace std;

int main(void)
{
    int t;
    scanf("%d",&t);
    for(int test = 1;test<=t;test++)
    {
        double c,f,x,ans,speed;

        ans = 0.0;
        speed = 2.0;
        
        cin >> c >> f >> x;
        
        while(true)
        {
            if((x/speed) <= (c/speed + x/(speed+f)))
            {
                ans += x/speed;
                break;
            }
            else
            {
                ans += c/speed;
                speed += f;
            }
        }
        
        printf("Case #%d: ",test);
        cout << fixed << setprecision(7) << ans << endl;
    }
    
    return 0;
}
