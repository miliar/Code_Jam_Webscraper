#include<bits/stdc++.h>
using namespace std;

#define st_clk double st=clock();
#define end_clk double en=clock();
#define show_time cout<<"\tTIME="<<(en-st)/CLOCKS_PER_SEC<<endl;


#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);

int main(){
	 #ifndef ONLINE_JUDGE
     f_in("in");
     f_out("out");
     #endif
     int t;
     scanf("%d",&t);
     int case1 = 0;
     while(t--){
     	case1++;
         double c,f,x;
         cin >> c >> f >> x;
         double init = x/2;
         double next = (c/2) + (x/(2+f));
         double toadd = c/2;
         int index = 1;
        // cout << init << " " << next << endl; 
		 while(next<init){
		      toadd += c/(2+(index)*f);
		      index++;
		      init = next;
		      double old = (x/(2 + ((index-1)*f)));
		      next =  toadd + (x/(2 + (index*f)));
		     // cout << init << " " << next << endl;
		 }
		 printf("Case #%d: %0.7f\n",case1,init);
	 }
}

