#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
int main(int argc,char **argv)
{
    freopen("B_in.txt", "r", stdin);
	freopen("B_out.txt", "w", stdout);
    int cnt; 
	cin >> cnt;
	double c,f,x;
	for(int i=1;i<=cnt;i++){
		printf("Case #%d: ", i);
		scanf("%lf %lf %lf",&c,&f,&x);
		double st_f=2.0,res_n=0.0;
		while(1){
			double x_t=x/st_f;
			double y_t=x/(st_f+f)+c/st_f;
			if(x_t<=y_t){
				res_n+=x_t;
				break;
			}
			else{
				res_n+=c/st_f;
				st_f+=f;
			}
		}
		printf("%.7lf\n",res_n);
	}
} 
