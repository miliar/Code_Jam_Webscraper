#include<fstream>
#include<iostream>
#include<sstream>
#include<cmath>
using namespace std;

int main(){
    ifstream infile("B-large.in");
    ofstream outfile("B-large.out");
    string line;
    getline(infile,line);
    int T,t=1;
	istringstream is(line);
	is>>T;

	while(t<=T){
	    getline(infile,line);
	    istringstream is1(line);
        double c,f,x;
        is1>>c>>f>>x;

        long double time=0;
        long double speed=2;
        while(x/speed>x/(speed+f)+c/speed){
            time+=c/speed;
            speed+=f;
        }
        time+=x/speed;

        outfile.precision(7);
        outfile<<"Case #"<<fixed<<t<<": "<<time<<endl;
		t++;
	}
	infile.close();
	outfile.close();

    return 0;
}
