#include <iostream>
#include <sstream>
#include <string>
#include <fstream>

using namespace std;

int main(){

	double c;
	long double f;
	long double x;
	const double s = 2;
	string line;
	int index;
	cout.precision(12);

	ifstream myfile ("/home/jack/Downloads/B-small-attempt0.in");
	if (myfile.is_open()){
		getline(myfile,line);
	} else cout << "Unable to open file"; 

	int cases = stoi(line);	

	for(int i = 0; i < cases; i++){

		if (myfile.is_open()){
			getline(myfile,line);
		} else cout << "Unable to open file"; 
		
	    istringstream iss(line);

	    string temp;
	    index = 0;
	    while (iss){
	    	iss>>temp;
	    	switch(index){
	    		case 0:
	    			c = atof(temp.c_str());
	    			//cout << "c= " << c << endl;
	    			break;
	    		case 1:
	    			//sscanf(temp.c_str(), "%Lf", &f);
	    			f = atof(temp.c_str());
	    			//cout <<"f= " << f << endl;
	    			break;
	    		case 2:
	    			//sscanf(temp.c_str(), "%Lf", &x);
	    			x = atof(temp.c_str());
	    			//cout<< "x= " << x << endl;
	    			break;
	    	}
	    	index++;   
	    }

	    double testTimes[10000];
	    double sum = 0;
	    double farms = 0;

	    for (int i = 0; i < 10000; i++){
	    	for (int j = 0; j < i; j++){
	    		sum += c/(s+farms);
	    		//cout<<"  "<<c/(s+i*f)<<endl;
	    		farms += f;
	    	}
	    	sum+= x/(s+farms);
	    	//cout<<"    "<<x/(s+(farms))<< "  ";
	    	testTimes[i] = sum;
	    	farms = 0;
	    	sum  = 0;
	    	//cout<< i << " TestTime: "<< testTimes[i]<<endl;
	    }

	    double min = testTimes[0];

	    for(int i = 0; i < 10000; i++){
	    	if (testTimes[i]< min){
	    		min = testTimes[i];
	    	}
	    }
	    cout<<"Case #" << i+1 << ": " << min<<endl;
	}
}