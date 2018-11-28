#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<cmath>
#include<string>
#include<string.h>
#include<strings.h>
#include<iomanip>
#include<cstdio>
#include<bitset>
#include<fstream>
using namespace std;
int main(){

 ofstream fout ("A-large-output.txt");
 ifstream fin ("A-large.in");
 int t, T;
 long long temp, n, i, x, a[10], digit, j, flag;
 fin>>T;
 for(t=1;t<=T;++t){
    flag=0;
    for(i=0;i<10;++i){
        a[i]=0;
    }
    fin>>n;
    if(n==0)
    {
        fout<<"Case #"<<t<<": INSOMNIA"<<endl;
        continue;
    }
    temp=n;
    while(temp>0){
        digit=temp%10;
        a[digit]++;
        temp=temp/10;
    }
    for(i=2;;++i){
        flag=0;
        x=i*n;
        temp=x;

        while(temp>0){
            digit=temp%10;

            a[digit]++;
            temp=temp/10;
        }

        for(j=0;j<10;j++){
            if(a[j]==0)
                flag=1;
        }
        if(flag==0)
            break;

    }

    fout<<"Case #"<<t<<": "<<x<<endl;

  }

 return 0;
}
