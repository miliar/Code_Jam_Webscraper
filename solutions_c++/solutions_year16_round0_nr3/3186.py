#include<iostream>
#include<math.h>
#include<vector>
using namespace std;
long int prime_check(long int number)
{
    long int divisor=0;
    for(long int i=2; i<sqrt(number)+2; i++)
    {
        if(number%i==0)
        {
            divisor=i;
            break;
        }
    }
    return divisor;
}
long int get_base_value(long int number,long int base,int max_bit)
{
    if(base==2)return number;
    else
    {
        long int base_value=0;
        for(int i=0; i<max_bit; i++)
        {
            if((number>>i)&1)base_value += pow(base,i);
        }
        return base_value;
    }
}
void print_bits(long int number,int max_bit)
{
    long int refnum=(1<<(max_bit-1));
    for(int i=0; i<max_bit; i++)
    {
        if((refnum & (number<<i)) != 0)cout<<1;
        else cout<<0;
    }
}
class jamcoin
{
    long int coin,divisors[9];
    int max_bit;
public :
    jamcoin(long int newcoin,int n)
    {
        coin = newcoin;
        max_bit = n;
    };
    bool check_validity();
    void print();
};
bool jamcoin::check_validity()
{
    bool validity=true;
    long int base_value;
    for(int base=2; base<=10; base++)
    {
        base_value = get_base_value(coin,base,max_bit);
        divisors[base-2]=prime_check(base_value);
        if(divisors[base-2]==0)
        {
            validity = false;
            break;
        }
    }
    return validity;
}
void jamcoin::print()
{
    print_bits(coin,max_bit);
    cout<<" ";
    for(int i=0;i<9;i++){cout<<divisors[i]<<" ";}
    cout<<endl;
}
int main()
{
    int T,n,j;
    cin >>T;
    for(int i=0; i<T; i++)
    {
        cin>>n>>j;
        cout<<"Case #"<<i+1<<":"<<endl;
        long int coin_under_check =(1<<n-1)+1;
        jamcoin new_jamcoin(coin_under_check,n);
        while(j!=0)
        {
            jamcoin new_jamcoin(coin_under_check,n);
            if(new_jamcoin.check_validity())
            {
                new_jamcoin.print();
                --j;
            }
            coin_under_check += 2;
        }
    }
}
