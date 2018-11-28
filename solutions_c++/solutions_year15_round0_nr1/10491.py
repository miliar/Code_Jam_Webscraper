#include<iostream>
#include<fstream>

using namespace std;

int main(){
    ifstream in("ova.in");
    ofstream out("ova.out");
    int n;
    in>>n;
    for(int i=0;i<n;i++){
		int r=0;//result
		int s=0;//standing
		char m=0;
		in>>m;
		m-=48;
		for(int j=0;j<=m;j++){
			int d=0;
			char a;
			in>>a;
			int b=int(a-48);
			//cout<<b;//current amount
			//current standing < current shyness
			if(s<j && b>0){
				d=j-s;
				//cout<<s<<" "<<j<<" "<<d<<" ";
				
			} else {
			}
			s+=b;
			r+=d;
			s+=d;

		}
		out<<"Case #"<<i+1<<": "<<r<<"\n";
		//cout<<r<<"\n";
    }


    return 0;
}
