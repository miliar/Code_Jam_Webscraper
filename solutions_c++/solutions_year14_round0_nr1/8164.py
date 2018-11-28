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

int a[17];
int main(){
    int T,row, second,i,j,t,x,k,found,ans;
    T = read();
    for(t=1;t<=T;t++){
               cout<<"Case #"<<t<<": ";
               memset (a,0,17*sizeof(int));
               for(k=0;k<2;k++){
                    row = read();
                    for(i=1;i<=4;i++)
                       for(j=1;j<=4;j++){
                           x = read();
                           if(i==row) a[x]++;
                       }
               }
               found=0;
               for(i=1;i<=16;i++){
//                                  cout<<a[i]<<":";
                   if(a[i] == 2) {found++; ans=i;}
               }
               if(found == 0){
                        cout<<"Volunteer cheated!";
               } else if (found ==1){
                      cout<<ans;
               } else {
                      cout<<"Bad magician!";
               }
               cout<<endl;
    }
//   while(1);
}
