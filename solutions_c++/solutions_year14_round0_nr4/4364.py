#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;


int PlayWar(vector<double> FirstPlayer,vector<double> SecondPlayer){
	int winSecondPlayer=0;
	int i,j;
	i=j=0;
	for(;i<FirstPlayer.size()&&j<SecondPlayer.size();i++,j++){
		if(FirstPlayer[i]>SecondPlayer[j]){
			for(;j<SecondPlayer.size()&&FirstPlayer[i]>SecondPlayer[j];j++);
		}
		if(j==SecondPlayer.size())
			break;
		winSecondPlayer++;
		
	}
	
	return FirstPlayer.size()-winSecondPlayer;
}


int main(){
	
	int T,N;
	cin>>T;
	for(int testcase=1;testcase<=T;testcase++){
		cin>>N;
		vector<double> Naomi(N),Ken(N);
		for(int i=0;i<N;i++)
			cin>>Naomi[i];
		for(int i=0;i<N;i++)
			cin>>Ken[i];
		
		sort(Naomi.begin(),Naomi.end());
		sort(Ken.begin(),Ken.end());
		
		cout<<"Case #"<<testcase<<": "<<Naomi.size()-PlayWar(Ken,Naomi)<<" "<<PlayWar(Naomi,Ken)<<endl;
		
		
	}
	
	return 0;
}
