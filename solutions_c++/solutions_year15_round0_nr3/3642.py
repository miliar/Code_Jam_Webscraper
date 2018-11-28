#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <cmath>
#include <algorithm>


using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
typedef stack<long long> ss;
#define get(a) #a
//#define DEBUG
#ifdef DEBUG

     #define debug(args...)            {dbg,args; cerr<<endl;}

#else

    #define debug(args...)              // Just strip off all debug tokens

#endif


struct debugger

{

    template<typename T> debugger& operator , (const T& v)

    {    

        cerr<<v<<" ";    

        return *this;    

    }

} dbg;

int main(){
	int t;
	cin>>t;

	char arr[5][5] = {0,0,0,0,0,
		0,1,2,3,4,
		0,2,-1,4,-3,
		0,3,-4,-1,2,
		0,4,3,-2,-1};

	int case1 = 1;
	while(t--){
		int l,x;
		cin>>l>>x;
		cin.ignore();

		int input[l];

		string t;
		cin>>t;

		for(int i = 0;i < l;i++){
			if(t[i] == '1'){
				input[i] = 1;
			}
			else if(t[i] == 'i'){
				input[i] = 2;
			}
			else if(t[i] == 'j'){
				input[i] = 3;
			}
			else{
				input[i] = 4;
			}
			//cout<<input[i]<<" ";
		}
		//cout<<endl;

		int lx[l*x];

		for(int i = 0;i < x;i++){
			for(int j = 0;j < l;j++){
				lx[l*i + j] = input[j];
				//cout<<"lx["<<(l*(i+1))<<"] = "<<lx[l*(i+1)]<<endl;
			}
		}

		//cout<<"Hello\n";
		int front[l*x];

		front[0] = input[0];
		for(int i = 1;i < (l*x);i++){
			if(front[i-1] < 0){
				if(lx[i] < 0)
					front[i] = arr[abs(front[i-1])][abs(lx[i])];
					//cout<<"dummy\n";
				else
					//cout<<"dummy\n";
					front[i] = -1*arr[abs(front[i-1])][abs(lx[i])];
			}
			else{
				if(lx[i] < 0)
					//cout<<"dummy\n";
					front[i] = -1*arr[abs(front[i-1])][abs(lx[i])];
				else
					//cout<<front[i-1]<<" " <<lx[i]<<" dummy\n";
					front[i] = arr[abs(front[i-1])][abs(lx[i])];
			}
			
			//cout<<"front["<<i<<"] = "<<front[i]<<endl;
		}
		
		int flag = 1;
		if(front[l*x - 1] != -1){
			flag = 0;
		}		
		if(flag == 1){
			for(int i = 0;i < (l*x);i++){
				for(int j = i+1;j < (l*x);j++){
					if(front[i] == 2){
						if(front[j] == 4){
							flag = 0;
							break;
						}
					}
				}
				if(flag == 0){
					break;
				}
			}
			if(flag == 0){
				cout<<"Case #"<<case1<<": YES"<<endl;
			}
			else{
				cout<<"Case #"<<case1<<": NO"<<endl;
			}
		}
		else{
			cout<<"Case #"<<case1<<": NO"<<endl;
		}
		case1++;
	}
}