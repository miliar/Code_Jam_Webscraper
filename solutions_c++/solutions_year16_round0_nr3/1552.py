#include <iostream>
#include <gmp.h>
#include <vector>
#include <fstream>
#define PLENTY (10000000)
#define MAX_ULONG (18446744073709551615)
using namespace std;

vector<unsigned long> sieve (unsigned long N)
{
    vector<bool> sieve_(N+1,true);
    sieve_[0]=false;
    sieve_[1]=false;
    unsigned long p=2;
    unsigned long n=1;
    unsigned long i;
    while(1)
    {
        sieve_[p]=true;
        for(i=2*p;i<=N;i+=p)
        {
            sieve_[i]=false;
        }
        bool found=false;
        for(i=p+1;i<=N;i++)
        {
            if(sieve_[i])
            {
                p=i;
                found=true;
                n++;
                break;
            }
        }
        if(!found)
            break;
    }
    vector<unsigned long> res(n);
    unsigned long counter=0;
    for(i=2;i<=N;i++)
    {
        if(sieve_[i])
        {
            res[counter]=i;
            counter++;
        }
    }
    return res;
}

class coinjam
{
    public:
    coinjam(int);
    std::ostream& print_coinjam(std::ostream&);
    bool is_legit();
    void next();
    //~coinjam();
    unsigned long get_div(int base)const{return divs[base];}
    private:
    unsigned long get_divisor(mpz_t x);
    void get_reps_from_current();
    void get_current_from_rep();
    int N;
    mpz_t rep;
    vector<int> current;
    mpz_t reps[11];
    vector<unsigned long> sieve_;
    vector<unsigned long> divs;
};

std::ostream& coinjam::print_coinjam(std::ostream& f)
{
    for(int i=0;i<N;i++)
    {
        f<<current[i];
    }
    return f;
}

coinjam::coinjam (int N_)
{
    N=N_;
    current=vector<int>(N);
    current[0]=1;
    current[N-1]=1;
    for(auto i=1;i<N-1;i++)
    {
        current[i]=0;
    }
    sieve_=sieve(PLENTY);
    divs=vector<unsigned long>(11);
    mpz_init_set_ui(rep,0);
    for(auto i=2;i<=10;i++)
    {
        mpz_init(reps[i]);
    }
    get_reps_from_current();

}
void coinjam::get_current_from_rep()
{
    unsigned long r;
    mpz_t q;
    mpz_init(q);
    mpz_set(q,rep);
    for(int i=N-2;i>=1;i--)
    {
        r=mpz_fdiv_q_ui(q,q,2);
        current[i]=r;
    }
    mpz_clear(q);
}
void coinjam::next()
{
    mpz_add_ui(rep,rep,1);
    get_current_from_rep();
    //cout<<"baz2"<<endl;
    get_reps_from_current();
}

void coinjam::get_reps_from_current()
{
    mpz_t multiplier;
    mpz_init(multiplier);
    for(auto i=2;i<=10;i++)
    {
        mpz_set_ui(multiplier,1);
        mpz_set_ui(reps[i],0);
        for(auto j=N-1;j>=0;j--)
        {
            if(current[j]==1)
            {
                mpz_add(reps[i],reps[i],multiplier);
            }
            mpz_mul_ui(multiplier,multiplier,i);
        }
    }
    mpz_clear(multiplier);
}

unsigned long coinjam::get_divisor(mpz_t x)
{
    mpz_t q;
    mpz_init(q);
    for(auto p:sieve_)
    {
        if(mpz_divisible_ui_p(x,p))
        {
            mpz_fdiv_q_ui(q,x,p);
            if(mpz_cmp_ui(q,1)>0)
            {
                mpz_clear(q);
                return p;
            }
        }
    }
    mpz_clear(q);
    return MAX_ULONG;
}

bool coinjam::is_legit()
{
    unsigned long tmp;
    for(int base=2;base<=10;base++)
    {
        tmp=get_divisor(reps[base]);
        if(tmp==MAX_ULONG)
            return false;
        else
        {
            divs[base]=tmp;
        }
    }
    return true;
}
int main()
{
    ofstream out;
    out.open("out.txt");
    int N=32;
    int J=500;
    coinjam cj(N);
    int T=1;
    int i,j;
    out<<"Case #"<<T<<":"<<endl;
    for(j=0;j<J;j++)
    {
        while(true)
        {
        if(cj.is_legit())
        {
            cj.print_coinjam(out);
            //out<<" ";
            for(i=2;i<=10;i++)
            {
                out<<" "<<cj.get_div(i);
            }
            out<<endl;
            cj.next();
            break;
        }
        else cj.next();
        }
    }
    out.close();
//    mpz_t x;
//    mpz_init_set_ui(x,12);
//    for(int i=0;i<5;i++)
//    {
//        gmp_printf("%Zd\n",x);
//        mpz_mul(x,x,x);
//    }
//
//    mpz_clear(x);
}
