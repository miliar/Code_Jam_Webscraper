#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include <iomanip> 

using namespace std;

int main()
{
    float c, f, x,tottime,ct,xt,ctnext,xtnext,rate;
    int cases, count = 1;
    cin>>cases;
    while(cases--)
    {
          tottime = 0.0f;
          rate = 2.0f;
          cout<<"Case #"<<count<<": ";
          count++;
          cin>>c >> f >> x;
          while(1)
          {
                 ct = (float)c/rate;//(float)((float)c/(float)rate);
                 xt = (float)x/rate;//(float)((float)x/(float)rate);
                 xtnext = (float)x/(rate+f);//(float)((float)x/(float)(rate+f));
                 if((float)(xt - xtnext) < (float)ct)
                 {
                     tottime = (float)tottime + (float)xt;
                     //printf("%.7f\n",xt);
                     break;
                 }
                 rate = (float)rate + (float) f;
                 tottime 	= (float)tottime + (float)ct;
                 //printf("%.7f ",ct);
          }
          printf("%.7f\n",tottime);
         // cout << setiosflags(ios::fixed) << setprecision(7) << tottime;
          //cout<<tottime<<endl;
          
    }
    return 0;
}
