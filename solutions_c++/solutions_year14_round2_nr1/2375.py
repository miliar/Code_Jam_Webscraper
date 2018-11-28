#include<iostream>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
#include<stdio.h>
using namespace std;
int main(){
freopen("A-small-attempt0.in","r",stdin);
freopen("out.txt","w",stdout);
long long int test,i,j,u,l,v=0,q;
cin>>test;
while(test--){
    v++;
    cin>>q;
    string a[q];
    string b[q];
    for(i=0;i<q;i++){
        cin>>a[i];
        b[i]+=a[i]+'=';
    }
    cout<<"Case #"<<v<<": ";
    int s1=0;
    string z;
    for(j=0;j<b[0].size();j++){
            if(b[0][j]!=b[0][j+1]){
                z+=b[0][j];
            }
        }
    for(i=1;i<q;i++){
            string x;
            for(j=0;j<b[i].size();j++){
                if(b[i][j]!=b[i][j+1]){
                x+=b[i][j];
                }
            }
        if(x.size()!=z.size()){
            s1=1;
            break;
        }
        else{
            for(j=0;j<z.size();j++){
                if(z[j]!=x[j]){
                    s1=1;
                    break;
                }
            }
            if(s1==1){
                break;
            }
        }
    }
    if(s1==1){
        cout<<"Fegla Won\n";
    }
    else{
        long long  int m1=0,m2=100000000;
        long int aa[q][100];
        for(i=0;i<q;i++){
            for(j=0;j<100;j++){
                aa[i][j]=0;
            }
        }
        for(i=0;i<q;i++){
                int u=0;
                string qw=a[i]+'=';
            for(j=0;j<qw.size();j++){
                if(a[i][j]==a[i][j+1]){
                    aa[i][u]++;
                }
                else
                {aa[i][u]++;u++;}
            }
        }
        for(i=0;i<q;i++){
            m1=0;
            for(j=0;j<q;j++){
                for(u=0;u<a[i].size();u++){
                    m1+=abs(aa[i][u]-aa[j][u]);
                }
            }
            m2=min(m1,m2);
        }
        string x=a[0]+'=';
        int s2=0;
    for(i=0;i<a[0].size()-1;i++){
       if(a[0][i]!=a[0][i+1])
        s2++;
    }
    s2++;
    m1=0;
    for(i=0;i<q;i++){
        int o=a[i].size();
        m1+=abs(o-s2);
    }
    
    m2=min(m1,m2);
    cout<<m2<<"\n";m2=100000000;
    }

}
return 0;}

