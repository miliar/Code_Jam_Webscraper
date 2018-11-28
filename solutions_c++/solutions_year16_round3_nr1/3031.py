#include <iostream>
using namespace std;
int main(){
	float x,tt,t,a,b,c;
	cin>>t;
	tt=1;
	while(t--){
		cout<<"Case #"<<tt++<<":";
		a=b=c=0;
		cin>>x>>a>>b;
		if(x==3)cin>>c;
		while(a>0||b>0||c>0){
			if(c<1){
				if(a-b>=2){cout<<" AA";a-=2;}
				if(b-a>=2){cout<<" BB";b-=2;}
				if(a-b==1 && a>2){cout<<" AA";a-=2;}
				if(b-a==1 && b>2){cout<<" BB";b-=2;}
				if(b==1 && a==2){cout<<" A AB";a=b=0;}
				if(a==1 && b==2){cout<<" B AB";a=b=0;}
				if(a==b&&a>0){cout<<" AB";a--;b--;}
			}
			else{
				if(a==c&&b==0){cout<<" AC";a-=1;c-=1;continue;}
				if(b==c&&a==0){cout<<" BC";b-=1;c-=1;continue;}
				if(a==b){
					if(c>1){cout<<" CC";c-=2;continue;}
					if(c==1){cout<<" C";c=0;continue;}
				}
				if(c-a>=2&&c-b>=2){cout<<" CC";c-=2;continue;}
				if(a>b&&c>b){cout<<" AC";a-=1;c-=1;}
				if(b>a&&c>a){cout<<" BC";b-=1;c-=1;}
				if(a>b&&a>c){cout<<" AA";a-=2;}
				if(b>a&&b>c){cout<<" BB";b-=2;}
				if(c==1&&a==1&&b==1){cout<<" C AB";c=a=b=0;}
				//cout<<" C";c--;
			}
		}
		cout<<endl;
	}
	return 0;
}
/*

11
12
13
21
22

  1 2 3 4 5 6 7 8 9
1 x x x
2 x x x x x
3 x x x
4
5
6
7
8
9

1:2 = 66%
2:3 = 60%
3:4 = 57%
4:5 = 55%


*/
