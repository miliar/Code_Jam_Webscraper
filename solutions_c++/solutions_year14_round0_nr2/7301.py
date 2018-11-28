#include<iostream>
#include<cstdio>
using namespace std;
int main(){
	int t, T;
	double c, f, x;
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
    cin>>T;
    t = T;
    while(T--){
    	cin>>c>>f>>x;
    	int n = (int)((x*f-2*c)/(c*f));
    	if(n < 0) n = 0;
    	double time = 0;
    	for(int i = 0 ; i < n; i++)
     {
       time += c/(2+i*f);
     }
     time += x/(2+n*f);
    printf("Case #%d: %0.7f\n",t-T, time);
    }
}
