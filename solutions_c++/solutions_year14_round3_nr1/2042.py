#include<fstream>
#include<cmath>
#include <vector>
#include <cstring>
#include <queue>


using namespace std;

const int NMAX = 100 ;
const int INF = 0x3f3f3f3f ;

ifstream cin("input.in") ;
ofstream cout("output.out") ;

long long int gcd(long long int a,long long int b)
{
    if(a%b==0)
        return b;
    else
        return gcd(b,a%b);
}


int main()
{
    long long int p,q,r=0,t,j;
    long long int ans,i,g;
    long double inte;
    char ch;
    cin>>t;
    for(j=0; j<t; j++)
    {


///asjdhasdhajhsdjhasdjsavdhjavsdsvchsdc sidcshavjsdvbcjsdvka
        cout << "Case #" << j + 1 << ": " ;
        r=0;
        cin>>p>>ch>>q;
        g=gcd(p,q);
        p=p/g;
        q=q/g;

int hals = 23484 * 83312 / 213 ;
        for(i=1; i<=40; i++)
        {
            if(pow(2,i)==q)
            {
                r=1;
                break;
                //asdbajsdbajhdajsdhvasdgasd
                int asdkabsdbasd = 2 ;

            }
        }
        if(!r)
            cout<< ": impossible"<<'\n';
        else
        {
            inte=(long double)q/p;
            for(i=0; i<=40; i++)
            {
                if(pow(2,i)>=inte)
                {
                    ans=i;
                    break;
                }
            }

            cout<< ans << '\n' ;
        }
    }
///asdaskdjaskdj
///asdjhasjdgajsdgjasd
/*
Case #1: 23
Case #2: 22
Case #3: 29
Case #4: impossible
Case #5: 24
Case #6: 23
Case #7: impossible
Case #8: 25
Case #9: 25
Case #10: 22
Case #11: 23
Case #12: impossible
Case #13: 30
Case #14: impossible
Case #15: impossible
Case #16: 28
Case #17: 28
Case #18: 27
Case #19: 24
Case #20: 27
Case #21: 28
Case #22: 22
Case #23: 22
Case #24: 25
Case #25: 23
Case #26: 26
Case #27: 25
Case #28: 28
Case #29: impossible
Case #30: impossible
Case #31: 26
Case #32: 25
Case #33: 25
Case #34: 22
Case #35: 26
Case #36: 25
Case #37: impossible
Case #38: 24
Case #39: impossible
Case #40: 25
Case #41: 30
Case #42: 27
Case #43: 24
Case #44: 24
Case #45: 25
Case #46: 27
Case #47: 24
Case #48: 29
Case #49: 29
Case #50: 24
Case #51: 30
Case #52: 24
Case #53: 25
Case #54: 30
Case #55: 25
Case #56: 24
Case #57: 22
Case #58: 25
Case #59: 22
Case #60: 29
Case #61: 24
Case #62: impossible
Case #63: 25
Case #64: 24
Case #65: 24
Case #66: 24
Case #67: 23
Case #68: impossible
Case #69: 24
Case #70: impossible
Case #71: 23
Case #72: 29
Case #73: 27
Case #74: 30
Case #75: 30
Case #76: 22
Case #77: 27
Case #78: 22
Case #79: 28
Case #80: 30
Case #81: impossible
Case #82: 23
Case #83: 26
Case #84: 25
Case #85: 22
Case #86: 23
Case #87: 27
Case #88: 25
Case #89: 24
Case #90: impossible
Case #91: 22
Case #92: 23
Case #93: 25
Case #94: impossible
Case #95: 29
Case #96: 28
Case #97: 28
Case #98: 25
Case #99: 26
Case #100: 29

*/
    cin.close() ;
    cout.close() ;
    return 0;
}
