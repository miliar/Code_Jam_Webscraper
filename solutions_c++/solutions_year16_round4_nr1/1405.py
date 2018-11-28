#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

static int roundp[13], roundr[13], rounds[13], nrounds;
static int answ[8192], answ2[8192], lans;
static int perm1[18], perm2[18];
static int winner[9]={-1,0,2,0,-1,1,2,1,-1}, loser[9]={-1,1,0,1,-1,2,0,2,-1};
static char const char_of_int[3]={'P','R','S'};

void solve(){
	int modround=((nrounds-1)%6), order[3]={0,1,2}, orderthen[3], posthen;
	lans=1;
	//perm1, perm2
	for(int i=0; i<6; i++){
		posthen=0;
		for(int fight1=0; fight1<2; fight1++)
			for(int fight2=fight1+1; fight2<3; fight2++){
				orderthen[posthen]=winner[3*order[fight1]+order[fight2]];
				perm1[3*i+orderthen[posthen]]=order[fight1]; perm2[3*i+orderthen[posthen]]=order[fight2];
				posthen++;
			}
		for(int j=0; j<3; j++)
			order[j]=orderthen[j];
	}
	//solve answer
	if(roundp[nrounds]>0)
		answ[0]=0;
	else{
		if(roundr[nrounds]>0)
			answ[0]=1;
		else
			answ[0]=2;
	}
	if(roundp[nrounds]+roundr[nrounds]+rounds[nrounds] !=1){
		cout<<"ERROR "<<endl;
	}
	for(int k=0; k<nrounds; k++){
		for(int i=0; i<lans; i++){
			answ2[i]=answ[i];
		}
		for(int i=0; i<lans; i++){
			answ[2*i]=perm1[3*modround+answ2[i]];
			answ[2*i+1]=perm2[3*modround+answ2[i]];
		}
		lans*=2;
		modround=(modround+5)%6;
	}
}

int main(){
	cout<<"launching function main"<<endl;
//	ifstream file("A-small-attempt0.in");
	ifstream file("A-large.in");
	ofstream outputfile("myoutput.txt");
	//start
	int T, N, R, P, S, n, r, p, s, np, nr, ns;
	bool possible;
	file>>T;
	for(int t=0;t<T;t++){
		//read input
		file>>N>>R>>P>>S;
		//solve
		nrounds=N;
		roundp[0]=P; roundr[0]=R; rounds[0]=S;
		possible=true;
		for(int i=0; i<N; i++){
			roundp[i+1]=(roundp[i]+roundr[i]-rounds[i])/2;
			roundr[i+1]=(roundr[i]+rounds[i]-roundp[i])/2;
			rounds[i+1]=(rounds[i]+roundp[i]-roundr[i])/2;
			if((roundp[i+1]<0) || (roundr[i+1]<0) || (rounds[i+1]<0))
				possible=false;
		}
		if(possible)
			solve();
		//write output
		outputfile<<"Case #"<<(t+1)<<": ";
		if(possible){
			for(int i=0; i<lans; i++)
				outputfile<<char_of_int[answ[i]];
		}else{
			outputfile<<"IMPOSSIBLE";
		}
		outputfile<<endl;
	}
	file.close();
	outputfile.close();
}

