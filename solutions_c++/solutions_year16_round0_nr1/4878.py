/*
#include <bits/stdc++.h>

typedef struct cords cords;

using namespace std;

struct cords
{
	lli y1,y2;
};
*/

#include <iostream>
#include <algorithm>
#include <vector>

//#include <pair>


using namespace std;
typedef long long int lli;
typedef unsigned int ui;
typedef unsigned long long int ulli;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define loop2(i,size) for(ui i=0;i<size;i++)
#define loop(i,begin,end) for(ui i=begin;i<=end;i++)

class mySet{
	bool p[10];
	int size;
public:
	mySet(){
		loop2(i,10){ p[i]=0;}
		size=0;
	}
	void put(int x){
		if(p[x]==0){
			p[x]=1;
			size+=1;
		}
	}
	int getSize(){
		return size;
	}
	void clear(){
		loop2(i,10){p[i]=0;}
		size=0;
	}
};
int main(){
	ulli t,n,i=0,ans,tmp,kn;
	mySet s=mySet();
	cin>>t;
	while(i++ < t){
		cin>>n;
		if(n==0){
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		}else{
			s.clear();
			kn=n;
			do{
				tmp=kn;
				while(tmp){
					s.put(tmp%10);
					tmp /= 10;
				}
				ans=kn;
				kn+=n;
			}while(s.getSize() != 10);
			cout<<"Case #"<<i<<": "<<ans<<endl;
		}
	}
	return 0;
}