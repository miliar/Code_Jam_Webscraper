#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstdlib>
#include<sstream>
#include<cstring>
using namespace std;
ifstream myfile;
FILE  *myfile1;
void solve(int n){
    double c,f,x,ans=0,m=2,k,temp=0,temp1,temp2,prev;
    int t,i;
    myfile>>c;myfile>>f;myfile>>x;
    //c=500.0; f=4.0 ;x=2000.0;
    ans=(double)x/m; prev=(double)x/m;temp1=(double)x/m;temp2=prev;
    while(true){
        temp=(double)temp1+(double)c/m -(double)prev +(double)x/(m+f);
        if(temp>temp1){fprintf(myfile1,"Case #%d: %.7f\n",n,temp1);break;}
        temp1=temp;
        prev=(double)x/(m+f);
        m=m+f;
    }
}
int main(){
    int nt,i;
    myfile1=fopen("bb.txt","w");
    myfile.open("abc.in");
    myfile>>nt;
    //nt=1;
    for(i=1;i<=nt;i++){
        solve(i);
    }
}
