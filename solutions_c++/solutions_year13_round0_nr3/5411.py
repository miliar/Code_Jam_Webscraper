#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
#define maxn 10000
int a[105];
bool isre(char x1[],int num){
     for(int k=0;k<num;k++){
             if(x1[k]!=x1[num-k-1]){
                  return false;
                  }
                  }
     return true;
}
bool istrue(int x){
     char temp[10];
     int tempmax=maxn;
     int times=0;
     int flag=0;
     while(tempmax>0){
          if(x/tempmax==0&&flag==0){
               tempmax=tempmax/10;
               continue;
               }
          else{
               flag=1;
               temp[times++]=x/tempmax;
               x=x%tempmax;
               tempmax=tempmax/10;
               }
               }
          if(isre(temp,times))
              return true;
          else
             return false;
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("c.out","w",stdout);
    a[0]=0;
    for(int i=1;i<100;i++){
            bool res=istrue(i);
            a[i]=a[i-1];
            if(res){
                if(istrue(i*i)){
                      a[i]++;
                //      cout<<i<<" "<<a[i]<<endl;
                      }
                  //    cout<<i<<" "<<a[i]<<endl;
                      }
        //    cout<<i<<" "<<a[i]<<endl;
        //    if(i==120)
        //    system("pause");
                      }
    int m;
    cin>>m;
    int time=0;
    while(m--){
       time++;
       int n1,n2;
       cin>>n1>>n2;
       cout<<"Case #"<<time<<": ";
    /*   if(n1==n2){
           cout<<"0"<<endl;
           continue;
           }*/
       int tempn1=ceil(sqrt(n1));
       int tempn2=floor(sqrt(n2));
       
       cout<<a[tempn2]-a[tempn1-1]<<endl;
       }
    return 0;
}
