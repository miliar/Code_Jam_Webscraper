#include<iostream>
#include<fstream>

using namespace std;

int main(){
	ifstream ins;
		ofstream outs;

		ins.open("B-large.in");
		outs.open("B-large.out");
		int t;
		ins>>t;
		int temp=1;
		while(t--){
			double c,f,x;
			double ev=2.0;
			bool flag=true;
			double ans=0;
			ins>>c>>f>>x;
			while(flag){
				if((x/ev)>(c/ev+x/(ev+f))){
					ans+=c/ev;
					ev+=f;
					flag=true;
				}
				else 
					flag=false;
			}

			ans+=(x/ev);
			outs<<"Case #"<<temp<<": ";
			outs.setf(ios::fixed);
			outs.setf(ios::showpoint);
			outs.precision(7);
			outs<<ans<<endl;
			temp++;
		}
		ins.close();
		outs.close();

	return 0;
}