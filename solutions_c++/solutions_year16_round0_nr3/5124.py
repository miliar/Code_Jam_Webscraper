#include <bits/stdc++.h>
using namespace std;

ifstream f("wow.in");
ofstream g("wow.out");
ofstream g2("wow2.out");
ofstream g3("wow3.out");

#define nr_cif 32
#define ll long long
vector<vector<int> > result_bit;
vector<vector<int> > result_divs;

vector<int> div_list;
int max_val=0;

bool is_sam(vector<int> i1,vector<int> i2)
{
    if (i1.size()!=i2.size()) return false;

    for(int i=0;i<i1.size();++i)
         if (i1[i]!=i2[i])
             return false;

    return true;
}

int is_not_prime(vector<int> bit_vec,int base)
{
    int mval=0,i,j;


    for(i=0;i<nr_cif;++i)
    {
        mval=mval*base+bit_vec[i];
        if (mval>1000) break;
    }

    for(i=2;i<mval;++i)
    {
        int R=0;
        for(j=0;j<nr_cif;++j) {
            R = (R * base + bit_vec[j]) % i;
        }

        if (R==0) return i;
    }
    return 0;
}

bool jam_money(vector<int> bit_vec) {

    div_list.clear();

    for(int base=2;base<=10;base++)
    {
       if (is_not_prime(bit_vec,base))
       {
           div_list.push_back(is_not_prime(bit_vec,base));
       }
       else
       {
         return false;
       }
    }

    return true;
}

template <typename T>
ostream& operator <<(ostream&os ,vector<T> &my_vec)
{
    for(auto it=my_vec.begin();it!=my_vec.end();++it)
        os<<*it;
   return os;
}

bool checker(vector<int> bits,vector<int> divs)
{
    for(ll base=2;base<=10;base++)
    {
       ll nr=0;
       for(auto &it:bits) nr=nr*base+((ll)it);

       if (nr%divs[base-2]!=0)
       {
           g2<<"Nr:  "<<nr<<"  Base:  "<<base<<" "<<"  Divisor  "<<divs[base-2];
           return false;
       }
    }

    return true;
}

int main()
{
    int nr_sol=0;

    g<<"Case #1:"<<'\n';

    while (true)
    {
        vector<int> bit_vec={1};
        for(int i=1;i<=nr_cif-2;++i)  bit_vec.push_back(rand()%2);
        bit_vec.push_back(1);

        if (jam_money(bit_vec))
        {
            ++nr_sol;
            result_bit.push_back(bit_vec);
            result_divs.push_back(div_list);
        }

        if (nr_sol==500)
        {
            break;
        }
    }

    for(int i=0;i<nr_sol;++i) {
        g << result_bit[i] << " ";
        for(auto &it:result_divs[i])
            g<<it<<" ";

        g<<'\n';
    }



    return 0;
}