#include<iostream>
#include<fstream>
using namespace std;
int a[100];
ifstream in("small.txt");
ofstream out("Q1.out");
void initialize(string s){
     int i;
     int len=s.length();
     int temp;
     for (i=0;i<len;i++){
         temp=(int)s[i];
         temp=temp-64;
         a[temp]++;
     }
}
bool contains(string s){
     int i,temp;
     int len=s.length();
     int b[100];
     for (i=0;i<100;i++) b[i]=a[i];
     for (i=0;i<len;i++){
         temp=(int)s[i];
         //cout<<temp<<endl;
         temp=temp-64;
         b[temp]--;
         if (b[temp]<0) return false;
     }
     return true;
}
void subtract(string s){ 
     int i,temp;
     int len=s.length();
     for (i=0;i<len;i++){
         temp=(int)s[i];
         temp=temp-64;
         a[temp]--;
     }
}
void test(){
     int i,temp;
     char ch;
     for (i=1;i<=26;i++){
         temp=i+64;
         ch=(char)temp;
         out<<ch<<": "<<a[i]<<endl;
     }
}
int main(){
    
    int n,i,j,k,l;
    string s;
    //string num[10]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
    string num[10]={"EIGHT","ZERO","TWO","SIX","SEVEN","FIVE","FOUR","ONE","THREE","NINE"};
    int opt[10]={8,0,2,6,7,5,4,1,3,9};
    int ot[10];
    in>>n;
    for (i=1;i<=n;i++){
        out<<"Case #"<<i<<": ";
        for (j=0;j<100;j++) a[j]=0;
        for (j=0;j<10;j++) ot[j]=0;
        in>>s;
        initialize(s);
        //test();
        for (j=0;j<10;j++){
            while (1){
                  if (contains(num[j])) {
                     subtract(num[j]);
                     //test();
                     ot[opt[j]]++;
                  }
                  else {break;}
            }
        }
        for (j=0;j<10;j++)
            for (k=0;k<ot[j];k++) out<<j;
        out<<endl;
    }
    //while(1);
}
