#include<iostream>
#include<fstream>
#include<vector>
#include<iomanip>
using namespace std;

double process(double C,double F,double X){
	double ans=X/2,sum=0;
	int temp=0;
	vector<double> vec;
	vec.push_back(C/(2+F*temp++));
	int iiii=3000000;
	while(iiii--){
		vec.push_back(C/(2+F*temp)+vec[temp-1]);
		temp++;
	}
	
	for(int i=0;i<vec.size();i++){
		double temp_ans;
		temp_ans=vec[i]+X/(2+F*(i+1));
		if(temp_ans<ans)ans=temp_ans;
	
	}
	return ans;
}






int main(){
	freopen("C:\\Users\\cychan442\\Desktop\\in.txt","r",stdin);
	freopen("C:\\Users\\cychan442\\Desktop\\out.txt","w",stdout);
	int N;
	cin>>N;
	for(int ii=1;ii<=N;ii++){
		double C,F,X;
		cin>>C>>F>>X;
		cout<<fixed<<setprecision(7)<<"Case #"<<ii<<": "<<process(C,F,X)<<endl;
	
	
	}


	//cin>>N;
}