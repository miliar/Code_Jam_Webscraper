#include<bits/stdc++.h>
//#define gc getchar_unlocked
#define gc getchar
#define ll long long 
using namespace std;

//standing, number , shyness
int difr(int a,int b,int i){
	if(b==0 || i==0)
		return 0;
    int x=a-b;
    if(x<0)
    	x=b-a;
    //cout<<a<<"  "<<b<<"  "<<x<<"  "<<endl; 
    return x;
}

int main(){
	int T;
	cin>>T;
	for(int k=1;k<=T;k++){

		//stand count,requirement 
		vector<pair<int ,int> > vec;

		int x;
		char str[1555];
		cin>>x>>str;
		int ars[10000]={0};
		for(int i=0;i<=x;i++){
			int x=str[i]-'0';
			if(x>0){
				vec.push_back(make_pair(x,i));
			}
		}

       // for(int i=0;i<=x;i++)cout<<ars[i]<<"  ";
        //cout<<endl;
        int stoodup=0;
        int ans=0,ans1=0,finans=0;

        
		for(int i=0;i<vec.size();i++){
			ans1=0;
		    //cout<<"befor "<<i<<"  "<<stoodup<<"   "<<ars[i]<<"  "<<ans<<"   "<<endl;
			if(stoodup<vec[i].second){
				ans+=vec[i].second-stoodup;
				stoodup+=vec[i].second-stoodup;
			}

            stoodup+=vec[i].first;


			//cout<<"after "<<i<<"  "<<stoodup<<"   "<<ars[i]<<"  "<<ans<<"   \n"<<endl;

		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
}