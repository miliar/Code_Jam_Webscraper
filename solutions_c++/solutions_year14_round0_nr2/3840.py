#include<iostream>
#include<cmath>
#include<cstdio>

using namespace std;
int main()
{
 
 int arr[5][5];
 int brr[5][5];
 int t,i,j,cases;
 cin>>t;
 double c,f,x, res, curcost, rate;
 int numMatches =0;
 for(cases=1;cases<=t;cases++)
 { 
  curcost = 0.0;
  rate = 2.0;
  cin >> c >> f >> x;
  res = x/rate; // no purchase time
  bool flag = true;
  while (flag) {
    curcost += (c/rate); 
    rate+= f;
    double newcost = curcost +(x/rate);
    if(newcost < res)
      res =newcost;
    else 
      break; 
  }                            
  //cout<<"Case #"<<cases<<": "<< res <<"\n";
  printf("Case #%d: %.7f\n",cases,res);  
}
return 0;
}