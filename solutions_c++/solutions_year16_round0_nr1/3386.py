#include<iostream>
using namespace std;
int a[200];
//bool b[200];
bool contain[10];
void judge(int x){
     int t=x;
     int k,i,temp;
     bool flag;
     for (i=0;i<10;i++) contain[i]=false;
     //if (f) contain[0]=true;
     while (1){
           temp=t;
           flag=false;
           while (temp>0){
                 k=temp%10;
                 temp=temp/10;
                 contain[k]=true;
           }
           for (i=0;i<10;i++){
               if (contain[i]==false){
                  t=t+x;
                  flag=true;
                  break;
               }
           }
           if (flag) continue;
           cout<<t<<endl;
           return;
     }
     
}
int main(){
    int n,i,x;
    cin>>n;
    for (i=0;i<n;i++){
        cin>>x;
        a[i]=x;
    }
    for (i=0;i<n;i++){
        cout<<"Case #"<<i+1<<": ";
        if (a[i]==0) cout<<"INSOMNIA"<<endl;
           else judge(a[i]);
    }
    //while (1);
}
