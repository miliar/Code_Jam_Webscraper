#include<iostream>
#include<fstream>
#include<algorithm>

using namespace std;
int main()
{
    int t;
    FILE *in,*o;
    o = fopen ("output.txt","w");
    cin>>t;
    double c,f,x;
    int k =1;
    double ans= 0;;
    double time =0;
    double x1=0,x2=0;
    double T = 2.0;
    while (k<=t){
            T = 2.0;
            ans = 0;
          cin>>c>>f>>x;
          while (1){
                    if (x/T > ((c/T)+(x/(T+f)))) {
                     ans =ans + (c/T);
                     T = T + f;
                    }
                    else {
                        ans = ans + (x/T);
                        break;
                    }
          }
        fprintf(o,"Case #%d: %.7lf\n",k,ans);
        k++;
    }
    return 0;
}
