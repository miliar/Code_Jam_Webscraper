#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	long double c,f,x,ct = 2.0,tot = 0.0;
	int flag = 0;
	int t;
	scanf("%d",&t);
	for(int i = 0 ; i < t; i++){
		scanf("%LF %LF %LF",&c,&f,&x);
		tot = 0.0;
		flag = 0;
		ct = 2.0;
		while(flag == 0){
			if((x/ct) > (c/ct)+(x/(ct+f))){
				tot+=(c/ct);	
				ct+=f;
			}else{
				tot+=(x/ct);
				flag = 1;	
			}	
			//cout << tot << "  "; 
		}
		//cout << endl;
		printf("Case #%d: %.7LF\n",i+1,tot);
	}
	return 0;
}
