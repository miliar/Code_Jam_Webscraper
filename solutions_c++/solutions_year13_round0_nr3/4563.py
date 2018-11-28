// dtb @ gcj'13
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

#define INFILE "./csmall.in"
#define OUTFILE "./csmall"

using namespace std;

bool pal (unsigned long long arg) {
		unsigned long long rev=0,num=arg;
		while (num) {
				rev=rev*10+num%10;
				num/=10;
		}

		return (arg==rev);
}


int main () {

		freopen (INFILE,"r",stdin);
		freopen (OUTFILE,"w+",stdout);

		unsigned long long x,y,count,min,max;
		int T,caseNum=0;

		for (scanf("%d",&T);T;T--) {
				count=0;
				cin >> x >> y;
				min=sqrt(x);
				max=sqrt(y);
				if (min*min < x)
						min+=1;
				for (int i=min;i<=max;i++) {
						if (pal(i))
								if(pal(i*i))
										count++;
				}

				cout << "Case #"<<++caseNum<<": "<<count<<endl;
		}
}



				
