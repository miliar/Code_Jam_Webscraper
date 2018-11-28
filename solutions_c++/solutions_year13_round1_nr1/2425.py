#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define PI 3.142
using namespace std;

int main()
{
    long long int r,t,n=0;
    
    freopen("A-small-attempt4.in","rt",stdin);
	//freopen("A-large.in","rt",stdin);
    freopen("A.out","wt",stdout);
	cin>>t;
	while(t>0)
	{
              n++;
              int c=0;
              double br=0,wr=0,tot=0,te=0,bc,wc;
              cin>>r>>te;
              while(tot<te)
              {
              if(c==0)
              {
              wr=r;
              }
              else
              {
                  wr=br+1;
              }
              br=wr+1;
              bc=PI*(br)*(br);
              wc=PI*wr*wr;
              //cout<<br<<" "<<wr<<endl;
              tot=(bc-wc)/(PI);
              //cout<<te<<" "<<tot<<endl;
              //printf("%.10f%.10f",tot,te);
              float x=(tot);
              float y=(te);
              //cout<<"diff"<<y-x;
              //cout<<x;
                           if(y-x>=0)
                           {          
                                      te-=tot;
                                      c=c+1;
                                      //cout<<c<<endl;
                           }
                           
              }
              cout<<"Case #"<<n<<": "<<c<<endl;
              t--;
    }
   //system("pause");
    return 0;
}
	
