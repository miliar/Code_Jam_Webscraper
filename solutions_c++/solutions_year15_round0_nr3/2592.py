#include <iostream>
using namespace std;
int l;
int seq[10010];
const int I=1;
const int J=2;
const int K=3;
const int MI=-1;
const int MJ=-2;
const int MK=-3;
const int One=20;
const int MOne=-20;


inline int get(int i){
	return seq[i%l];
}
inline int mul(int x, int y){
	int m=1;
	if(x<0){
		x=-x;
		m=-1;
	}
	if(y<0){
		y=-y;
		m*=-1;
	}
	if(x==One)return m*y;
	else if(x==I){
		if(y==One)return m*I;
		else if(y==I)return m*MOne;
		else if(y==J)return m*K;
		else return m*MJ;
	}
	else if(x==J){
		if(y==One)return m*J;
		else if(y==I)return m*MK;
		else if(y==J)return m*MOne;
		else return m*I;
	}
	else{
		if(y==One)return m*K;
		else if(y==I)return m*J;
		else if(y==J)return m*MI;
		else return m*MOne;
	}
	
}
int main(){
	freopen("out3.txt","w",stdout);
	freopen("in3.txt","r",stdin);
	int _c;
	cin>>_c;
	for(int c=1;c<=_c;c++){
		int x;
		cin>>l>>x;
		int len=l*x;
		
		for(int i=0;i<l;i++){
			char ch;
			do{
				cin>>ch;
			}while(ch==' '||ch=='\t'||ch=='\n'||ch=='\r');
			if(ch=='i')seq[i]=I;
			else if(ch=='j')seq[i]=J;
			else seq[i]=K;
		}

		//first I
		int tm=One;
		int Ip=-1;
		for(int i=0;i<len;i++){
			tm=mul(tm,get(i));
			if(tm==I){
				Ip=i;
				break;
			}
		}
		if(Ip!=-1){
			//then K
			int tm2=One;
			int Kp=-1;
			for(int i=len-1;i>=0;i--){
				tm2=mul(get(i),tm2);
				if(tm2==K){
					Kp=i;
					break;
				}
			}
			if(Kp!=-1){
				//then J
				int tm3=One;
				for(int i=Ip+1;i<Kp;i++)
					tm3=mul(tm3,get(i));
				if(tm3==J){
					//success
					cout<<"Case #"<<c<<": YES"<<endl;
					continue;
				}
			}
		}
		cout<<"Case #"<<c<<": NO"<<endl;	
	}
}
