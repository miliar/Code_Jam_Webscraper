#include<iostream>
#include<fstream>
#include<string>
using namespace std;
string nbnum[100000];
int p[100];
int alldigit = 0;
int nbcount = 3;
void square(int *a,int digit){
	int carry = 0;
	memset(p,0,sizeof(p));
	for(int i = 0; i < digit; i++){
		carry = 0;
		for(int j = 0; j < digit; j++){
			p[i+j] += carry+(a[i]*a[j]%10);
			carry = (a[i]*a[j])/10+p[i+j]/10;
			p[i+j] %= 10;
		}
		p[i+digit] = carry;
		carry = 0;
	}
	for(int i = digit*digit-1; i >=0;i--)
		if(p[i] != 0){alldigit = i;break;}
}
void generate(){
	nbnum[0] = "1";nbnum[1] = "4";nbnum[2] = "9";
	int a[100];
	//2
	for(int i = 1; i < 10; i++){
		a[0] = a[1] = i;
		square(a,2);
		bool flag = true;
		for(int i = 0; i <= alldigit; i++){
			if(p[i]!=p[alldigit-i]){flag=false; break;}
		}
		if(flag){
//			for(int nn = 1; nn >= 0; nn--)cout << a[nn];
//			cout << endl;
			string s  = "";
			for(int i = alldigit; i >= 0; i--)s+=p[i]+'0';
			nbnum[nbcount++] = s;
		}
	}
	//3
	for(int i = 1; i < 10; i++){
		a[0] = a[2] = i;
		for(int j = 0; j < 10; j++){
			a[1] = j;
			square(a,3);
			bool flag = true;
			for(int i = 0; i <= alldigit; i++){
				if(p[i]!=p[alldigit-i]){flag=false; break;}
			}
			if(flag){
//				for(int nn = 2; nn >= 0; nn--)cout << a[nn];
//				cout << endl;
				string s  = "";
				for(int i = alldigit; i >= 0; i--)s+=p[i]+'0';
				nbnum[nbcount++] = s;
			}
		}
	}
	//4
	for(int i = 1; i < 10; i++){
		a[0] = a[3] = i;
		for(int j = 0; j < 10; j++){
			a[1] = a[2] = j;
			square(a,4);
			bool flag = true;
			for(int i = 0; i <= alldigit; i++){
				if(p[i]!=p[alldigit-i]){flag=false; break;}
			}
			if(flag){
//				for(int nn = 3; nn >= 0; nn--)cout << a[nn];
//				cout << endl;
				string s  = "";
				for(int i = alldigit; i >= 0; i--)s+=p[i]+'0';
				nbnum[nbcount++] = s;
			}
		}
	}
	//5
	for(int i = 1; i < 10; i++){
		a[0] = a[4] = i;
		for(int j = 0; j < 10; j++){
			a[1] = a[3] = j;
			for(int k = 0; k < 10; k++){
				a[2] = k;
				square(a,5);
				bool flag = true;
				for(int i = 0; i <= alldigit; i++){
					if(p[i]!=p[alldigit-i]){flag=false; break;}
				}
				if(flag){
//					for(int nn = 4; nn >= 0; nn--)cout << a[nn];
//					cout << endl;
					string s  = "";
					for(int i = alldigit; i >= 0; i--)s+=p[i]+'0';
					nbnum[nbcount++] = s;
				}
			}
		}
	}
	//6
	for(int i = 1; i < 10; i++){
		a[0] = a[5] = i;
		for(int j = 0; j < 10; j++){
			a[1] = a[4] = j;
			for(int k = 0; k < 10; k++){
				a[2] = a[3] = k;
				square(a,6);
				bool flag = true;
				for(int i = 0; i <= alldigit; i++){
					if(p[i]!=p[alldigit-i]){flag=false; break;}
				}
				if(flag){
//					for(int nn = 5; nn >= 0; nn--)cout << a[nn];
//					cout << endl;
					string s  = "";
					for(int i = alldigit; i >= 0; i--)s+=p[i]+'0';
					nbnum[nbcount++] = s;
				}
			}
		}
	}
	//7
	for(int i = 1; i < 10; i++){
		a[0] = a[6] = i;
		for(int j = 0; j < 10; j++){
			a[1] = a[5] = j;
			for(int k = 0; k < 10; k++){
				a[2] = a[4] = k;
				for(int l = 0 ; l < 10; l++){
					a[3] = l;
					square(a,7);
					bool flag = true;
					for(int i = 0; i <= alldigit; i++){
						if(p[i]!=p[alldigit-i]){flag=false; break;}
					}
					if(flag){
//						for(int nn = 6; nn >= 0; nn--)cout << a[nn];
//						cout << endl;
						string s  = "";
						for(int i = alldigit; i >= 0; i--)s+=p[i]+'0';
						nbnum[nbcount++] = s;
					}
				}
			}
		}
	}
	//8
	for(int i = 1; i < 10; i++){
		a[0] = a[7] = i;
		for(int j = 0; j < 10; j++){
			a[1] = a[6] = j;
			for(int k = 0; k < 10; k++){
				a[2] = a[5] = k;
				for(int l = 0 ; l < 10; l++){
					a[3] = a[4] = l;
					square(a,8);
					bool flag = true;
					for(int i = 0; i <= alldigit; i++){
						if(p[i]!=p[alldigit-i]){flag=false; break;}
					}
					if(flag){
//						for(int nn = 6; nn >= 0; nn--)cout << a[nn];
//						cout << endl;
						string s  = "";
						for(int i = alldigit; i >= 0; i--)s+=p[i]+'0';
						nbnum[nbcount++] = s;
					}
				}
			}
		}
	}
}
void main(){
	int T,A,B;
//	ifstream cin("C-small-attempt0.in");
//	ofstream cout("2013gcj_qr_C.out");
	generate();
	for(int i = 0; i < nbcount;i++)cout << nbnum[i]<<endl;
	cout << nbcount<<endl;
	cin >> T;
	for(int i = 0; i < T; i++){
		cin >> A >> B;
//		cout << "Case #"<<i+1<<": "<<count<<endl;
	}
	system("pause");
}