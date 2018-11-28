#include "iostream"
#include "fstream"
#include "vector"
#include "math.h"
#include "string"

using namespace std;


int main(){
    int T;
    ifstream in("A-large.in");
    ofstream out("output.txt");
    in >>T;
    for(int i=0;i<T;i++){
		int N;
		in>>N;
		vector <int> aud;
		for(int j=0;j<=N;j++){
			char tp;
			in>>tp;
			aud.push_back(tp-'0');
		}
		int sum=0, ans=0;
		for(int j=0;j<=N;j++){
			if(sum<j){
				ans+=j-sum;
				sum=j;
			}
			sum+=aud[j];
		}
		out<<"Case #"<< i+1<<": "<<ans<<endl;
	}
}
