#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;


void recSort(vector<long double> & toSort, vector<long double> & parallel, int a, int b){
	if(b<a+2)
		return;
	int middle=(a+b)/2;
	recSort(toSort, parallel, a, middle);
	recSort(toSort, parallel, middle, b);
	//merge
	vector<long double> merged, pmerged;
	int pos1=a, pos2=middle;
	for(int i=a; i<b; i++){
		if(pos1==middle){
			merged.push_back(toSort[pos2]);
			pmerged.push_back(parallel[pos2]);
			pos2++;
		}else{
			if(pos2==b){
				merged.push_back(toSort[pos1]);
				pmerged.push_back(parallel[pos1]);
				pos1++;
			}else{
				if(toSort[pos1]<toSort[pos2]){
					merged.push_back(toSort[pos1]);
					pmerged.push_back(parallel[pos1]);
					pos1++;
				}else{
					merged.push_back(toSort[pos2]);
					pmerged.push_back(parallel[pos2]);
					pos2++;
				}
			}
		}
	}
	for(int i=a; i<b; i++){
		toSort[i]=merged[i-a];
		parallel[i]=pmerged[i-a];
	}
}

void sort(vector<long double> & toSort, vector<long double> & parallel){
	recSort(toSort, parallel, 0, toSort.size());
}

void assert(bool b){
	if(!b)
		cout<<"ERROR assert"<<endl;
}

int main(){
	cout<<"launching function main"<<endl;
	ifstream file("B-small-attempt1.in");
	ofstream outputfile("myoutput.txt");
	int T, N, highpos, lowpos;
	long double V, X, r, c, rate, eps=0.00001, highrate, lowrate, hightemp, lowtemp, highratio, lowratio;
	bool possible;
	vector<long double> R, C;
	file>>T;
	for(int t=0;t<T;t++){
		//read input
		R.clear();
		C.clear();
		file>>N>>V>>X;
		for(int i=0;i<N;i++){
			file>>r>>c;
			R.push_back(r);
			C.push_back(c);
		}
		//solve & write
		sort(C,R);
		rate=0;
//		possible=((C[0]<=X+eps) && (C[N-1]+eps>=X));
		possible=((C[0]<=X) && (C[N-1]>=X));
		if(!possible)
			outputfile<<"Case #"<<(t+1)<<": "<<"IMPOSSIBLE"<<endl;
		else{
			highpos=N-1; lowpos=0;
			highrate=R[highpos]; lowrate=R[lowpos];
			hightemp=C[highpos]; lowtemp=C[lowpos];
			while(hightemp>X && lowtemp<X){
				assert(highrate>=0 && lowrate>=0);
				lowratio=(hightemp-X)/(hightemp-lowtemp);
				highratio=1.0-lowratio;
				if(lowrate*highratio>highrate*lowratio){
					if(highratio>0){
						rate=rate+highrate/highratio;
						lowrate=lowrate-highrate*lowratio/highratio;
					}
					highpos--;
					highrate=R[highpos];
					hightemp=C[highpos];
				}else{
					if(lowratio>0){
						rate=rate+lowrate/lowratio;
						highrate=highrate-lowrate*highratio/lowratio;
					}
					lowpos++;
					lowrate=R[lowpos];
					lowtemp=C[lowpos];
				}
			}
			if(highpos==lowpos){
				if(hightemp==X || lowtemp==X){
					rate=rate+min(lowrate, highrate);
				}
			}else{
				if(hightemp==X){
					rate=rate+highrate;
				}
				if(lowtemp==X){
					rate=rate+lowrate;
				}
			}
//			outputfile<<"Case #"<<(t+1)<<": "<<(V/rate)<<endl;
			outputfile<<"Case #"<<(t+1)<<setprecision(12)<<": "<<(V/rate)<<endl;
		}
	}
	file.close();
	outputfile.close();
}

