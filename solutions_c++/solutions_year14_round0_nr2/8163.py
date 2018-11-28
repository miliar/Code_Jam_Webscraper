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

int main(){
    int T,t;
    double C,F,X,sum,r,curSum,CbyF,time;
    T = read();
    for(t=1;t<=T;t++){
        cin>>C>>F>>X;
        CbyF = C/F;
        sum=0;
        r=2;
        time=0;
        while(X > (C + CbyF*r)){
            sum=curSum;
            time+=C/r;
            r+=F;
        }
        time+= X/r;
        printf("Case #%d: %.7f\n",t,time);
//        cout<<"Case #"<<t<<": "<<time<<endl;
    }
//   while(1);
}
