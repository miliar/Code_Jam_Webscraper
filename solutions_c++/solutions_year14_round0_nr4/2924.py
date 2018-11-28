#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

	ifstream f;
    f.open("small.in");
    ofstream of;
    of.open("out.txt");
    int nbr_of_testcases;
    f >> nbr_of_testcases;
    for (int i = 1; i<=nbr_of_testcases ; i++) {
    	vector<double> naomi;
    	vector<double> ken;
    	int nbr_of_logs;
    	f >>nbr_of_logs;
    	for (int j = 0; j < nbr_of_logs; ++j)
    	 {
    	 	double in;
    	 	f >> in;
    	 	naomi.push_back(in);
    	 } 
    	for (int j = 0; j < nbr_of_logs; ++j)
    	 {
    	 	double in;
    	 	f >> in;
    	 	ken.push_back(in);
    	 } 
    	 //do stuff
    	sort(naomi.begin(),naomi.end(),[](double d1, double d2){return d1>d2;});
    	sort(ken.begin(),ken.end(),[](double d1, double d2){return d1>d2;});
    	//war
    	auto nb = naomi.begin();
    	auto ne = naomi.end();
    	auto kb = ken.begin();
    	auto ke = ken.end();
    	int wcount = 0;
    	while(nb!=ne && kb !=ke) {
    		if(*kb>*nb) {
    			++nb;
    			++kb;
    		} else {

    			++wcount;
    			++nb;
    			--ke;
    		}
    	}
    	//deceitfull war
    	sort(naomi.begin(),naomi.end());
    	sort(ken.begin(),ken.end());
    	nb = naomi.begin();
    	ne = naomi.end();
    	kb = ken.begin();
    	ke = ken.end();
    	--ke;
    	int dcount = 0;
    	while(nb!=ne) {
    		if(*nb<*kb) {
    			++nb;
    			--ke;
    		} else {
    			++dcount;
    			++nb;
    			++kb;
    		}

    	}
    	of << "Case #" << i << ": " << dcount << " " << wcount;
    	if (i!=nbr_of_testcases) {
    		of << endl;
    	}
    }
}