#include <iostream>
#include<fstream>
using namespace std;
typedef long long LL;
int b[40],t,N,J,total;
LL ans[505][12];
LL base(LL k){
    LL x=0,y=1;
    for(int i=N;i>=1;i--){
        x+=y*b[i];
        y*=k;
    }
    return x;
}
LL notprime(LL x){
    LL i;
    if(x%2==0)return 2;
    for(i=3;i*i<=x;i+=2)
        if(x%i==0)return i;
    return 0;
}
void Find(int x){
    if(total>50)return;
    if(x==N){
        int i;
        for(i=2;i<=10;i++){
            LL num=notprime(base(i));
            if(num!=0)ans[total][i]=num;
            else break;
        }
        if(i==11){
            ans[total][1]=base(10);
            total++;
        }
    }
    else{
        b[x]=1;
        Find(x+1);
        b[x]=0;
        Find(x+1);
    }
}
int main()
{
    ifstream in;
    ofstream out;
    in.open("E:\\project\\C-small-attempt0.in");
    out.open("E:\\project\\c-small.txt");
    in>>t;int k=0;
    while(t--){
        k++;
        in>>N>>J;
        for(int i=1;i<=N;i++)b[i]=0;
        b[1]=1;b[N]=1;
        total=0;
        Find(2);
        out<<"Case #"<<k<<": "<<endl;
        for(int i=0;i<J;i++){
            for(int j=1;j<=10;j++){
                if(j>1)out<<" ";
                out<<ans[i][j];
            }
            out<<endl;
        }
    }
    in.close();
    out.close();
    return 0;
}
