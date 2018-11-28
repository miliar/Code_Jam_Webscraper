#include<cstdio>
#include<iostream>

using namespace std;

inline void write(int a){
       register char c;
       char snum[20];
       int i=0;
       do{
          snum[i++]=a%10+48;
          a=a/10;
       }while(a!=0);
       i=i-1;
       while(i>=0)
           putchar(snum[i--]);
}

inline int readString() {
  register char c = getchar();
  while(c<'0' || c>'1') c = getchar();
  int ret = 0;
  while(c>='0' && c<='1') {
    ret = ret|(c - 48);
    ret<<=1;
    c = getchar();
  }
  ret>>=1;
  return ret;
}

inline int read() {
  register char c = getchar();
  while(c<'0' || c>'9') c = getchar();
  int ret = 0;
  while(c>='0' && c<='9') {
    ret = (ret<<3)+(ret<<1) + c - 48;
    c = getchar();
  }
  return ret;
}

inline long readL() {
  register char c = getchar();
  while(c<'0' || c>'9') c = getchar();
  long ret = 0;
  while(c>='0' && c<='9') {
    ret = (ret<<3)+(ret<<1) + c - 48;
    c = getchar();
  }
  return ret;
}

int main(){
    int T,t;
    long long P,Q,div,ans,k;
    T = read();
    for(t=1;t<=T;t++){
            P=readL();
            Q=readL();
//            cout<<"Read: P="<<P<<",Q="<<Q<<endl;
            if(P>Q || Q==0){
                    cout<<"Case #"<<t<<": impossible"<<endl;
                    continue;
            } if(P==0 || P==Q){
                    cout<<"Case #"<<t<<": 0"<<endl;
                    continue;                    
            }            
            while(P%2==0 && Q%2==0){
                         P>>=1;
                         Q>>=1;
            }
//            cout<<"Reduced is "<<P<<"/"<<Q<<endl;
            if(Q%2){
                    cout<<"Case #"<<t<<": impossible"<<endl;
                    continue;
            }
            int x=2; 
            ans=0;  
            while(x <= Q && Q%x==0){
              x<<=1;
              ans++;
            }
            k = 1L<<ans;
            div = Q/k;
//            cout<<"Found div="<<div<<endl;
            if(P%div == 0){
                     P/=div;
                     while(P>0){
                                P>>=1;
                                ans--;
                     }
                    cout<<"Case #"<<t<<": "<<(ans+1)<<endl;
            } else {
                    cout<<"Case #"<<t<<": impossible"<<endl;
            }
    }
//    while(1);
}
