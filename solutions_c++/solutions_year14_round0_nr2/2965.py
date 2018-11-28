#include <cstdio>
#include <iostream>
#include <iomanip> 
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
int t, total;
cin>>t;
total=t;
while(t-- && t<=100){
bool flag = true;
double c,f,x,d=2.0;
double present, previous, tillNow=0, answer;
cin>>c>>f>>x;
while(flag)
{
	present = (double(x)/d) + tillNow;
	if(present > previous && tillNow)
	{
	answer = previous;
	flag = false;
	}
	tillNow = tillNow + (double(c)/d);
	d = d + f;
	previous = present;
}

cout << "Case #" << total-t << ": ";
cout<< fixed << setprecision(7) << answer << endl;

}
    return 0;
}
