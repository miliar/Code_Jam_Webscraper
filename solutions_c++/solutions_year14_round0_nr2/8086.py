#include <iostream>
#include <cstdio>
using namespace std;

double c,f,x;

double curc,curt;

int curf;

int gt;

int main() {
    // your code goes here
	freopen("inp.txt","rt",stdin);
    //freopen("out.txt","wt",stdout);

	cin>>gt;
    //gt=1;
	for(int run=1;run<=gt;run++)
	{
		cin>>c>>f>>x;
		curc=0.0;
		curf=0;
		curt=0.0;

		while(true){
			if(curc<c){
				double t1= c-curc;
				t1=t1/(curf*f+2.0);
				if(t1*2+ curf*f*t1 +curc > x ) break;
				curt+= t1;
				curc+= (t1*2+curf*f*t1);
			    //flag=1;
            }
			else{
				double t1= c/f;
				if(curc+t1*2+curf*f*t1>=x) break;
				curc=curc-c;
				curf++;
			}
		}
		curt+= (x-curc)/(2.0+curf*f);

        printf("Case #%d: %0.9f\n",run,curt);
	}





	return 0;
}
