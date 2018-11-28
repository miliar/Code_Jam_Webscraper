#include<iostream>
#include<string>
#include<math.h>
using namespace std;
long long lst[11];
long long table[11][17];
long long power(long long a, long long b){
          int x;
          long long ans=1;
          for (x=0;x<b;x++) ans=ans*a;
          return ans;
}

long long prime(long long x){
          long long i;
          long long n=(long long)sqrt(x);
          //cout<<"x="<<x<<endl;
          //cout<<"n="<<n<<endl;
          for (i=2;i<n;i++){
              //cout<<x<<"%"<<i<<"="<<x%i<<endl;
              if (x%i==0) return i;
          }
          return -1;
}

string convert(long long x,long long n){
       long long i;
       string ans="";
       char ch;
       for (i=0;i<n;i++){
           ch=(char)(x%2+48);
           x=x/2;
           ans=ch+ans;
       }
       return ans;
}

long long foo(long long x, long long n){
          long long temp;
          while (1){
                if (x%32768==0) {temp=table[n][15]; break;}
                if (x%16384==0) {temp=table[n][14]; break;}
                if (x%8192==0) {temp=table[n][13]; break;}
                if (x%4096==0) {temp=table[n][12]; break;}
                if (x%2048==0) {temp=table[n][11]; break;}
                if (x%1024==0) {temp=table[n][10]; break;}
                if (x%512==0) {temp=table[n][9]; break;}
                if (x%256==0) {temp=table[n][8]; break;}
                if (x%128==0) {temp=table[n][7]; break;}
                if (x%64==0) {temp=table[n][6]; break;}
                if (x%32==0) {temp=table[n][5]; break;}
                if (x%16==0) {temp=table[n][4]; break;}
                if (x%8==0) {temp=table[n][3]; break;}
                if (x%4==0) {temp=table[n][2]; break;}
                if (x%2==0) {temp=table[n][1]; break;}
                return 1;
          }
          temp=temp-(temp-1)/(n-1);
          return temp;
}

int main(){
    int n,k;
    string s;
    long long kk;
    long long i,j;
    long long adder;
    bool flag;
    int count=0;
    cin>>n;
    cin>>n;
    cin>>k;
    cout<<"Case #1:"<<endl;
    for (i=2;i<=10;i++){
        for (j=0;j<16;j++){
            table[i][j]=power(i,j);
            //cout<<table[i][j]<<' ';
        }
        //cout<<endl;
    }
    long long a[11];
    for (i=2;i<=10;i++){
        a[i]=power(i,n-1)+1;
    }
    long long t;
    t=power(2,n-2);
    for (i=1;i<t;i++){
        s=convert(i-1,n-2);
        s='1'+s+'1';
        //cout<<s<<endl;
        for (j=2;j<=10;j++){
            flag=false;
            kk=prime(a[j]);
            if (kk==-1) {
               flag=true;
               break;
            }
            lst[j]=kk;
        }
        for (j=2;j<=10;j++){
            adder=foo(i,j)*j;
            a[j]=a[j]+adder;
        }
        if (flag) continue;
        count++;
        cout<<s;
        for (j=2;j<=10;j++) cout<<' '<<lst[j];
        cout<<endl;
        if (count==k) break;
    }
    //cout<<"end"<<endl;
    //while(1);
}
