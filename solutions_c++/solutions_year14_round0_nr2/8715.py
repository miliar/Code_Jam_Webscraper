#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<map>
#include<iostream>
#include<string.h>
#include<limits.h>
#include<functional>
#include<vector>
#include<utility>
#include<stdlib.h>
#define mem(a) memset(a,0,sizeof(a))
#define pb push_back
#define bx(i) binary_search(x.begin(),x.end(),i)
#define bo(i) binary_search(o.begin(),o.end(),i)
using namespace std;
inline int fastRead()
      {
        int a=0;
       char c= getchar();
         
            while (c < '0' || c>'9') c=getchar();
        
            while( c >= '0' && c <= '9' )
             {
               a = (a<<3)+(a<<1) + c-'0';
               c=getchar();
             }
        return a;
       
      }
//cout<<"Case #"<<number<<": Game has not completed"<<endl;
int main()
{
	freopen("H:\\input.txt","r",stdin);
	freopen("H:\\output.txt","w",stdout);
	int tc = fastRead();
	for(int number=1;number<=tc;number++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double r = 2.0;
		while( (double)x/r > ( (double)c/r + (double)x/(r+f)) )
		r+=f;
		double s=0;
//		cout<<s<<endl;
		double k = 2.0;
		while(k<r)
		{
			s = s + (double)c/k;
			k = k + f;
//			cout<<s<<endl;
		}
		s = s + (double)x/r;
		printf("Case #%d: %0.7lf\n",number,s);
	}
}
