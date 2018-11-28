#include<stdio.h>
#include<iostream>
#include<vector>
#include<stack>
#include<utility>//pair
#include<functional>//greater
#include<queue>
#include<string.h>
#include<algorithm>
#include<math.h>
#define mod 1000000007//10^9+7
#define pp(a,b) make_pair(a,b)
//#include<fstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<long long,long long> pll;
//ifstream fin("B-small-attempt0.in");
//ofstream fout("output.txt");
int main()
{
    int t,tc=1,l,k0,k1,k,c,i,j;
    char s[103];
    scanf("%d",&t);
    //fin>>t;
    while(t--)
    {
        scanf("%s",s);
        //fin>>s;
        l=strlen(s);
        //cout<<l<<endl;
        k0=0;k1=0;c=0;
        if(s[0]=='+')
            k=1;
        else
            k=0;
        for(i=1;i<l;i++)
            {
                if(k==0)
                {
                    if(s[i]=='+')
                    {
                        c++;k=1;
                    }
                }
                else
                {
                    if(s[i]=='-')
                    {
                        c++;k=0;
                    }
                }
            }
            if(k==0)
                c++;
        printf("Case #%d: %d\n",tc,c);
        //fout<<"Case #"<<tc<<": "<<c<<"\n";
        tc++;
    }
    return 0;
}

