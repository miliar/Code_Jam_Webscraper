#include<iostream>
#include<fstream>
#define CIN cin
#define COUT cout
//#define TEST 1
using namespace std;
int main(){
int t,a,b;
int aa[4][4],bb[4][4];
#ifdef TEST
fstream in("ainp.txt"),out("aout.txt");
#endif
CIN>>t;
int caseno=1;
while(t--)
{
    CIN>>a;
    for(int i=0;i<16;i++)
        CIN>>aa[i/4][i%4];
    CIN>>b;
    for(int i=0;i<16;i++)
        CIN>>bb[i/4][i%4];
    int ct=0,ans=-1;
    a--;b--;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            if(aa[a][i]==bb[b][j]){ct++;ans=aa[a][i];}
    COUT<<"Case #"<<caseno<<": ";
    caseno++;
    if(ct==1)COUT<<ans;
    else COUT<<(ct==0?"Volunteer cheated!":"Bad magician!");
    COUT<<endl;
}
}
