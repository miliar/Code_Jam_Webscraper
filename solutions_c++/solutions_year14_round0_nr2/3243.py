#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int T, l;
double c, f, x;

void doit(){
	double rate = 2, lefttime, usedtime = 0, lefttime2;
	while (1){
		lefttime = x / rate;
		lefttime2 = c / rate + x / (rate + f);
		//cout<<lefttime<<" "<<lefttime2<<endl;
		//cin>>l;
		if (lefttime < lefttime2){
			usedtime += lefttime;
			break;
		}
		else{
			usedtime += c / rate;
			rate += f;
		}
	}
	
	printf("%.7lf\n", usedtime);
}

int main(){
 	freopen("B0.in","r",stdin);
 	freopen("B0.out","w",stdout);
	cin>>T;
	for (int cs = 1; cs <= T; cs ++){
		cin>>c>>f>>x;
		printf("Case #%d: ", cs);
		doit();
	}
	return 0;
}
