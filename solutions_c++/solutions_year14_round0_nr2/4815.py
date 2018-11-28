#include <iostream>
#include <stdio.h>
#include <map>

using namespace std;

int n;
int times;
map<int,int> h;
double x,y,z;
const double eps=1e-7;

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>times;
	for (int ti=1;ti<=times;ti++){
		cin >> x>>y>>z;
		double sp=2;
		double tot=0;
        while (1){
              double now = z*1.0/sp;
              double ti = x*1.0/sp+z*1.0/(sp+y);
              if (now-ti>eps){
                 tot+=x*1.0/sp;
                 sp+=y;
              }else{
                    tot+=now;
                    break;
              }
        }
		//cout<<"Case #"<<ti<<": ";
		printf("Case #%d: %lf\n",ti,tot);
	}
	return 0;
}
