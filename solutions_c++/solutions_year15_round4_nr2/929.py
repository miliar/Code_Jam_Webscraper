#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
using namespace std;  
struct tap{
	long double s,t;
    bool operator<(const tap ext) const{
    return (t<ext.t);
    }
};
int main(){
                cout.setf(ios::fixed,ios::floatfield);
        cout.precision(12);
    long long z,t,n,i,j,k;
    tap tp[100];
    long double v,x,ans,vv,xx;
    long double mi,ma,mid,temp,pt;
    bool ok,wok;
    cin>>t;

    for (z=1; z<=t; ++z){
      cin>>n>>v>>x;
    //  if (z==28)
     // cout<<n<<" "<<v<<" "<<x<<endl;
      ok=true;
      for (i=0; i<n; ++i)
          cin>>tp[i].s>>tp[i].t;
      if ((n==1) && (tp[0].t!=x))
         ok=false;
      sort(tp,tp+n);
      for (i=0; i<n; ++i)
     // cout<<tp[i].s<<" "<<tp[i].t<<endl;
      if (n>1){
         if ((x<tp[0].t) || (x>tp[n-1].t))
            ok=false;
      }
      if (ok){
         if (n==1){
            ans=v/tp[0].s;
         }
         else if (x==tp[0].t){
              vv=0;
              for (i=0; i<n; ++i){
                  if (tp[i].t==x)
                  vv+=tp[i].s;
              }
              ans=v/vv;
         }
         else if (x==tp[n-1].t){
              vv=0;
              for (i=0; i<n; ++i){
                  if (tp[i].t==x)
                  vv+=tp[i].s;
              }
              ans=v/vv;
         }
         else{
              mi=0;
              ma=100000001;
              while (ma-mi>1e-12){
                    wok=true;

                    mid=(mi+ma)/2;
                  //                      cout<<"LOOP: "<<mid<<endl;
                    vv=0;
                    xx=0;
                    for (i=0; i<n; ++i){
                        vv=vv+tp[i].s*mid;
                        xx=xx+tp[i].s*tp[i].t*mid;
                    }
                    xx=xx/vv;
                  //  cout<<vv<<" "<<xx<<endl;
                    if(vv<v){
                             wok=false;
                    }
                    else if (abs(xx-x)>1e-18){
                       if (xx>x){ //remove the hot water
                          for (i=n-1; i>=0; --i){
                              temp=vv*xx-tp[i].s*tp[i].t*mid;
                              temp=temp/(vv-tp[i].s*mid);
                         //     cout<<i<<": "<<tp[i].t<<" "<<temp<<endl;
                              if (temp>x){
                                 if (vv-tp[i].s*mid<v)
                                 {
                                    wok=false;
                                    break;
                                 }
                                 else{
                                      vv=vv-tp[i].s*mid;
                                      xx=temp;
                                 }
                              }
                              else{//ok
                                  pt=vv*(xx-x)/(tp[i].t-x);
                            //      cout<<pt<<endl;
                                  if (vv-pt<v)
                                     wok=false;
                                  break;     
                              }
                          }
                       }
                       else{ //remove the cold water
                          for (i=0; i<n; ++i){
                              temp=vv*xx-tp[i].s*tp[i].t*mid;
                              temp=temp/(vv-tp[i].s*mid);
                           //   cout<<i<<": "<<tp[i].t<<" "<<temp<<endl;
                              if (temp<x){
                                 if (vv-tp[i].s*mid<v)
                                 {
                                    wok=false;
                                    break;
                                 }
                                 else{
                                      vv=vv-tp[i].s*mid;
                                      xx=temp;
                                 }
                              }
                              else{//ok
                                  pt=vv*(xx-x)/(tp[i].t-x);
                               //   cout<<"PT: "<<pt<<endl;
                                  if (vv-pt<v)
                                     wok=false;
                                  break;     
                              }
                          }
                       }
                    }
                    if (wok)
                       ma=mid;
                    else
                        mi=mid;
              } //end of while
              ans=mid;
         }
      } //end of if ok
      if (ok)
         cout<<"Case #"<<z<<": "<<ans<<endl;
      else
      cout<<"Case #"<<z<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}
