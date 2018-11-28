#include <iostream>
#include <vector>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, n;
    cin >> t;
    for(int c=1; c<=t; c++)
    {

        vector<bool> digits(10,false);
        int seen=0;
        cin >> n;

        printf("Case #%d: ", c);
        if(n == 0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        int temp = 0;
        while(seen < 10)
        {
            temp += n;
            int aux = temp;
            while(aux)
            {
                int d = aux %10;
                if(!digits[d])
                {
                    digits[d] = true;
                    seen++;
                }
                aux/=10;
            }
        }
        printf("%d\n", temp);
    }
    return 0;
}
