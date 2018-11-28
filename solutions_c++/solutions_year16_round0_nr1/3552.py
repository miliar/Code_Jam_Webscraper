#include<iostream>
#include<fstream>
#include<cstdlib>
using namespace std;
class sol{
public:
	long long count(long long n){
		int num=0;
		if(n==0)
			return -1;
		for(int i=0;i<10;i++){
			tb[i]=false;
		}
		int zeos=0;
		while(n%10==0){
			if(!tb[0]){
				tb[0]=true;
				num++;
			}
			n/=10;
			zeos++;
		}
		long long now=n;
		int mult=1;
		while(num!=10){
			if(mult%10==0){
				if(mult==10&&!tb[0]){
					num++;
					tb[0]=true;
				}
			}
			else
				process(now,num);
			if(num==10){
				for(int i=0;i<zeos;i++)
					now*=10;
				return now;
			}
			now+=n;
			mult++;
		}
	}
	void process(long long n,int& num){
		int now;
		while(n!=0){
			now=n%10;
			if(!tb[now]){
				num++;
				tb[now]=true;
			}
			n/=10;
		}
	}
private:
	bool tb[10];
};
int main(){
	ifstream is("A-large.in");
	ofstream os("Output.txt");
	sol s;
	int num;
	is>>num;
	long long cse;
	long long result;
	for(int i=1;i<=num;i++){
		is>>cse;
		result=s.count(cse);
		if(result==-1){
			//cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			os<<"Case #"<<i<<": INSOMNIA\n";
		}
		else{
			//cout<<"Case #"<<i<<": "<<result<<endl;
			os<<"Case #"<<i<<": "<<result<<"\n";
		}
	}
	is.close();
	os.close();
}