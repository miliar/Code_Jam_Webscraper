//Ominous Omino
#include<iostream>
using namespace std;
int main(){
	int T;
	cin>>T;
	for (int i=0;i<T;i++){
		int x,r,c;
		string winn;
		cin>>x>>r>>c;
		if ((r*c)%x!=0){
			winn="RICHARD";
		} else if ((x>2)&&((r==1)||(c==1))){ winn="RICHARD";
		} else if ((x>r)&&(x>c)) {	winn="RICHARD";
		} else if ((x==4)&&(r*c==8)) { winn="RICHARD";
		} else {
			int winr=0;
			for (int j=1;j<=x;j++){
				if (x%j==0){
					if ((x%j>r)||(x%j>c)){
						winr++;
						break;
					}
				}
			}
			if (winr>=1) winn="RICHARD"; else winn="GABRIEL";
		}
		cout<<"Case #"<<i+1<<": "<<winn<<endl;
	}
}
