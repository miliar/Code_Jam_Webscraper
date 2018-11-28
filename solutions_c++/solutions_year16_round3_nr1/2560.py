#include <bits/stdc++.h> 
#define si(a) scanf("%d",&a)
#define ll long long 
#define MOD 1000000007
using namespace std ;
vector < pair<int,int> > v;
string res ;
bool compare(pair<int,int> a,pair<int,int> b){
	return a.second > b.second ;
}
int main(){
	int t,i,j,k,n,z;
	si(t);
	for(z=1;z<=t;z++){
		int arr[26]={0},total = 0 ;
		si(n);
		v.clear();
		for(i=0;i<n;i++){
			si(arr[i]);
			v.push_back(pair<int,int>(i,arr[i]));
			total = total + arr[i];
		}
		pair<int,int> p1,p2;
		char ch1,ch2 ;

		res = "";
		while(total>0){
			sort(v.begin(),v.end(),compare);
			// cout<<total<<"\n";
			// for(i=0;i<v.size();i++){
			// 	printf("%d %d\n",v[i].first,v[i].second);
			// }
			p1 = v[0],p2 = v[1];
			ch1 = p1.first + 'A' , ch2 = p2.first + 'A';
			int mx = p1.second , sx = p2.second ;
			if(total==2){
				res = res + ch1 + ch2;
				total -= 2 ;
			}
			else{
				if(mx>=2){
					mx -= 2 ;
					total -= 2 ;
					v[0].second -= 2;
					mx = max(sx,mx);
					if(mx<=total/2){
						res = res + ch1 + ch1 + ' ';
					} 
					else{
						total += 1;
						v[0].second +=1;
						mx = max(v[0].second,sx);
						if(mx<=total/2){
							res = res + ch1 + ' ';
						}
						else{
							total -= 1;
							v[1].second -=1;
							res = res + ch1 + ch2 + ' ';
						}
						
					}
					
				}else{
						mx -= 1;
						total -=1;
						v[0].second -=1;
						mx = max(mx,sx);
					if(mx<=total/2){
						res = res + ch1 + ' ';
					}
					else{
						total -= 1;
						v[1].second -=1;
						res = res + ch1 + ch2 + ' ';
					}
				}
			}

		}

		cout<<"Case #"<<z<<": ";
		cout<<res;
		printf("\n");
	}

}