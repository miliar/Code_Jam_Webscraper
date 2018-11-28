/*#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
	int T,CASES=1;
	

	ofstream output;
	output.open("output.out");
	ifstream input;
	input.open("A-small-attempt5.in");

	input>>T;
	while(CASES<=T){
		int first,second;
		int cnt[17]={};
		int cards[5][5]={};
		input>>first;
		int i,j;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++){
				input>>cards[i][j];
			}
		for(j=1;j<=4;j++)
			cnt[cards[first][j]]++;
		input>>second;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				input>>cards[i][j];
		for(j=1;j<=4;j++)
			cnt[cards[second][j]]++;
		int guess2=0,guess;
		for(i=1;i<=16;i++){
			if(cnt[i]==2){
				guess2++;
				guess=i;
			}
		}
		if(guess2==0)
			output<<"Case #"<<CASES<<": Volunteer cheated!\n";
		else if(guess2==1)
			output<<"Case #"<<CASES<<": "<<guess<<endl;
		else
			output<<"Case #"<<CASES<<": Bad magician!\n";
		CASES++;
	}
	output.close();
	input.close();
	return 0;
}

#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
	int T,CASES=1;
	ifstream input;
	input.open("B-small-attempt0.in");
	ofstream output;
	output.open("B-output.out");
	input>>T;
//	cin>>T;
//	cout<<T<<endl;
	while(CASES<=T){
		double C,F,X,cur_cookies=0;
		input>>C>>F>>X;
		//cin>>C>>F>>X;
		double cur_spent_time=0, cur_rate=2;
		while( 1 ){
			if( cur_cookies - C >=0 &&
				(X - (cur_cookies - C))/(cur_rate+F) - (X - cur_cookies)/cur_rate <= 0)
			{
				cur_cookies -= C;
				cur_rate += F;
			}
			else if ( cur_cookies - C >=0 &&
				(X - (cur_cookies - C))/(cur_rate+F) - (X - cur_cookies)/cur_rate > 0)
			{
				cur_spent_time += (X-cur_cookies)/cur_rate;
				break;
			}
			else{
				cur_cookies += C;
				cur_spent_time += C/cur_rate;
			}
		}
		//cout<<cur_spent_time<<endl;
		output<<"Case #"<<CASES<<": "<< std::setprecision(10)<<cur_spent_time<<endl;
		CASES++;
	}
	return 0;
}*/

#include<iostream>
#include<fstream>
#include<stdlib.h>
using namespace std;
int cmp(const void *a,const void *b)
{
	double *aa = (double *)a;
	double *bb = (double *)b;
	if(*aa - *bb < 0)return -1;
	else return 1;
}

int main()
{
	int T,CASES=1,N;
	ifstream input;
	ofstream output;
	input.open("D-large.in");
	output.open("D-output.out");
	input>>T;
	while(CASES<=T){
		input>>N;
		int i,j;
		int realscore=0,fakescore=0;
		double naomi[1001],ken[1001];//small dataset
		bool ken_choose_fake[1001]={},ken_choose_real[1001]={};
		for(i=0;i<N;i++)
			input>>naomi[i];
		for(i=0;i<N;i++)
			input>>ken[i];
		qsort(naomi,N,sizeof(naomi[0]),cmp);
		qsort(ken,N,sizeof(naomi[0]),cmp);
		for(i=0;i<N;i++){
			bool findless=false;
			for(j=0;j<N;j++){
				if(ken_choose_real[j]==false && naomi[i]<ken[j]){
					ken_choose_real[j]=true;
					break;
				}
			}
			for(j=0;j<N;j++)
			{//找到比naomi小的，报1，则ken会选最小的
				if(ken_choose_fake[j]==false && ken[j]<naomi[i]){
					fakescore++;
					ken_choose_fake[j]=true;
					findless=true;
					break;
				}
			}
			if(!findless){//没有找到比naomi小的，报ken最大值-0.000001
				for(j=N-1;j>=0;j--){
					if(ken_choose_fake[j]==false){
						ken_choose_fake[j]=true;
						break;
					}
				}
			}
		}
		for(i=0;i<N;i++)
			if(ken_choose_real[i]==false)
				realscore++;

		output<<"Case #"<<CASES<<": "<<fakescore<<" "<<realscore<<endl;
		CASES++;
	}

}