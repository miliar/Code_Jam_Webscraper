#include<iostream>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;

/*problems
*/

/*plans
*/

//classes
typedef pair<int,int> P;
typedef long long LL;

//constants
int INF=INT_MAX/2;

//variables
ifstream fin;
ofstream foot,fout;
int T,A,B;

//data structures
vector<int> fine;

//functions
bool chk(LL x)
{
	vector<int> temp;
	LL m=x;

	while(m>0){
		temp.push_back(m%10);
		m/=10;
	}

	LL sum=0,b=1;
	for(int i=int(temp.size())-1; i>=0; i--){
		sum+=temp[i]*b;
		b*=10;
	}

	if(sum==x)return 1;
	else return 0;
}

void init(int n)
{
	for(int i=1; i<=n; i++){
		if(chk(i)){
			if(chk(i*i))fine.push_back(i*i);
		}
	}
}

void solve()
{
	LL a=upper_bound(fine.begin(),fine.end(),A-1)-fine.begin();
	LL b=upper_bound(fine.begin(),fine.end(),B)-fine.begin();

	fout<<b-a<<endl;
}

int main()
{
	fin.open("C:\\Users\\fumi\\Downloads\\C-small-attempt0.in");
	fout.open("C:\\Users\\fumi\\Downloads\\C-small-answer.txt");
	foot.open("C:\\Users\\fumi\\Downloads\\C-small-sample.txt");

	fin>>T;
	init(50);

	for(int i=0; i<T; i++){
		fin>>A>>B;
		fout<<"Case #"<<i+1<<":"<<" ";
		solve();
	}

	fin.close();
	fout.close();
	foot.close();

	system("pause");
	return 0;
}