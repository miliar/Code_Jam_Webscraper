#include<fstream>
#include<string>

using namespace std;

const char* input_fname = "input";
const char* output_fname = "output";

const int digits_limit = 101;

class LargeInt
{
public:
    int value[digits_limit];
    int digits;

    LargeInt();
    LargeInt(int digits);
    LargeInt(string lit);

    bool is_palindrome();
    bool smaller_then(LargeInt t);
    bool bigger_then(LargeInt t);
    LargeInt square();
    void increase_one();
};

int main(void)
{
    ifstream in(input_fname);
    ofstream out(output_fname);

    int testcase_sz = 0;
    in >> testcase_sz;

    for(int case_id=1;case_id<=testcase_sz;case_id++)
    {
        int num_fair_and_square = 0;

        string Astr, Bstr;
        in >> Astr >> Bstr;
        LargeInt A(Astr);
        LargeInt B(Bstr);
        LargeInt a( (1+Astr.size())/2 );
        LargeInt b( (1+Bstr.size())/2 );

        while( a.square().smaller_then(A) ) a.increase_one();
        while( !b.square().bigger_then(B) ) b.increase_one();

        for(;a.smaller_then(b);a.increase_one())
        {
            if( !a.is_palindrome() ) continue;
            if( a.square().is_palindrome() ) num_fair_and_square++;
        }

        out << "Case #" << case_id << ": " << num_fair_and_square;

        if(case_id<testcase_sz) out << endl;
    }

    return 0;
}

LargeInt::LargeInt()
{
    for(int i=0;i<digits_limit;i++) value[i] = 0;
}

LargeInt::LargeInt(int digits)
{
    for(int i=0;i<digits_limit;i++) value[i] = 0;
    value[digits-1] = 1;
    this->digits = digits;
}

LargeInt::LargeInt(string lit)
{
    int sz = lit.size();
    this->digits = sz;
    int i=0;
    for(;i<sz;i++)
    {
        value[sz-i-1] = (lit.c_str())[i] - '0';
    }
    for(;i<digits_limit;i++)
    {
        value[i] = 0;
    }
}

bool LargeInt::is_palindrome()
{
    for(int i=0;i<digits/2;i++)
    {
        if(value[i]!=value[digits-i-1]) return false;
    }
    return true;
}

bool LargeInt::smaller_then(LargeInt t)
{
    if(digits<t.digits) return true;
    if(digits>t.digits) return false;
    for(int i=digits-1;i>=0;i--)
    {
        if(value[i]<t.value[i]) return true;
        if(value[i]>t.value[i]) return false;
    }
    return false;
}

bool LargeInt::bigger_then(LargeInt t)
{
    if(digits<t.digits) return false;
    if(digits>t.digits) return true;
    for(int i=digits-1;i>=0;i--)
    {
        if(value[i]<t.value[i]) return false;
        if(value[i]>t.value[i]) return true;
    }
    return false;
}

LargeInt LargeInt::square()
{
    LargeInt ret;

    for(int i=0;i<digits;i++)
    {
        for(int j=0;j<digits;j++)
        {
            ret.value[i+j] += value[i]*value[j];
        }
    }

    for(int d=0;d<2*digits;d++)
    {
        if(ret.value[d]>9)
        {
            ret.value[d+1] = ret.value[d]/10;
            ret.value[d] = ret.value[d]%10;
        }
    }

    if(ret.value[2*digits-1]==0) ret.digits = 2*digits-1;
    else ret.digits = 2*digits;

    return ret;
}

void LargeInt::increase_one()
{
    int pos = 0;
    while( value[pos]==9 ) pos++;
    value[pos]++;
    for(int i=0;i<pos;i++) value[i] = 0;
    if(pos==digits) digits++;
}
