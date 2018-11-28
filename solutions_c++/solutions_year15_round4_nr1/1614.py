#include "stdc++.h"

using namespace std;

inline void ln(){putchar('\n');};
inline void space(){putchar(' ');};

inline void scan(int& a){ scanf("%d",&a); };
inline void scan (long int &a){scanf("%ld",&a);};
inline void scan (long long int &a){scanf("%lld",&a);};
inline void scan (string& s){ //stop at the end of the line
	int c;
	while((c=getchar())=='\n'||c==' '||c=='\r');
	do{
		switch(c){
		case'\n':case'\r':return;
		default:s+=c;
		}
	}while((c=getchar())!=EOF);
};
inline void scanspace (string& s){ //stop when encountering a space
	int c;
	while((c=getchar())=='\n'||c==' '||c=='\r');
	do{
		switch(c){
		case'\n':case'\r': case' ':return;
		default:s+=c;
		}
	}while((c=getchar())!=EOF);
};
inline void scan (char& c){ while((c=getchar())=='\n'||c==' '||c=='\r');};
inline void scan (double& a){scanf("%lf",&a);};
inline void scan (vector<int > &v, int n){
	int tmp;
	for(int i=0;i<n;i++){
		scan(tmp);
		v.push_back(tmp);
	}
};
inline void scan (vector<long int> &v, int n){
	long int tmp;
	for(int i=0;i<n;i++){
		scan(tmp);
		v.push_back(tmp);
	}
};
inline void scan (vector<long long int> &v, int n){
	long long int tmp;
	for(int i=0;i<n;i++){
		scan(tmp);
		v.push_back(tmp);
	}
};
inline void scan (vector<double> &v, int n){
	double tmp;
	for(int i=0;i<n;i++){
		scan(tmp);
		v.push_back(tmp);
	}
};
inline void scan (vector<char> &v, int n){
	char tmp;
	for(int i=0;i<n;i++){
		scan(tmp);
		v.push_back(tmp);
	}
};
inline void scan (vector<string> &v, int n){ //all words on the same line
	string tmp;
	for(int i=0;i<n;i++){
		scan(tmp);
		v.push_back(tmp);
		tmp.clear();
	}
};
inline void scanspace (vector<string> &v, int n){ //if several words on the same line
	string tmp;
	for(int i=0;i<n;i++){
		scanspace(tmp);
		v.push_back(tmp);
		tmp.clear();
	}
};
inline void scan(int a[],int b){
	for(int i=0;i<b;i++){
		scan(a[i]);
	}
};
inline void scan(long int a[],int b){
	for(int i=0;i<b;i++){
		scan(a[i]);
	}
};
inline void scan(long long int a[],int b){
	for(int i=0;i<b;i++){
		scan(a[i]);
	}
};
inline void scan(double a[],int b){
	for(int i=0;i<b;i++){
		scan(a[i]);
	}
};
inline void scan(char a[],int b){
	for(int i=0;i<b;i++){
		scan(a[i]);
	}
};
inline void scan(string a[],int b){
	for(int i=0;i<b;i++){
		scan(a[i]);
	}
};
inline void scanspace(string a[],int b){
	for(int i=0;i<b;i++){
		scanspace(a[i]);
	}
};
inline void scanasint(vector <int>& v){
	char c;
	while((c=getchar())=='\n'||c==' '||c=='\r');
	do{
		switch(c){
		case'\n':case'\r':case' ':return;
		default:v.push_back((int) c-'0');
		}
	}while((c=getchar())!=EOF);
};
inline void print(int a){ printf("%d",a); };
inline void print(long int a){ printf("%ld",a);}
inline void print(long long int a){printf("%lld",a);}
inline void print(double a,int nb=9){ printf("%.*lf",nb,a);};
inline void print(char c){cout<<c;};
inline void print(string s){cout<<s;};
inline void print(vector <int> v){
	vector<int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);
	}
};
inline void print(vector <long int> v){
	vector<long int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);
	}
};
inline void print(vector <long long int> v){
	vector<long long int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);
	}
};
inline void print(vector <double> v){
	vector<double>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);
	}
};
inline void print(vector <char> v){
	vector<char>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);
	}
};
inline void print(vector <string> v){
	vector<string>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);
	}
};
inline void printspace(vector <int> v){
	vector<int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);space();
	}
};
inline void printspace(vector <long int> v){
	vector<long int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);space();
	}
};
inline void printspace(vector <long long int> v){
	vector<long long int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);space();
	}
};
inline void printspace(vector <double> v){
	vector<double>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);space();
	}
};
inline void printspace(vector <char> v){
	vector<char>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);space();
	}
};
inline void printspace(vector <string> v){
	vector<string>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);space();
	}
};
inline void println(vector <int> v){
	vector<int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);ln();
	}
};
inline void println(vector <long int> v){
	vector<long int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);ln();
	}
};
inline void println(vector <long long int> v){
	vector<long long int>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);ln();
	}
};
inline void println(vector <double> v){
	vector<double>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);ln();
	}
};
inline void println(vector <char> v){
	vector<char>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);ln();
	}
};
inline void println(vector <string> v){
	vector<string>::iterator it;
	for(it=v.begin();it!=v.end();it++){
		print(*it);ln();
	}
};
inline void print(int a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);
	}
};
inline void print(long int a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);
	}
};
inline void print(long long int a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);
	}
};
inline void print(double a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);
	}
};
inline void print(char a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);
	}
};
inline void print(string a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);
	}
};
inline void printspace(int a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);space();
	}

}
inline void printspace(long int a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);space();
	}
};
inline void printspace(long long int a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);space();
	}
};
inline void printspace(double a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);space();
	}
};
inline void printspace(char a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);space();
	}
};
inline void printspace(string a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);space();
	}
};
inline void println(long int a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);ln();
	}
};
inline void println(long long int a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);ln();
	}
};
inline void println(double a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);ln();
	}
};
inline void println(char a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);ln();
	}
};
inline void println(string a[],int b){
	for (int i=0;i<b;i++){
		print(a[i]);ln();
	}
};




bool dir(vector <string> grid,int x,int y,int R,int C,int direction){
	bool retour=false;
	if(direction==0)
	{
		for(int i=x+1;i<R;i++)
		{
			//cout<<"grid"<<grid[i][y]<<endl;
			if(grid[i][y]!='.')
			{
				//cout<<"direction"<<direction<<"ok"<<endl;
				retour=true;
				break;
			}
		}
	}
	if(direction==1)
	{
		for(int i=x-1;i>=0;i--)
		{
			if(grid[i][y]!= '.')
			{
				//cout<<"direction"<<direction<<"ok"<<endl;
				retour=true;
				break;
			}
		}
	}
	if(direction==2)
	{
		for(int i=y+1;i<C;i++)
		{
			if(grid[x][i]!='.')
			{
				retour=true;
				break;
			}
		}
	}
	if(direction==3)
	{
		for(int i=y-1;i>=0;i--)
		{
			if(grid[x][i]!='.')
			{
				retour=true;
				break;
			}
		}
	}
	return(retour);
}



int solve(){
	int a=0;
	int tmp;
	int cpt;
	int R,C;
	scan(R);
	scan(C);
	vector <string> grid;

	scan(grid,R);
	/*
	for(int i=0;i<R;i++)
	{
		//for(int j=0;j<C;j++)
		{
			print(grid[i]);
		}
	}
	 */

	for(int i=0;i<R;i++)
	{
		for(int j=0;j<C;j++)
		{
			//cout<<"ij"<<i<<j<<endl;
			//cout<<a<<"a"<<endl;
			if(grid[i][j]=='<')
			{
				if(!dir(grid,i,j,R,C,3))
				{
					a++;
					if(!dir(grid,i,j,R,C,2) and !dir(grid,i,j,R,C,1) and !dir(grid,i,j,R,C,0))
					{
						print("IMPOSSIBLE");
						return(0);
					}
				}

			}
			if(grid[i][j]=='>')
			{
				if(!dir(grid,i,j,R,C,2))
				{
					a++;
					if(!dir(grid,i,j,R,C,0) and !dir(grid,i,j,R,C,1) and !dir(grid,i,j,R,C,3))
					{
						print("IMPOSSIBLE");
						return(0);
					}
				}

			}
			if(grid[i][j]=='v')
			{
				if(!dir(grid,i,j,R,C,0))
				{
					a++;
					if(!dir(grid,i,j,R,C,1) and !dir(grid,i,j,R,C,2) and !dir(grid,i,j,R,C,3))
					{
						print("IMPOSSIBLE");
						return(0);
					}
				}

			}
			if(grid[i][j]=='^')
			{
				if(!dir(grid,i,j,R,C,1))
				{
					a++;
					if(!dir(grid,i,j,R,C,0) and !dir(grid,i,j,R,C,2) and !dir(grid,i,j,R,C,3))
					{
						print("IMPOSSIBLE");
						return(0);
					}
				}

			}
		}
	}

	print(a);
	return(0);

};


int init(){
	freopen("A-large.in.txt","r",stdin);
	freopen("output_big.txt","w",stdout);
	return 0;
}
int main(){
	init();
	int t;
	scan(t);
	for(int i=0;i<t;i++){
		printf("Case #%d: ",i+1);
		solve();
		ln();
	}
}
