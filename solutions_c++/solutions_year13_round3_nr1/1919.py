#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <map>

using namespace std;

map<pair<int,int>,int>b;

int calc(string str,int i,int j){
   int count=0;
   int max=0;

   for(int n=i;n<=j;n++){
	   if(str.substr(n,1)!="a" && str.substr(n,1)!="i" && str.substr(n,1)!="u" && str.substr(n,1)!="e" && str.substr(n,1)!="o"){count++;/*cout<<str.substr(n,1) << count<<endl;*/}
	   else{count=0;}
	   if(count>=max){max=count;/*cout <<"max=" <<max<<endl;*/}
   }
   return max;
}

int main()
{
	//ifstream ifs("A-small-attempt0 (3).in");
    ifstream ifs("A-small-attempt1 (2).in");
    ofstream ofs("answer");
	int T;
	ifs >> T; cout << "T= " << T <<endl;
   
   for(int t=0;t<T;t++){  // test cases

	   b.clear();
	string str;
    ifs >> str; cout << str <<endl;

	int n;
	ifs >> n; cout << n <<endl;

	int N=str.size();

	long ans=0;

	for(int s=0;s<=N-1;s++){
		for(int i=0;i+s<=N-1;i++){
               int j=i+s;
			   if(s!=0 && (b[pair<int,int>(i+1,j)]>=n || b[pair<int,int>(i,j-1)]>=n)){b[pair<int,int>(i,j)]=n;ans++;}
			   else{ int num=calc(str,i,j);
			         b[pair<int,int>(i,j)]=num;
					 if(num>=n){ans++;}
			         }
		}

	}

	//cout << str << " " << calc(str,0,str.size()-1)<<endl;

	cout << "Case #" <<t+1<<": " << ans <<endl;
    ofs << "Case #" <<t+1<<": " << ans <<endl;

   } // end of test cases

 return 0;
}