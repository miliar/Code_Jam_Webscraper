#include <fstream>
#include <cmath>
using namespace std;

long long power(int s){
	long long ans = 1;
	for(int i=0 ; i<s ; i++){
		ans*=10;
	}
	return ans;
}

long long db[1000];

int init(){
		//odd
	int counter=0;
		for(int i=0 ; i<=9999 ; i++){
			for(int m=0 ; m<9 ; m++){
			bool pal = true;
			int digit = (int)log10((double) i) +1;
			long long test = i*power(digit+1);
			for(int j=1 ; j<=digit; j++){
				test+= ((i/power(j-1))%10)*power((digit)-j);
			}
			test+=m*power(digit);
			if(test==0){continue;}
			test*= test;
			int digit2 = log10((long double)test)+1;
			for(int j=1 ;  2*j<=digit2 ; j++){
				if(!((test/power(digit2-j))%10 == (test/power(j-1))%10)){
					pal=false;
					break;
				}
			}
			if(pal){db[counter] = test ; counter++;}
			}
		}

		//even
		for(int i=0 ; i<=9999 ; i++){
			bool pal = true;
			int digit = (int)log10((double) i) +1;
			long long test = i*power(digit);
			for(int j=1 ; j<=digit; j++){
				test+= ((i/power(j-1))%10)*power((digit)-j);
			}
			if(test==0){ continue;}
			test*= test;
			int digit2 = log10((long double)test)+1;
			
			for(long long j=1 ;  2*j<=digit2 ; j++){			
				if(!((test/power(digit2-j))%10 == (test/power(j-1))%10)){
					pal=false;
					break;
				}
			}
					if(pal){db[counter] = test ; counter++;}
		}
		return counter;
}

int main(){
	ifstream cin;
	ofstream cout;

	cin.open("C-large-1.in");
	cout.open("QR3_Loutput.txt");

	int index = init();	
	int N;
	cin>> N;
	for(int n=0 ; n<N ; n++){
		long long head, tail;

		int count =0;
		cin >> head >> tail;
		
		for(int i=0 ; i<index ; i++){
			if(db[i]<=tail && db[i]>=head){
				count++;
			}
		}
		cout << "Case #" << n+1 << ": " << count << endl;
		}

	}


