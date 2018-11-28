#include<iostream>
#include<stdio.h>
#include<cstring>
#include<stdlib.h>
#include <queue>
#include<string>
#include <sstream>
#include<list>
#include<map>
#include<cmath>
#include<algorithm>

using namespace std;
#define INF 1e9
#define DIVIDE 10000


int main()
{
	long long input,index = 0,length;
	freopen ("d:/Codejam/A-small-attempt0(1).in","r",stdin);
	freopen ("d:/Codejam/A-small-attempt0(1).out","w",stdout);
	scanf("%lld",&input);
	long long ans=0, P,Q,j,i;
	string given;
	while(input--){
		cin>>given;
       P=0;
	   Q=0;
       i=0;
	   ans =0;
       while(given[i]!='/')
	   {
           P = P*10+(given[i]-'0');//convert
           i++;
       }
       i++;
       length =given.size();

       while(i<length)
	   {
           Q = Q*10 + (given[i]-'0');//convert
		   i++;
       }
       for( j=2;j*j<=P;j++)
	   {
           while(P%j==0&&Q%j==0)
		   {
               P/=j;
               Q/=j;
           }
       }
       ans=0;
       while(Q%2==0&&Q>P){
           Q/=2;ans++;
       }
       while(Q%2==0){
           Q/=2;
       }

		printf("Case #%lld: ",++index);

		if(Q==1)
			cout<<ans;
		else 
			cout<<"impossible";
		cout<<endl;
	}
	return 0;
}