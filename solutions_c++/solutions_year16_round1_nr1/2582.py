#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

#define N 100

typedef struct{
	int a, b;
}tipo;

bool compare (tipo x, tipo y){
	return x.a<y.a;
}


int main () {
  ofstream myfile;
  ifstream input;
  input.open("entrada.txt");
  myfile.open ("saida.txt");   
  int t;
  input>>t;
  vector<tipo> vt;
  string s;
  string ans;
  for(int i=1; i<=t; i++){
		input>>s;
		ans = "";
		ans+=s[0];
		for(int j=1; j<s.size(); j++){
			if(s[j]>=ans[0]){
				ans=s[j]+ans;
			}else{
				ans = ans + s[j];
			}
		}
		myfile<<"Case #"<<i<<": "<<ans<<endl;
		sort(vt.begin(), vt.end(), compare);
  }
  myfile.close();
  input.close();
  return 0;
}

