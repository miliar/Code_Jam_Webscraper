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
ifstream fin ("c-small.in");
ofstream fout ("coin.txt");
long long ji;
void three(long long divisor){
 long long count, mod, ans, tempo, sum;
 tempo=divisor;
 sum=0;
 count=0;
 while(tempo>0){
    mod=tempo%10;
    sum=sum+(mod*round(pow(3,count)));
    count++;
    tempo/=10;
 }
    fout<<sum<<" ";

}


void four(long long divisor){
 long long count, mod, ans, tempo, sum;
 tempo=divisor;
 sum=0;
 count=0;
 while(tempo>0){
    mod=tempo%10;
    sum=sum+(mod*round(pow(4,count)));
    count++;
    tempo/=10;
 }

    fout<<sum<<" ";
}

void five(long long divisor){
 long long count, mod, ans, tempo, sum;
 tempo=divisor;
 sum=0;
 count=0;
 while(tempo>0){
    mod=tempo%10;
    sum=sum+(mod*round(pow(5,count)));
    count++;
    tempo/=10;
 }

    fout<<sum<<" ";
}

void six(long long divisor){
 long long count, mod, ans, tempo, sum;
 tempo=divisor;
 sum=0;
 count=0;
 while(tempo>0){
    mod=tempo%10;
    sum=sum+(mod*round(pow(6,count)));
    count++;
    tempo/=10;
 }

fout<<sum<<" ";
}

void seven(long long divisor){
 long long count, mod, ans, tempo, sum;
 tempo=divisor;
 sum=0;
 count=0;
 while(tempo>0){
    mod=tempo%10;
    sum=sum+(mod*round(pow(7,count)));
    count++;
    tempo/=10;
 }
 fout<<sum<<" ";

}

void eight(long long divisor){
 long long count, mod, ans, tempo, sum;
 tempo=divisor;
 sum=0;
 count=0;
 while(tempo>0){
    mod=tempo%10;
    sum=sum+(mod*round(pow(8,count)));
    count++;
    tempo/=10;
 }

 fout<<sum<<" ";
}

void nine(long long divisor){
 long long count, mod, ans, tempo, sum;
 tempo=divisor;
 sum=0;
 count=0;
 while(tempo>0){
    mod=tempo%10;
    sum=sum+(mod*round(pow(9,count)));
    count++;
    tempo/=10;
 }

 fout<<sum<<" ";
}

long long two (long long x)
{
    vector<long long>basetwo;

    long long temp, divisor, j, i, rem;
    double z;
    for(i=2;i<=60000;i++){

        basetwo.clear();
        temp=i;
        //fout<<temp<<" ";
        divisor=0;
        while(i>0){
            rem=i%2;
            basetwo.push_back(rem);
            i=i/2;
        }

        for(j=0,z=0;j<basetwo.size();j++,z++)
        {
            divisor=divisor+(basetwo[j]*round(pow(10,z)));
        }
        if(divisor==x)
            return -2;
        //fout<<divisor<<endl;
        if(x%divisor==0)
            {
                ji--;

                fout<<x<<" ";
                fout<<temp<<" ";
                three(divisor);
                four(divisor);
                five(divisor);
                six(divisor);
                seven(divisor);
                eight(divisor);
                nine(divisor);
                fout<<divisor<<endl;
                if(ji==0)
                    exit(0);
                return -1;
            }

        i=temp;
    }



}

int main(){
 string s, t;
 long long te, x, ans, n;
 fin>>te;
 fin>>n>>ji;
 s="1000000000000001";
 x=stoll(s);
 fout<<"Case #"<<"1: "<<endl;
 ans=two(x);

 s="00000000000001";
 do{
    t="1"+s+"1";
    x=stoll(t);
    ans=two(x);
 }while(next_permutation(s.begin(),s.end()));

 s="00000000000011";
 do{
    t="1"+s+"1";
    x=stoll(t);
    ans=two(x);
 }while(next_permutation(s.begin(),s.end()));

 s="00000000000111";
 do{
    t="1"+s+"1";
    x=stoll(t);
    ans=two(x);
 }while(next_permutation(s.begin(),s.end()));

 s="00000000001111";
 do{
    t="1"+s+"1";
    x=stoll(t);
    ans=two(x);
 }while(next_permutation(s.begin(),s.end()));

 s="00000000011111";
 do{
    t="1"+s+"1";
    x=stoll(t);
    ans=two(x);
 }while(next_permutation(s.begin(),s.end()));

 s="00000000111111";
 do{
    t="1"+s+"1";
    x=stoll(t);
    ans=two(x);
 }while(next_permutation(s.begin(),s.end()));

 s="00000001111111";
 do{
    t="1"+s+"1";
    x=stoll(t);
    ans=two(x);
 }while(next_permutation(s.begin(),s.end()));

 s="00000011111111";
 do{
    t="1"+s+"1";
    x=stoll(t);
    ans=two(x);
 }while(next_permutation(s.begin(),s.end()));

 s="00000111111111";
 do{
    t="1"+s+"1";
    x=stoll(t);
    ans=two(x);
 }while(next_permutation(s.begin(),s.end()));

 s="00001111111111";
 do{
    t="1"+s+"1";
    x=stoll(t);
    ans=two(x);
 }while(next_permutation(s.begin(),s.end()));

 s="00011111111111";
 do{
    t="1"+s+"1";
    x=stoll(t);
    ans=two(x);
 }while(next_permutation(s.begin(),s.end()));

 s="00111111111111";
 do{
    t="1"+s+"1";
    x=stoll(t);
    ans=two(x);
 }while(next_permutation(s.begin(),s.end()));


 s="01111111111111";
 do{
    t="1"+s+"1";
    x=stoll(t);
    ans=two(x);
 }while(next_permutation(s.begin(),s.end()));


 s="11111111111111";
 x=stoll(s);
 ans=two(x);


 return 0;
}
