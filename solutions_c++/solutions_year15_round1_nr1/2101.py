#include <iostream>

using namespace std;

int main(){
	int cases;
	cin>>cases;
	for(int c=1;c<=cases;c++){
		int cents[10001]={};
		int n;
		cin>>n;
		int prev;
		int current;
		cin>>prev;
		cents[prev]++;
		int comi1=0;
		int comi2=0;
		int maxcaida=0;
		for(int i=0;i<n-1;i++){
			cin>>current;
			if(i<n-2)
				cents[current]++;
			if(current<prev){
				comi1+=(prev-current);
				if(prev-current>maxcaida)
					maxcaida=prev-current;
			}
			prev=current;
		}
		for(int i=maxcaida;i<10001;i++){
			comi2+=cents[i];
			//if(cents[i]!=0)
			//	cout<<"mas 1\n";
		}
		comi2=comi2*maxcaida;
		for(int i=0;i<maxcaida;i++)
			comi2+=i*cents[i];
		//cout<<maxcaida<<endl;
		//cout<<cents[5];
		cout<<"Case #"<<c<<": "<<comi1<<' '<<comi2<<endl;

	}


	return 0;
}