#include<iostream>
#include<cstdio>
#include<set>
#include<cstring>

using namespace std;
typedef  pair<int,int> pii;
int D;
multiset<int> se;
multiset<int>::iterator it;
void nhap(){
	cin>>D;
	int x;
	se.clear();
	for(int i=1 ; i<=D;i++){
		cin>>x;
		se.insert(x);
	}	
}
int proce1(multiset<int> se){
	int ans1 = 0,ans2 = 0,n,p,temp,dem,maxp;	
	while(!se.empty()){
		n = se.size();		
		it = se.end(); it-- ; p = *it;
		dem = 0;
		while(*it == p){
			dem++;
			if(it == se.begin()) break;
			it--;
		}
		if(it == se.begin()) maxp =0;
		else maxp =*it;
		
		temp = (p - ans2)/2;
		if((p-ans2)&1) temp++;
		if(p - ans2 - dem > temp&&temp >maxp){
			ans1 += 2*dem;
			it = se.end(); it-- ;
			for(int i = 1; i<= dem ;i++){
				it = se.end(); it-- ;
				se.erase(it);		
			}
			temp = p - ans2;
			for(int i = 1; i <= dem ;i++){
				if(temp%3 == 0){
					se.insert(temp/3 + ans2);
					se.insert(temp/3 + ans2);
					se.insert(temp/3 + ans2);
				}else if(temp%3 == 1){
					se.insert(temp/3 + ans2);
					se.insert(temp/3 + ans2);
					se.insert(temp/3 + ans2 + 1);
				}else if(temp%3 == 2){
					se.insert(temp/3 + ans2);
					se.insert(temp/3 + ans2+1);
					se.insert(temp/3 + ans2+1);
				}
			}
		}		
		else if((p - ans2 - dem) > temp){
			ans1 += dem;
			it = se.end(); it-- ;
			for(int i = 1; i<= dem ;i++){
				it = se.end(); it-- ;
				se.erase(it);		
			}
			for(int i = 1; i <= dem ;i++){
				se.insert(temp + ans2);
				se.insert(p - temp);
			}
		}else ans2++;
						
		it = se.begin();
		while(*it <= ans2){
			se.erase(it);
			if(se.empty()) break;
			it = se.begin();
		}
		
	}
	return ans1+ans2;
}
int proce2(multiset<int> se){
	int ans1 = 0,ans2 = 0,n,p,temp,dem,maxp;	
	while(!se.empty()){
		n = se.size();		
		it = se.end(); it-- ; p = *it;
		dem = 0;
		while(*it == p){
			dem++;
			if(it == se.begin()) break;
			it--;
		}
		if(it == se.begin()) maxp =0;
		else maxp =*it;
		
		temp = (p - ans2)/2;
		if((p-ans2)&1) temp++;
		
		if((p - ans2 - dem) > temp){
			ans1 += dem;
			it = se.end(); it-- ;
			for(int i = 1; i<= dem ;i++){
				it = se.end(); it-- ;
				se.erase(it);		
			}
			for(int i = 1; i <= dem ;i++){
				se.insert(temp + ans2);
				se.insert(p - temp);
			}
		}else ans2++;
						
		it = se.begin();
		while(*it <= ans2){
			se.erase(it);
			if(se.empty()) break;
			it = se.begin();
		}
		
	}
	return ans1+ans2;
}
int main(){
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int t;
	cin>>t;
	for(int i = 1; i<=t;i++){
		nhap();				
		int ans = min(proce1(se),proce2(se));
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
		
	return 0;
}

