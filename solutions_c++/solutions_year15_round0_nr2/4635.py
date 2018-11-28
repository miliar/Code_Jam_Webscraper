#include <iostream>
#include <algorithm>
#include <limits>
#include <queue>
#include <vector>
#include <cmath>
#include <sstream>
#include <fstream>
using namespace std;

int g=0;

int f (int buffer, int limit, vector<int> ar){
	g++;
	std::vector<int> br = ar;
	std::vector<int> cr = ar;
	//cout<<buffer<<" "<<limit;
	//buffer--time spent;limit-- time allowed;ar--sorted
	if(buffer>limit) return 10000;

	int D = ar.size();
	//cout<<"buf: "<<buffer<<" "<<D<<" "<<limit<<" "<<g<<endl;
	int max = ar[D-1];
	//cout<<max;
	int nummax = 0;
	if(max ==1){
		return 1;
	}

	for(int i=0;i<D;i++)
	{
		br[i]--;
	}

	ar.pop_back();
	if(max%2==0){
			ar.push_back(max/2);
			ar.push_back(max/2);	
		}
	else{
			ar.push_back((max+1)/2);
			ar.push_back((max-1)/2);
		}

	//divide into 3
	int flag = 0;
	if(max%3==0&&max!=3){
		//cout<<"asd";
		cr.pop_back();
		cr.push_back(max/3);
		cr.push_back(max/3);
		cr.push_back(max/3);
		flag = 1;
	}

	// for(int i=D-1;i>=0;i--)
	// {
	// 	if(ar[i]==max)
	// 	{
	// 		nummax ++;
	// 		ar.pop_back();
	// 	}
	// 	else {
	// 		break;
	// 	}
	// }
	// for(int i=0;i<nummax;i++)
	// {
	// 	if(max%2==0){
	// 		ar.push_back(max/2);
	// 		ar.push_back(max/2);	
	// 	}
	// 	else{
	// 		ar.push_back((max+1)/2);
	// 		ar.push_back((max-1)/2);
	// 	}
			
	// }
	
	sort(ar.begin(),ar.end());
	int ans = f(buffer+1,limit,ar);
	int ans2 = 1+f(buffer+1,limit,br);
	//cout<<ans<<" "<<ans2<<" "<<buffer<<" "<<max<<" "<<nummax<<endl;
	int as = min(1+ans,ans2);
	//if(ans2<nummax+ans){cout<<"HURRAY!!"<<as<<" " <<nummax+ans;}
	//cout<<max<<" "<<ans<<" "<<buffer<<" "<<nummax<<" "<<g<<endl;
	if (flag = 0){ return as;}
	//return as;//min(max,as);
	else{
		sort(cr.begin(),cr.end());
		int t = 2+f(buffer+2,limit,cr);
		//cout<<t;
		as = min(as,t);
		return as;
	}
}


int main(){
	int T;
	int Tn;
	cin>>T;
	Tn = T;
	//freopen("A.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	while(T--){
		int D;cin>>D;
		//string sh;
		vector<int> ar;
		
		//cin>>sh;
		for(int i=0;i<D;i++)
		{
			int p;
			cin>>p;
			ar.push_back(p);
			//cout<<ar[i]<<endl;
		}
		sort(ar.begin(),ar.end());

		//cout<<(ar.back());
		int ans = f(0,ar[D-1],ar);
		cout<<"Case #"<<(Tn-T)<<": "<<ans<<endl;
	}
}
