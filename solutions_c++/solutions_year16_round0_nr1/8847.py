#include<bits/stdc++.h>
using namespace std;
int t0=0,t1=0,t2=0,t3=0,t4=0,t5=0,t6=0,t7=0,t8=0,t9=0;
void reinitialize()
    {
t0=0;t1=0;t2=0;t3=0;t4=0;t5=0;t6=0;t7=0;t8=0;t9=0;}
void check(int n){
    switch(n){
        case 0:t0=1;break;
        case 1:t1=1;break;
        case 2:t2=1;break;
        case 3:t3=1;break;
        case 4:t4=1;break;
        case 5:t5=1;break;
        case 6:t6=1;break;
        case 7:t7=1;break;
        case 8:t8=1;break;
        case 9:t9=1;break;
    }
}
int checkall(){
    if(t0==1 && t1==1 && t2==1 && t3==1 && t4==1 && t5==1 && t6==1 && t7==1 && t8==1 && t9==1)
        return 1;
    else 
        return 0;
}
int main(){
    int n;
    int t;
    int m,j,a[100],b[100];
    cin>>t;
    for(int i=0;i<t;i++){
        cin>>n;
        reinitialize();
        if(n==0)
            cout<<"Case #"<<i+1<<": INSOMNIA\n";
            else
            {cout<<"Case #"<<i+1<<": ";
j=0;
                m=n;
            while(m>0){
                a[j]=m%10;
                m=m/10;
                check(a[j]);j++;
            };
            int s=j;
            for(int k=2;;k++){int size=s;
                int c=0;
                for(int j=0;j<size;j++){
                    int prod=a[j]*k+c;
                    b[j]=prod%10;
                    c=prod/10;
                    check(b[j]);
                }
                while(c){
                    b[size]=c%10;
                    c=c/10;
                    check(b[size]);size++;  
                }
             if(checkall()){
                 for(int l=size-1;l>-1;l--)cout<<b[l];
                 break;
             }
                
            }label:cout<<"\n";
        }
    }
    return 0;
}
