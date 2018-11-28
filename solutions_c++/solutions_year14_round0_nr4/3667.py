#include<iostream>
#include<cmath>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
 
 vector<double> naomi;
 vector<double> ken;
 int t,i,j,n,cases;
 cin>>t;
 double c,f,x, res, curcost, rate;
 int numMatches =0;
 for(cases=1;cases<=t;cases++)
 { 
  cin >> n;
  naomi.clear();
  ken.clear();
  for (i = 0; i <n; ++i) 
  {
      double temp;
      cin >> temp;
      naomi.push_back(temp);                            
  }
  std::sort(naomi.begin(), naomi.end());
  for (i = 0; i <n; ++i) 
  {
      double temp;
      cin >> temp;
      ken.push_back(temp);                            
  }
  std::sort(ken.begin(), ken.end());
  int ni =0,ki =0;
  int ncount =0, kcount =0;
  while(ni <n && ki <n)
  {
     if(naomi[ni] >= ken[ki])
     {
         ++ni;
         ++ki;
         ++ncount;
     } else 
     {
            ++ni;
     }
  }
  if(ni <n)
    ncount+= (n-ni);

  ni=0; ki =0;
    while(ni <n && ki <n)
  {
     if(ken[ki] >= naomi[ni])
     {
         ++ni;
         ++ki;
         ++kcount;
     } else 
     {
            ++ki;
     }
  }
   if(ki <n)
    kcount+= (n-ki);
    //cout<<"Case #"<<cases<<": "<< res <<"\n";
  printf("Case #%d: %d %d\n",cases,ncount, n-kcount);  
 }
return 0;
}