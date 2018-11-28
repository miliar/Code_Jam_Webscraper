#include <iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
bool b[11];
int main()
{
    long long t,n,i,num,temp,cur,no;
    FILE *in=NULL,*out=NULL;
    in=fopen("E:\\project\\A-large.in","r");
    out=fopen("E:\\project\\large-out.txt","w");
    if(!in){
        cout<<"error"<<endl;
        return 0;
    }
    fscanf(in,"%lld",&t);
    //cin>>t;
    cout<<t;
    no=0;
    while(t--){
        fscanf(in,"%lld",&n);
        //cin>>n;
        //cout<<n;
        no++;
        if(n==0){
            cout<<"Case #"<<no<<": "<<"INSOMNIA"<<endl;
            fprintf(out,"Case #%lld: INSOMNIA\n",no);
            continue;
        }
        for(i=0;i<11;i++)b[i]=false;num=0;cur=n;
        for(i=1;i<10000;i++,cur+=n){
            temp=cur;
            while(temp){
                if(!b[temp%10]){
                    num++;
                    b[temp%10]=true;
                }
                temp/=10;
            }
            if(num==10)break;
        }
        if(i==10000){
            cout<<"Case #"<<no<<": "<<"INSOMNIA"<<endl;
            fprintf(out,"Case #%lld: INSOMNIA\n",no);
        }
        else {
            cout<<"Case #"<<no<<": "<<cur<<endl;
            fprintf(out,"Case #%lld: %lld\n",no,cur);
        }
    }
    fclose(in);
    fclose(out);
    return 0;
}
