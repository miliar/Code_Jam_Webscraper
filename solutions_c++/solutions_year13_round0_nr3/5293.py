#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <sstream>
#define FOR1(i,n) for(i=1;i<=n;i++)
using namespace std;

bool checkfair(long long x)
{
    stringstream ss;
    bool res=true;
    ss<<x;
    string sint=ss.str();
    //cout<<sint<<endl;
    int i=0, j=sint.length()-1;
    while(i<j)
    {
        if(sint[i]!=sint[j])
        {
            res=false;
            break;
        }
        i++; j--;
    }



    return res;

}


int main()
{
    int sm=1;
    char *filin, *filot;
    if(sm)
    {
        filin="C-small-attempt0.in";
        filot="C-small-result.txt";
    }
    else
    {
        filin="C-large.in";
        filot="C-large-result.txt";

    }

    ifstream inf;
    ofstream otp;

    inf.open(filin);
    otp.open(filot);

    string line;
    int res_cnt;
    long num;
    long double sqrtnum;
    int test, it_test=1;
    getline(inf, line);
    stringstream sline(line);
    sline>>test;

    FOR1(it_test, test)
    {
        res_cnt=0;
        getline(inf, line);
        string a="", b="";
        int i=0;
        int lim=line.length()-1;
        while(i<lim)
        {
            if(line[i]==' ')
                break;
            i++;
        }
        a=line.substr(0,i);
        b=line.substr(i+1, lim+1);

        stringstream ssa(a);
        stringstream ssb(b);

        long na, nb;
        ssa>>na;
        ssb>>nb;
//cout<<a<<" "<<b<<endl;
        for(num=na;num<=nb;num++)
        {
            int dig=num-(num/10)*10;

         if(dig==2 || dig==3 || dig==7 || dig==8)
            continue;

            if(checkfair(num))
            {
                sqrtnum=sqrt(num);
                if(sqrtnum==floor(sqrtnum) && checkfair(sqrtnum))
                    res_cnt++;
            }
        }

    otp<<"Case #"<<it_test<<": "<<res_cnt<<endl;

    }
    return 0;
}
