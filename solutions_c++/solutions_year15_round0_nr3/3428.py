#include <iostream>
#include <cstdio>
using namespace std;
char r[4][4]={{'1','i','j','k'},{'i','1','k','j'},{'j','k','1','i'},{'k','j','i','1'}};
int s[4][4]={{1,1,1,1},{1,-1,1,-1},{1,-1,-1,1},{1,1,-1,-1}};
int c(char ch)
{
    if(ch=='1') return 0;
    else if(ch=='i') return 1;
    else if(ch=='j') return 2;
    else if(ch=='k') return 3;
}
void process(){
    long long int L,X;
    cin>>L>>X;
    char ch[10005];
    int result=0;
    int sign=1;
    
    int flag=0;
    int current=1;
     for(long long int i=0;i<L;i++)
    {
        scanf(" %c",&ch[i]);
	}
    for(long long int i=0;i<L*X;i++)
    {
        sign=sign*s[result][c(ch[i%L])];
        result=c(r[result][c(ch[i%L])]);
       // cout<<"R " <<result<<" "<<"S "<<sign<<endl;
        if(result==current && sign==1){ current++; result=0;}
    }
	if(current==4 && result == 0 && sign== 1) cout<<"YES\n";
    else cout<<"NO\n";
}

int main()
{
   // freopen("input.txt","r",stdin);
    int T;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        process();
    }
}
