#include <bits/stdc++.h>

using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define pd(x) printf("%d",x)
#define pull(x) printf("%llu",x)
#define pll(x) printf("%lld",x)

#define pn() printf("\n")
#define loop(i, a, b) for (int i = int(a); i < int(b); i++)
#define MAXN 1000005
typedef long long int ll;
typedef unsigned long long int ull;
    char my_string[2012];
    int my_counter[35];
    int counter=0;
    int my_answ2[26];
void intit(){

my_answ2[0]=my_counter[int('Z')-64-1];
my_answ2[2]=my_counter[int('W')-64-1];
my_answ2[4]=my_counter[int('U')-64-1];
my_answ2[6]=my_counter[int('X')-64-1];
my_answ2[8]=my_counter[int('G')-64-1];
my_answ2[7]=my_counter[int('S')-64-1]- my_answ2[6];
my_answ2[5]=my_counter[int('F')-64-1]- my_answ2[4];
my_answ2[3]=my_counter[int('H')-64-1]- my_answ2[8];
my_answ2[1]=my_counter[int('O')-64-1]- my_answ2[0]-my_answ2[2]-my_answ2[4];
my_answ2[9]=my_counter[int('I')-64-1]- my_answ2[5]-my_answ2[6]-my_answ2[8];


}
int main()
{
    freopen("A-large.in","r",stdin);
  freopen("out2.txt","w",stdout);
    int t;
    cin>>t;


    while(t--)
    {
        counter++;
        cin>>my_string;

        memset(my_counter, 0 ,sizeof my_counter);
        //loop
        for(int i=0;i<strlen(my_string);i++)
        {
            my_counter[int( my_string[i] )-64-1]++;
        }
       intit();
        cout<<"Case #"<<counter<<":"<<" ";
        for(int i=0;i<10;i++)
        {
            while(my_answ2[i]>0){
                cout<<i;
                my_answ2[i]=my_answ2[i]-1;
                }
        }

        cout<<endl;
    }
    return 0;
}
