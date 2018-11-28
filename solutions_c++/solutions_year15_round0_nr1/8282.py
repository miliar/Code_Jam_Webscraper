#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

ofstream fout;
ifstream fin;

char s[1001];
long sum[1001];
int s_max,T,c,min_el;

int main(){
    fin.open("A-large.in");
    fout.open("output.txt");
    fin>>T;
    for(int t=1;t<=T;t++){
        fin>>s_max;
        for(int i=0;i<=s_max;i++){
            fin>>s[i];
            sum[i]=0;
        }
        sum[0]=s[0]-'0';
        min_el=0;
        for(int i=1;i<=s_max;i++){
            if(sum[i-1]>=i)
                sum[i]=sum[i-1]+s[i]-'0';
            else{
                c=i-sum[i-1];
                sum[i]=sum[i-1]+s[i]-'0'+c;
                min_el+=c;
        }
        }
  fout<<"Case #"<<t<<":"<<" "<<min_el<<"\n";
    }
  return 0;
}
