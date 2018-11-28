#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

typedef unsigned long long ull;
const ull fas[] = 
{
    1,
    4,
    9,
    121,
    484,
    10201,
    12321,
    14641,
    40804,
    44944,
    1002001,
    1234321,
    4008004,
    100020001,
    102030201,
    104060401,
    121242121,
    123454321,
    125686521,
    400080004,
    404090404,
    10000200001,
    10221412201,
    12102420121,
    12345654321,
    40000800004,
    1000002000001,
    1002003002001,
    1004006004001,
    1020304030201,
    1022325232201,
    1024348434201,
    1210024200121,
    1212225222121,
    1214428244121,
    1232346432321,
    1234567654321,
    4000008000004,
    4004009004004
};

inline bool pal(ull v)
{
    ostringstream oss;
    oss<<v;
    string s = oss.str();
    int length = s.length();
    int lo = 0;
    int hi = length - 1;
    while(lo < hi)
    {
        if(s[lo]!=s[hi]) return false;
        lo++;
        hi--;
    }
    return true;
}

void init()
{
    ofstream temp("fas");
    for(ull base = 1; base <= 10000000ULL; base++)
    {
        if(pal(base) && pal(base*base)) temp<<"    "<<base*base<<","<<endl;
    }
    temp.close();
}

int eval(ull A, ull B)
{
    int count = 0;
    for(auto v : fas) if(v >= A && v <= B) count++;
    return count;
}
    
void test(ull A, ull B)
{
    cout<<A<<":"<<B<<" = "<<eval(A,B)<<endl;
}

int main(int argc, char* argv[])
{
    //init();
    ifstream in("C-large-1.in");
    ofstream out("out.txt");
    int T;
    in>>T;
    for(int i=0;i<T;i++)
    {
        ull A,B; in>>A>>B;
        out<<"Case #"<<i+1<<": "<<eval(A,B)<<endl;
    }
    in.close();
    out.close();
	return 0;
}
