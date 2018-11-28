#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
#define ll long long
#define forr(i,n) for(int i=0;i<n;i++)
#define s(n) scanf("%d",&n)
#define p(n) printf("%d\n",n)
int main(){
    int t;s(t);
    forr(j,t){
        int x,r,c;s(x);s(r);s(c);
        bool flag = 0;
        if((r*c)%x!=0){
            flag = 0;
        }
        else{
            if(x==1 || x==2)
                flag = 1;
            else if(x==3){
                if(r==1 || c==1)
                    flag=0;
                else
                    flag=1;
            }
            else{
                if(r*c==8 || r*c==4)
                    flag = 0;
                else
                    flag = 1;
            }
        }
        if(flag==0)
            cout<<"Case #"<<j+1<<": RICHARD"<<endl;
        else
            cout<<"Case #"<<j+1<<": GABRIEL"<<endl;
    }
}
