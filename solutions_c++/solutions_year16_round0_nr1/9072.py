#include<stdio.h>
#include<iostream>
#include<vector>
#include<stack>
#include<utility>//pair
#include<functional>//greater
#include<queue>
#include<algorithm>
#include<math.h>
#define mod 1000000007//10^9+7
#define pp(a,b) make_pair(a,b)
//#include<fstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<long long,long long> pll;
//ifstream fin("A-small-attempt0.in");
//ofstream fout("out.txt");
int main()
{
    int t,tc=1,n,x,f,cd;
    scanf("%d",&t);
    //fin>>t;
    while(t--)
    {
        scanf("%d",&n);
        //fin>>n;
        f=10;
        bool d[10]={0};
        if(n>0)
        {
            int i;
            for(i=1;f>0;i++)
            {
                x=i*n;
                while(x>0&&f)
                {
                    cd=x%10;
                    if(!d[cd])
                    {
                        d[cd]=1;f--;
                    }
                    x/=10;
                }
            }
            i--;
            x=i*n;
            printf("Case #%d: %d\n",tc,x);
            //fout<<"Case #"<<tc<<": "<<x<<endl;
        }
        else
        {
            printf("Case #%d: INSOMNIA\n",tc);
            //fout<<"Case #"<<tc<<": INSOMNIA\n";
        }

        tc++;
    }
    return 0;
}

