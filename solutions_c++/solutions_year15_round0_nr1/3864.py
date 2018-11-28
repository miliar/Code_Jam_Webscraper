#include <iostream>
#include <fstream>
#define cin fin
#define cout fout
using namespace std;
ifstream fin("a.in");
ofstream fout("a.out");
char Shy[1002];
int Sm;
int Need(){
    int i,sum=0,tmp,need=0;
    if(Sm==0)
        return 0;
    sum=int(Shy[0])-int('0');
    for (int i=1;i<=Sm;i++)
    {
        if(sum<i) {
            need+=i-sum;
            sum=i;
        }
        tmp=int(Shy[i])-int('0');
        sum+=tmp;
    }
    return need;
}


int main( )
{
    int N,i,num;
    cin>>N;
    for(i=0;i<N;i++)
    {
        cin>>Sm;
        cin>>Shy;
        num=Need();
        cout<<"Case #"<<i+1<<": "<<num<<endl;
    }
    return 0;
}
