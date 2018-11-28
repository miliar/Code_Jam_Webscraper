#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

double P[220];
int N,K;

vector<double> chosen;
vector<double> actual;
double max_prob_submitted;

double calc_prob(){
	double sum_prob[K+1]={1,0};
	for(int i=0;i<K;i++){
		double tmp_prob[K+1]={0};

		double this_prob=chosen[i];
		for(int j=0;j<K+1;j++)
			tmp_prob[j]+=(1-this_prob)*sum_prob[j];
		for(int j=0;j<K;j++)
			tmp_prob[j+1]+=(this_prob)*sum_prob[j];
		for(int j=0;j<K+1;j++)sum_prob[j]=tmp_prob[j];
	}
	return sum_prob[K/2];
}

void submit(){
	double my_prob=calc_prob();
	if(my_prob>max_prob_submitted){
		actual=vector<double>(chosen);
	}
	max_prob_submitted=max(max_prob_submitted,my_prob);
}

void search(int n,int kremain){
	//cout<<"Search"<<n<<":"<<kremain<<endl;
	if(n==N){
		if(kremain==0)
			submit();
		return;
	}

	if(kremain>0){
		chosen.push_back(P[n]);
		search(n+1,kremain-1);
		chosen.pop_back();
	}
	search(n+1,kremain);
}


void Calc(){
	cin>>N>>K;
	for(int i=0;i<N;i++)cin>>P[i];

	
	//for(int i=0;i<N;i++)
	//	P[i]=(rand()%100)/100.0;
	//cout<<"P:"<<P[0]<<endl;
	//P[0]=0.01;P[1]=0.01;P[2]=0.5;P[3]=0.75;P[4]=0.99;P[5]=0.52;
	//P[0]=0;P[1]=1;P[2]=2;P[3]=3;
	max_prob_submitted=-1;
	search(0,K);

	cout<<max_prob_submitted;
	//cout<<"actual=";
	//for(auto v:actual)cout<<v<<";";
		cout<<endl;
		/*
	sort(P,P+N);
	int M=K/2;
	chosen.clear();
	for(int i=0;i<M;i++)chosen.push_back(P[i]);
	for(int i=0;i<M;i++)chosen.push_back(P[N-i-1]);

	cout<<"chosen=";
	for(auto v:chosen)cout<<v<<";";
		cout<<endl;

	double optim_prob=calc_prob();
	cout<<"test_optim_prob:"<<optim_prob<<endl;
	*/

	/*
	double valmin=2,valmax=-1;
	for(int i=0;i<N;i++){
		valmin=min(valmin,P[i]);
		valmax=max(valmax,P[i]);
	}*/
	//cout<<"Est pb minmax:"<<(valmin*(1-valmax)+ (valmax)*(1-valmin))<<endl;
}

int main(){
	
	int T;cin>>T;for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		Calc();
	}
	return 0;
}
