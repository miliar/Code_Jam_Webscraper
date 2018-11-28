#include<iostream>
#include<iomanip>
#include<sstream>
#include<string>
#include<map>

using namespace std;

void sort_string(string s, map<char, int>* app){

	for(int i=0; i<s.length(); ++i){
		char c=s[i];

//		int temp=(*app)[c];
		(*app)[c]++;
	}

}

void judge_special(map<char, int>* app, map <int, int>* number){

	if((*app)['Z']>0){
		int temp=(*app)['Z'];

		(*number)[0]=temp;

		for(int i=0; i<temp; ++i){
			int t1=(*app)['Z'];
			int t2=(*app)['E'];
			int t3=(*app)['R'];
			int t4=(*app)['O'];

			(*app)['Z']=t1-1;
			(*app)['E']=t2-1;
			(*app)['R']=t3-1;
			(*app)['O']=t4-1;
		}

	}


	if((*app)['W']>0){
		(*number)[2]=(*app)['W'];

		for(int i=0; i<(*number)[2]; ++i){
			(*app)['T']--;
			(*app)['W']--;
			(*app)['O']--;
		}

	}

	if((*app)['U']>0){

		(*number)[4]=(*app)['U'];

		for(int i=0; i<(*number)[4]; ++i){
			(*app)['F']--;
			(*app)['O']--;
			(*app)['U']--;
			(*app)['R']--;
		}

	}

	if((*app)['X']>0){
		(*number)[6]=(*app)['X'];

		for(int i=0; i<(*number)[6]; ++i){
			(*app)['S']--;
			(*app)['I']--;
			(*app)['X']--;
		}

	}

	if((*app)['G']>0){

		(*number)[8]=(*app)['G'];

		for(int i=0; i<(*number)[8]; ++i){
			(*app)['E']--;
			(*app)['I']--;
			(*app)['G']--;
			(*app)['H']--;
			(*app)['T']--;
		}

	}

	if((*app)['S']>0){

			(*number)[7]=(*app)['S'];

			for(int i=0; i<(*number)[7]; ++i){
				(*app)['S']--;
				(*app)['E']--;
				(*app)['V']--;
				(*app)['E']--;
				(*app)['N']--;
			}

		}


	if((*app)['V']>0){

			(*number)[5]=(*app)['V'];

			for(int i=0; i<(*number)[5]; ++i){
				(*app)['F']--;
				(*app)['I']--;
				(*app)['V']--;
				(*app)['E']--;
			}

		}

	if((*app)['T']>0){

			(*number)[3]=(*app)['T'];

			for(int i=0; i<(*number)[3]; ++i){
				(*app)['T']--;
				(*app)['H']--;
				(*app)['R']--;
				(*app)['E']--;
				(*app)['E']--;
			}

		}

	if((*app)['I']>0){

			(*number)[9]=(*app)['I'];

			for(int i=0; i<(*number)[9]; ++i){
				(*app)['N']--;
				(*app)['I']--;
				(*app)['N']--;
				(*app)['E']--;
			}

		}

	if((*app)['E']>0){

				(*number)[1]=(*app)['E'];

				for(int i=0; i<(*number)[1]; ++i){
					(*app)['O']--;
					(*app)['N']--;
					(*app)['E']--;
				}

			}

}


int main(){
	map <char, int> app;

	app['E']=0;
	app['F']=0;
	app['G']=0;
	app['H']=0;
	app['I']=0;
	app['N']=0;
	app['O']=0;
	app['R']=0;
	app['S']=0;
	app['T']=0;
	app['W']=0;
	app['V']=0;
	app['X']=0;
	app['Z']=0;

	map <int, int> number;

	number[0]=0;
	number[1]=0;
	number[2]=0;
	number[3]=0;
	number[4]=0;
	number[5]=0;
	number[6]=0;
	number[7]=0;
	number[8]=0;
	number[9]=0;

	int total;
	cin>>total;


	int case_num=1;

	for(int i=0; i<total; ++i){


	string s;
	cin>>s;
	sort_string(s, &app);
    judge_special(&app, &number);

    cout<<"Case #"<<case_num<<": ";

	for (map<int,int>::iterator it=number.begin(); it!=number.end(); ++it){
			 if(it->second>0){
				 for(int i=0; i<it->second; ++i){
				 cout << it->first ;
			 }
			 }
	}

	cout<<endl;
		app['E'] = 0;
		app['F'] = 0;
		app['G'] = 0;
		app['H'] = 0;
		app['I'] = 0;
		app['N'] = 0;
		app['O'] = 0;
		app['R'] = 0;
		app['S'] = 0;
		app['T'] = 0;
		app['W'] = 0;
		app['V'] = 0;
		app['X'] = 0;
		app['Z'] = 0;

		number[0] = 0;
		number[1] = 0;
		number[2] = 0;
		number[3] = 0;
		number[4] = 0;
		number[5] = 0;
		number[6] = 0;
		number[7] = 0;
		number[8] = 0;
		number[9] = 0;


	++case_num;
	}

}
