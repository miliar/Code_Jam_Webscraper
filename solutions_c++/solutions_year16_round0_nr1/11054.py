#include <iostream>
#include <math.h>
using namespace std;

struct ret_digits
{
    public:
    int arry[10];
};

ret_digits get_dig(int n)
{
    int iter,nn;

    ret_digits out;
    nn=n;
    iter = floor(log10(n))+1;
    for (int i=0;i<iter;i++)
    {
        out.arry[i] = nn%10;
        nn = nn/10;
    }
    return out;


}
int chek_digit(int dig[])
{
    int cont_1;
    for (int jj=0;jj<10;jj++)
    {
        if (dig[jj]==1)
        {
            cont_1++;
        }
    }
    if (cont_1==10)
    {
        return 1;
    }
    else
    {
        return 0;
    }

}






int main()
{
    int t,n,digit[10],mul,num,small=200,dig_no,result,large=1000000;
    ret_digits get_digits;

    cin >> t ;
    for (int i=1;i<=t;i++)
    {
        cin >> n;
        for (int bog=0;bog<10;bog++)
        {
            digit[bog]= -1;
        }
        mul = 1;
        if(n<=large)
        {
            if (n==0)
            {
                cout << "Case #" << i << ":" << " " << "INSOMNIA" << endl;
            }
            else
            {
                while(!chek_digit(digit))
                {
                    num = mul * n;
                    get_digits = get_dig(num);
                    dig_no = floor(log10(num))+1;
                    for (int jj=0;jj<dig_no;jj++)
                    {
                        digit[get_digits.arry[jj]] = 1;
                        //cout << get_digits.arry[jj];
                    }
                    mul++;

                }
                result = num;
                cout << "Case #" << i << ":" << " " <<result << endl;

            }



        }
    }
}

