#include<iostream>
using namespace std;
int main()
{
int K;
cin>>K;
int N[K];
int O[K];
for(int j = 0; j<K; j++)
cin>>N[j];
//for(int j = 0; j<K; j++)
//cout<<N[j]<<endl;
for(int l =0; l<K; l++)
{
if(N[l]==0)
cout<<"Case #"<<l+1<<": "<<"INSOMNIA"<<endl;
else{
int k[10] ={0};
//for(int i=0;i <10;i++)
//cout<<k[i]<<endl;
//for(int i=0;;i++)
int M =N[l];
int i=1;
while(k[0]*k[1]*k[2]*k[3]*k[4]*k[5]*k[6]*k[7]*k[8]*k[9] ==0)
{
M=N[l]*i;
O[l] = N[l]*i;
//cout<<i<<"		hi"<<endl;
i++;
while(M!=0)
{
k[M%10] =1;
//cout<<M%10<<endl;
//for(int i=0;i <10;i++)
//cout<<k[i]<<endl;
M = (M-M%10)/10;
}
}
cout<<"Case #"<<l+1<<": "<<O[l]<<endl;
}}
}
