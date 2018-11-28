#include <climits>
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

void  testcase(int casex){
	double c, f ,x;
	cin >> c >>f >>x;
	
	double t =0;
	double r=2;
	while(x/r> x/(r+f)+c/r){
		t+= c/r;
		r+=f;
	}
	t+=x/r;
	cout << "Case #"<<casex<<": ";
	cout <<setprecision(7)<< fixed<<t<<endl;

}

int main()
{
	ios_base::sync_with_stdio(false);
	int cases;
	cin >> cases;
	for(int i =1; i<=cases;i++){
		testcase(i);  
	}

  return 0;
}
