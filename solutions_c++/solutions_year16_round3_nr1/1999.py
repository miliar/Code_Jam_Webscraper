#include<iostream>
#include<algorithm>
#include<sstream>
using namespace std;
#define ALL(x) (x).begin(), (x).end()
#define EACH(itr,c) for(__typeof((c).begin()) itr=(c).begin(); itr!=(c).end(); itr++)  
#define FOR(i,b,e) for (int i=(int)(b); i<(int)(e); i++)
#define MP(x,y) make_pair(x,y)
#define REP(i,n) for(int i=0; i<(int)(n); i++)


int main(){
//	freopen("A-1.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	REP(rnd,T){
		cout<<"Case #"<<rnd+1<<":";
		int N,sum=0;
		int a[26];
		cin>>N;
		REP(i,N){
			cin>>a[i];
			sum+=a[i];
		}
		while(sum!=0){
			int max1=0,max2=0,index1=-1,index2=-2;
			REP(i,N){
				index1=(max1<=a[i])?i:index1;
				max1=(max1<=a[i])?a[i]:max1;
			}			
			REP(i,N){
				if(i==index1)continue;
				index2=(max2<=a[i])?i:index2;
				max2=(max2<=a[i])?a[i]:max2;
			}
			if((sum-2)==1){
				sum-=1;
				cout<<" "<<char('A'+index1);
				a[index1]-=1;
			}else{
				sum-=2;
				cout<<" "<<char('A'+index1)<<char(index2+'A');
				a[index1]-=1;
				a[index2]-=1;
			}
		}
		cout<<endl;
		
			
			
	}
	return 0;
}


