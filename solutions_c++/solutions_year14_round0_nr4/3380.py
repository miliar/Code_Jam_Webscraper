#include<iostream>
#include<cmath>
#include<cstdio>
#include<fstream>
#include<deque>
#include<algorithm>
using namespace std;
int main(){
	 ifstream myfile;
	 myfile.open("data.txt");
	FILE *fp = freopen ("myfile.txt","w",stdout);
	int tc;
	myfile>>tc;
	for (int cc=0;cc<tc;cc++){
		int no, y, z;
		deque<float> k1, n1;
		myfile>>no;
		for(int row=0;row<no;row++){
			float temp;
			myfile>>temp;
			n1.push_back(temp);
			
		}
		for(int row=0;row<no;row++){
			float temp;
			myfile>>temp;
			k1.push_back(temp);
		}
		if(no>1){
			deque<float> k(k1);
			deque<float> n(n1);
			for(int ll=0;ll<no;ll++){
				sort(k.begin(), k.end());
				sort(n.begin(), n.end());
				
				//playing optimally
				//cout<<n.size()<<endl;
			//for(int vv=0;vv<n.size();vv++){
			//		cout<<k[vv]<<" "<<n[vv]<<endl;
			//	}
			//	cout<<k.back()<<" a"<<n.front()<<endl;
				if(k.back()<n.front()){
					y=n.size();
					break;
				}
				
				float cur=n.front();
			//	cout<<cur<<endl;
				n.pop_front();
			//	cout<<n.front()<<endl;
				for(int dd=0;dd<no;dd++){
					if(k[dd]>cur){
						k.erase(k.begin()+dd);
						break;
					}
				}
				
			}
			if(n.size()==0)y=0;
			
			deque<float> k2(k1);
			deque<float> n2(n1);
			for(int ll=0;ll<no;ll++){
				sort(k2.begin(), k2.end());
				sort(n2.begin(), n2.end());
				
				//playing deceptively
			
				//	for(int vv=0;vv<n2.size();vv++){
				//	cout<<k2[vv]<<" "<<n2[vv]<<endl;
			//	}
			//	cout<<k2.back()<<" a"<<k2.front()<<" "<<n2.back()<<" "<<n2.front()<<endl;
					
				
				
				if((k2.front()<n2.front()) && (k2.back()<n2.back())){
					z=n2.size();
					break;
				}
				
				n2.pop_front();
				k2.pop_back();
			
				
			}
						if(n2.size()==0)z=0;
			int tt=n2.size();
			for(int ll=0;ll<tt;ll++){
				sort(k2.begin(), k2.end());
				sort(n2.begin(), n2.end());
				
				//playing deceptively
			//
			//		for(int vv=0;vv<n2.size();vv++){
			//	cout<<k2[vv]<<" "<<n2[vv]<<endl;
			//	}
			//	cout<<k2.back()<<" a"<<k2.front()<<" "<<n2.back()<<" "<<n2.front()<<endl;
					
				
				
				float cur=k2.front();
			//	cout<<cur<<endl;
				k2.pop_front();
			//	cout<<n.front()<<endl;
				for(int dd=0;dd<n2.size();dd++){
					if(cur<n2[dd]){
						n2.erase(n2.begin()+dd);
						break;
					}
				}
			
				
			}
			z-=n2.size();
		}else{
			if(k1[0]>n1[0]){
				y=0;
				z=0;
			}else{
				y=1;
				z=1;
			}
		}
			printf("Case #%d: %d %d\n", cc+1, z, y);
	
	
		
	}
	  fclose (stdout);
}
