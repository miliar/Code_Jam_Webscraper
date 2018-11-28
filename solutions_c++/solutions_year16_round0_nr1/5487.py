#include<bits/stdc++.h>
using namespace std;
bool check (bool pen[])
{
    for (int i=0;i<=9;i++)
        if (pen[i] == true) return true;
    return false;
}


int main()
{
    int n,c;
    scanf("%d",&n);
    ofstream out_data("AsmOUT.dat");
    for (c=1;c<=n;c++)
    {
        long long int num,ans,aux;
        int dig;
        bool pen[10] = {true,true,true,true,true,true,true,true,true,true};
        scanf ("%lld",&num);
        ans = num;
        if (!num)
        {
            out_data << "Case #" << c << ": INSOMNIA" << endl;
        }
        else
        {
            while (true)
            {
                aux = ans;
                while (aux)
                {
                    dig = aux%10;
                    pen[dig] = false;
                    aux = aux/10;
                }
                if (!check(pen)) 
                    break;
                ans += num;
            } 
            out_data << "Case #" << c << ": " << ans << endl;
        }
    }
    return 1;

}
