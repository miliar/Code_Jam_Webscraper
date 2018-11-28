#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main(){
	int t=0,n=0;
	cin>>t;
	while (n<t){
		n++;
		double c,f,x,t=0,cook_sec=2;
		cin>>c>>f>>x;
		while((x/cook_sec)>((c/cook_sec)+(x/(cook_sec+f)))){
			t+=c/cook_sec;
			cook_sec+=f;
		}
		t+=x/cook_sec;
		
		cout<<"Case #"<<n<<": ";
		cout.precision(9);
		cout << t;
		if(fmod(t,1)==0){
			printf(".");
			for(int i=0;i<7;i++)
				printf("0");	
		}
			
		cout<<endl;

	}
	return 0;
}
